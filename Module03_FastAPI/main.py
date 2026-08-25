#                    Topic: (First API Code, Decorators, Routes & Docs Explained)
# ________________________________________________________________________________________________
# ------------------------------------------------------------
# pip Requirement: --> python -m pip install fastapi uvicorn pyd
# virtual Environment command: --> python -m venv fapi
# ------------------------------------------------------------
# uvicorn --> 'server ha fastapi ka'
# pydantic(pyd) --> is a 'translator'
# ------------------------------------------------------------
# {2:4} --> Dictionary
# {'2':4} --> JSON ()
# ------------------------------------------------------------
# 2. JSON kya hai?
# JSON = JavaScript Object Notation
# JSON ek data exchange format hai. Iska purpose different applications/systems ke darmiyan data transfer karna hai.
# JSON:
# {
#     "name": "Aatif",
#     "age": 25,
#     "doctor": true
# }
# ------------------------------------------------------------
# Ye Python dictionary jaisa dikh raha hai, lekin technically ye JSON data hai.
# Notice:
# Python:
# "doctor": True
# "doctor": True

# JSON:
# "doctor": true
# ------------------------------------------------------------
# Python mein:
# True
# False
# None

# JSON mein:
# true
# false
# null
# ------------------------------------------------------------


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

 