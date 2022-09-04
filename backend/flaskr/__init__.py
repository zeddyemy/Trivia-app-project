import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_results(request, results):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    the_results = [result.format() for result in results]
    current_results = the_results[start:end]

    return current_results

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    
    # @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    cors = CORS(app, resources = {r"/*":{"origins": "*"}})

    
    # @TODO: Use the after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response


    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories')
    def request_all_categories():

        categories = Category.query.all()
        
        formatted_categories = {}
        for category in categories:
            formatted_categories.update({category.id: category.type})

        return jsonify({
            'success': True,
            'categories': formatted_categories,
            'total_categories': len(categories)
        })


    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """
    @app.route('/questions')
    def request_all_questions():
        try:
            questions = Question.query.order_by(Question.id).all()
            current_questions = paginate_results(request, questions)

            if len(current_questions) == 0:
                abort(404)
            
            # get all categories
            categories = Category.query.all()
            currentCategory = paginate_results(request, categories)
            formatted_categories = {}
            for category in categories:
                formatted_categories.update({category.id: category.type})

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(questions),
                'categories': formatted_categories,
                'currentCategory': currentCategory,
            })
        except:
            abort(404)

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """
    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()
            questions = Question.query.order_by(Question.id).all()
            current_questions = paginate_results(request, questions)

            return jsonify(
                {
                    "success": True,
                    "deleted": question_id,
                    "questions": current_questions,
                    "total_questions": len(questions),
                }
            )

        except:
            abort(422)

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route("/questions", methods=["POST"])
    def post_question():
        body = request.get_json()

        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_difficulty = body.get("difficulty", None)
        new_category = body.get("category", None)

        try:
            question = Question(
                question=new_question,
                answer=new_answer,
                difficulty=new_difficulty,
                category = new_category
            )
            question.insert()

            questions = Question.query.order_by(Question.id).all()
            current_questions = paginate_results(request, questions)

            return jsonify(
                {
                    "success": True,
                    "created": question.id,
                    "questions": current_questions,
                    "total_questions": len(questions),
                }
            )

        except:
            abort(422)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route("/search", methods=["POST"])
    def search_by_phrase():
        body = request.get_json()

        searchTerm = body.get('searchTerm')

        if searchTerm:
            questions = Question.query.order_by(Question.id).filter(
                Question.question.ilike("%{}%".format(searchTerm))
            ).all()
            
            current_questions = paginate_results(request, questions)

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(questions)
            })
        else:
            abort(404)

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route("/categories/<int:category_id>/questions")
    def questions_in_category(category_id):
        # fetch category by id
        category = Category.query.filter(Category.id == category_id).one_or_none()
        
        # if category is none return a 404 status code
        if category is None:
            abort(404)
        
        else:
            # fetch questions that belong in a category
            questions = Question.query.filter(Question.category == str(category_id)).all()
            current_questions = paginate_results(request, questions)

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(questions),
                'current_category': category.type
            })
    

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """
    @app.route('/quizzes', methods=['POST'])
    def quiz():
        # get the question category an the previous question
        body = request.get_json()
        previousQuestion = body.get('previous_questions')
        quiz_category = body.get('quiz_category')

        try:
            if (quiz_category['id'] == 0):
                questions = Question.query.all()
            else:
                questions = Question.query.filter(
                    Question.category == quiz_category['id']
                ).all()

            # generate random question from the Queried Questions
            randomKey = random.randint(0, len(questions)-1)
            randomQuestion = questions[randomKey]

            # check if random question has been shown,
            # if it hasn't, send it to the frontend.
            while randomQuestion.id not in previousQuestion:
                randomQuestion = questions[randomKey]
                return jsonify({
                    'success': True,
                    'question': {
                        "answer": randomQuestion.answer,
                        "category": randomQuestion.category,
                        "difficulty": randomQuestion.difficulty,
                        "id": randomQuestion.id,
                        "question": randomQuestion.question
                    },
                    'previousQuestion': previousQuestion
                })

        except:
            abort(404)

    
    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    # Error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request."
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404
    
    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "The request was well-formed but was unable to be followed due to semantic errors."
        }), 422
    
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not allowed."
        }), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            'error': 500,
            "message": "Internal server error"
        }), 500

    return app

