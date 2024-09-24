# Fyle Backend Intern Assignment

This project is a solution to the Fyle Backend Intern assignment. It includes a fully functional Flask backend with key features such as assignment submission, grading, and validation states (DRAFT, SUBMITTED, GRADED). The application is designed to be set up locally or run with Docker.

## Results
- I had tested and tried all the Existing as well as missing APIs and given my best to develop them here is the Link where you can check them and review.
- https://www.postman.com/abhigawande123/workspace/remote-bricks-apis/collection/36164059-1eaad4af-d47d-4d08-9dc0-0ef68f62bdba?action=share&creator=36164059 
- I had also attached the screenshots of the (pytest --cov & pytest -vvv -s tests/) in the Output folder.

## Note:
- Whether i will be considered for this position or not but i would like to give an feedback regarding the data in the database schema of the assignment is having some issue.
    1.The Default STATE of the assignment is set to GRADED and whenever there is some change to do that the tests through an error.So please Take a look at that it will be helpful for other candidates.
    Please consider redesigning your database schema for this assignments.

## Prerequisites

- Python 3.8 or higher
- Virtualenv
- Docker (optional, for containerized setup)

## Project Setup

### Local Setup

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```

### Docker Setup

### Build the Docker Image

```
docker build -t fyle-backend-intern .
```
### Run the Docker Container

```
docker run -p 5000:5000 fyle-backend-intern
```
### Visit Live Server

```
http://localhost:5000
```



