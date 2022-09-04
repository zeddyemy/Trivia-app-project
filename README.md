# Trivia App

This project Trivia game app I created while learning API Development & Documentation at Udacity. I was tasked with building out API experience for the frontend. By completing this trivia app,  i have gained the ability to structure plan, implement, and test an API. It seemed a bit difficult at first, but i pulled through. The app currently has the following functionalities:

1. Displays questions - all questions are displayed and can also be displayed by category. Each Questions shows category and difficulty rating by default and can show/hide the answer.
2. Delete questions - Questions can be deleted.
3. Adding questions.
4. Searching for questions based on a text query string.
5. Playable quiz game, randomizing either all questions or within a specific category.

## Guidelines

Once again this is just a small project, so  feel free to expand on the project in any way you see fit. I'll also be the expanding on the project myself, to solidify my skills. For instance, you could add more styling, or make the app more responsive, add a timer for the quiz, whatever you want. "The sky's the limit."



## Getting Started

### Pre-requisites and Local Development 
Developers using this project should already have Python3, pip and node installed on their local machines.

### Backend

The [backend](./backend/README.md) directory contains a fully completed Flask and SQLAlchemy server. You can check out the `__init__.py` to see the defined endpoints. You can reference models.py for DB and SQLAlchemy setup. These are some of the files available in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`
3. `backend/models.py`
4. `backend/trivia.psql`
5. `backend/requirements.txt`

From the backend folder run `pip install requirements.txt`. All required packages are included in the requirements file. 

To run the application run the following commands: 
```
export FLASK_APP=flaskr
export FLASK_ENV=development
export FLASK_DEBUG=True
flask run
```
These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows OS, i advise you use gitBash.

The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration.

> View the [Backend README](./backend/README.md) for more details.

### Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. 

From the frontend folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
npm start 
```

By default, the frontend will run on localhost:3000.

> View the [Frontend README](./frontend/README.md) for more details.

### Tests
In order to run tests navigate to the backend folder and run the following commands: 

- For Mac and Linux Users
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
- For Windows Users:
```
psql -U postgres
drop database trivia_test;
create database trivia_test;
\q
psql -U postgres -d trivia_test -f trivia.psql
python test_flaskr.py
```

The first time you run the tests, omit the dropdb/drop database command. 

All tests are kept in that file and should be maintained as updates are made to app functionality.


## API Reference

### Getting Started
- Base URL: As this was a project to solidify my skills in API development, this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Also this application does not require authentication or API keys.

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed 
- 422: Not Processable 
- 500: Internal Server Error

### Endpoints 
#### GET /questions
- General:
    - Returns a list of categories objects, currentCategory objects, questions objects, success value, and total number of questions
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1. 
- Sample: `curl http://127.0.0.1:5000/questions`
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "currentCategory": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 20
}
```


#### DELETE /questions/{question_id}
- General:
    - Deletes the questions of the given ID if it exists. Returns the id of the deleted book, success value, total questions, and questions list based on current page number to update the frontend. 
- `curl -X DELETE http://127.0.0.1:5000/questions/24`
```
{
  "deleted": 24,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 19
}

```


#### POST /questions
- General:
    - Creates a new question using the submitted question, answer, difficulty and category. Returns the id of the created question, success value, total questions, and list of questions based on current page number to update the frontend. 
- `curl http://127.0.0.1:5000/questions?page=2 -X POST -H "Content-Type: application/json" -d '{"question":"who owns Tesla?", "answer":"Elon Musk", "difficulty":"1", "category":"1"}'`
```
{
  "created": 25,
  "questions": [
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "Elon Musk",
      "category": 1,
      "difficulty": 1,
      "id": 25,
      "question": "who owns Tesla?"
    }
  ],
  "success": true,
  "total_questions": 20
}
```

#### POST /search
- General:
    - Searches the database for questions that contain a given phrase. Returns list of questions that have the given phrase, a success value and total number of questions
- `curl http://127.0.0.1:5000/search?page=1 -X POST -H "Content-Type: application/json" -d '{"searchTerm":"Tesla"}'`
```
{
  "questions": [
    {
      "answer": "Elon Musk",
      "category": 1,
      "difficulty": 1,
      "id": 25,
      "question": "who owns Tesla?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```

#### GET /categories/{id}/questions
- General:
    - This endpoint get questions based on category. It returns list of questions from specified id, Current category, Success value and total questions
`curl -X GET http://127.0.0.1:5000/categories/4/questions`
```
{
  "current_category": "History",
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 4
}
```

#### POST /quizzes
- General:
    - This endpoint takes a category and previous question parameters and return a random questions within the given category. It returns a json format like below:
`curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"quiz_category":{"type":"Science","id":"1"}, "previous_questions":[21]}'`
```
{
  "previousQuestion": [
    21
  ],
  "question": {
    "answer": "Blood",
    "category": 1,
    "difficulty": 4,
    "id": 22,
    "question": "Hematology is a branch of medicine involving the study of what?"
  },
  "success": true
}
```

## Deployment N/A

## Authors
Yours truly, Emmanuel Olowu

## Acknowledgements 
The wonderful teacher Coach Caryn at Udacity and all of peers at Udacity!