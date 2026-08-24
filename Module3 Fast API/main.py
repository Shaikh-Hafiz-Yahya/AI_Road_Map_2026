# pip Requirement: (python -m pip install fastapi uvicorn pyd)

# uvicorn --> 'server ha fastapi ka'
# pydantic(pyd) --> is a 'translator'

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {

        "Message":"Hello World"

    }

@app.get('/about')
def about():

    return {

        "Message":"Hello my name is Aatif and I am a Doctor"

        }
# python -m uvicorn main:app --reload

 