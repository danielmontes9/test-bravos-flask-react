# Test Bravos Flask React

This project was developed using Flask and consumes the free [Dog API](https://dogapi.dog/docs/api-v2). It also includes endpoint testing to ensure the reliability and correctness of the API integration.

## Backend

### Requirements
- Python 3.7+
- pip (Python package manager)


### How to Run This Flask Project
1. Clone the Repository
```bash
  git clone https://github.com/danielmontes9/test-bravos-flask-react.git
  cd test-bravos-flask-react/dog-flask-app
```

2. Install Dependencies
```bash
  pip install flask
```

3. Run the Flask App
```bash
  python dog_api_backend.py
```
The app will run at: http://127.0.0.1:5000/

4. Run the test
```bash
  python test_endpoints.py
```
Note: Your app must be running at the same time.