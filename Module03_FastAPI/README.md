# FastAPI — First API Code, Decorators, Routes & Docs

This module introduces the fundamentals of **FastAPI**, including:

- FastAPI installation
- Virtual environment
- Uvicorn
- Pydantic
- First FastAPI application
- Routes
- GET requests
- Decorators
- JSON responses
- Python Dictionary vs JSON
- Swagger UI / API Documentation
- Running FastAPI with Uvicorn

---

## 📌 1. Requirements

Before starting FastAPI, install the required packages.

### Install FastAPI and Uvicorn

```bash
python -m pip install fastapi uvicorn
```

> **Note:** FastAPI uses Pydantic for data validation and serialization. Installing FastAPI normally installs Pydantic as a dependency.

---

## 🐍 2. Create a Virtual Environment

It is recommended to create a separate virtual environment for each Python project.

```bash
python -m venv fapi
```

This creates a virtual environment named:

```text
fapi
```

### Activate the Virtual Environment on Windows

PowerShell:

```powershell
.\fapi\Scripts\Activate.ps1
```

Command Prompt:

```cmd
fapi\Scripts\activate
```

After activation, the terminal usually shows:

```text
(fapi)
```

---

# 🚀 3. Important FastAPI Components

## Uvicorn

Uvicorn is the **ASGI server** used to run FastAPI applications.

Simple understanding:

> **Uvicorn = FastAPI application ko run karne wala server**

We can start our FastAPI application using:

```bash
python -m uvicorn main:app --reload
```

---

## Pydantic

Pydantic is used by FastAPI for:

- Data validation
- Data parsing
- Data serialization
- Defining structured data models

Simple understanding:

> **Pydantic = incoming/outgoing data ko validate aur structure karne mein help karta hai.**

---

# 📦 4. First FastAPI Application

Create a file named:

```text
main.py
```

Then write:

```python
from fastapi import FastAPI

app = FastAPI()
```

### Explanation

```python
from fastapi import FastAPI
```

This imports the `FastAPI` class from the FastAPI package.

```python
app = FastAPI()
```

This creates the FastAPI application object.

Here:

```text
app
```

is our FastAPI application instance.

---

# 🛣️ 5. First API Route

Let's create our first route:

```python
@app.get('/')
def home():
    return {
        "Message": "Hello World"
    }
```

This creates a GET endpoint at:

```text
/
```

So when we open:

```text
http://127.0.0.1:8000/
```

we get:

```json
{
    "Message": "Hello World"
}
```

---

# 🧩 6. What is a Route?

A **route** defines:

1. The URL/path
2. The HTTP method
3. The function that should execute

For example:

```python
@app.get('/')
def home():
    return {
        "Message": "Hello World"
    }
```

Here:

```text
@app.get('/')
```

means:

> When a GET request comes to `/`, execute the `home()` function.

---

# 🎯 7. What is a Decorator?

This line:

```python
@app.get('/')
```

is called a **decorator**.

The decorator tells FastAPI:

> "This function should be used when a GET request is made to `/`."

The function below the decorator:

```python
def home():
```

is connected to that route.

### General Structure

```python
@app.get("/path")
def function_name():
    return something
```

For example:

```python
@app.get("/")
def home():
    return {
        "Message": "Hello World"
    }
```

---

# 🌐 8. About Route

We can create another route:

```python
@app.get('/about')
def about():

    return {
        "Message": "Hello my name is Aatif and I am a Doctor"
    }
```

Now our API has two routes:

| Method | Route | Function |
|---|---|---|
| GET | `/` | `home()` |
| GET | `/about` | `about()` |

---

# 📝 9. Complete `main.py`

Our complete first FastAPI code is:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {
        "Message": "Hello World"
    }


@app.get('/about')
def about():
    return {
        "Message": "Hello my name is Aatif and I am a Doctor"
    }
```

---

# ▶️ 10. Run the FastAPI Application

Open the terminal inside the folder containing `main.py`.

Run:

```bash
python -m uvicorn main:app --reload
```

---

## 🔍 Understanding the Command

```text
python -m uvicorn main:app --reload
```

### `python -m uvicorn`

Runs Uvicorn through Python.

### `main`

Refers to:

```text
main.py
```

### `:app`

Refers to:

```python
app = FastAPI()
```

So:

```text
main:app
```

means:

> Find the `app` object inside `main.py`.

### `--reload`

Automatically reloads the server whenever the Python source code changes.

This is very useful during development.

---

# 🖥️ 11. Expected Uvicorn Output

After running:

```bash
python -m uvicorn main:app --reload
```

you should see something similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

The important part is:

```text
http://127.0.0.1:8000
```

This means our FastAPI server is running successfully.

---

# 🌍 12. Test the Home Route

Open your browser:

```text
http://127.0.0.1:8000/
```

Response:

```json
{
    "Message": "Hello World"
}
```

---

# 👨‍⚕️ 13. Test the About Route

Open:

```text
http://127.0.0.1:8000/about
```

Response:

```json
{
    "Message": "Hello my name is Aatif and I am a Doctor"
}
```

---

# 📚 14. FastAPI Automatic Documentation

One of the powerful features of FastAPI is its automatic API documentation.

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

This opens the **Swagger UI**.

Swagger UI allows us to:

- See available API routes
- See HTTP methods
- Test endpoints
- Send requests directly from the browser
- View API responses

For example, you will see:

```text
GET /
GET /about
```

You can expand an endpoint and click:

```text
Try it out
```

Then:

```text
Execute
```

to test the API.

---

# 📖 15. JSON vs Python Dictionary

This is an important concept when working with FastAPI.

## Python Dictionary

A dictionary is a Python data structure.

```python
person = {
    "name": "Aatif",
    "age": 25,
    "doctor": True
}
```

Check its type:

```python
print(type(person))
```

Output:

```text
<class 'dict'>
```

Therefore:

```text
Dictionary = Python data structure
```

---

# 🔄 16. What is JSON?

JSON stands for:

> **JavaScript Object Notation**

JSON is a **data interchange/exchange format** commonly used to transfer structured data between applications and systems.

Example:

```json
{
    "name": "Aatif",
    "age": 25,
    "doctor": true
}
```

JSON looks very similar to a Python dictionary, but they are not exactly the same thing.

---

# ⚖️ 17. Python Dictionary vs JSON

### Python Dictionary

```python
{
    "name": "Aatif",
    "age": 25,
    "doctor": True
}
```

### JSON

```json
{
    "name": "Aatif",
    "age": 25,
    "doctor": true
}
```

Notice the difference:

| Python | JSON |
|---|---|
| `True` | `true` |
| `False` | `false` |
| `None` | `null` |

---

# 🧠 18. Easy Way to Remember

> **Dictionary = Python ke andar data structure**

> **JSON = systems/applications ke darmiyan data exchange format**

For example:

```text
Python Dictionary
       ↓
     FastAPI
       ↓
 JSON Response
       ↓
 Browser / Client
```

When we write:

```python
@app.get('/')
def home():
    return {
        "Message": "Hello World"
    }
```

we are returning a **Python dictionary** from our Python function.

FastAPI processes the response and provides it as a JSON response to the client.

---

# 🔢 19. Important Syntax Difference

A Python dictionary can use single or double quotes:

```python
student = {
    'name': 'Yahya',
    'age': 25
}
```

or:

```python
student = {
    "name": "Yahya",
    "age": 25
}
```

JSON uses double quotes for strings and property names:

```json
{
    "name": "Yahya",
    "age": 25
}
```

---

# 🧪 20. Simple API Example

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "Message": "Hello World"
    }


@app.get("/student")
def student():
    return {
        "name": "Muhammad Yahya",
        "field": "Artificial Intelligence",
        "semester": 7
    }
```

Test:

```text
http://127.0.0.1:8000/student
```

Response:

```json
{
    "name": "Muhammad Yahya",
    "field": "Artificial Intelligence",
    "semester": 7
}
```

---

# 🧩 21. Common FastAPI Project Structure

A simple FastAPI project can look like:

```text
Module3 Fast API/
│
├── fapi/
│   └── ...
│
└── main.py
```

The important file at this stage is:

```text
main.py
```

---

# ⚠️ 22. Common Uvicorn Problem

If you run:

```bash
python -m uvicorn main:app --reload
```

from the wrong directory, Uvicorn may not find `main.py`.

For example, if your structure is:

```text
AI_Road_Map_2026/
│
└── Module3 Fast API/
    └── main.py
```

and the terminal is currently here:

```text
AI_Road_Map_2026>
```

then first move into the correct directory:

```powershell
cd ".\Module3 Fast API"
```

Then run:

```powershell
python -m uvicorn main:app --reload
```

---

# 🔁 23. WatchFiles and Auto Reload

When using:

```bash
python -m uvicorn main:app --reload
```

Uvicorn watches the project files for changes.

If you modify:

```text
main.py
```

you may see:

```text
WatchFiles detected changes in 'main.py'. Reloading...
```

This is **not necessarily an error**.

It means Uvicorn detected a code change and restarted the development server.

---

# 📌 24. Important Commands Cheat Sheet

### Install FastAPI

```bash
python -m pip install fastapi
```

### Install Uvicorn

```bash
python -m pip install uvicorn
```

### Create virtual environment

```bash
python -m venv fapi
```

### Activate virtual environment — PowerShell

```powershell
.\fapi\Scripts\Activate.ps1
```

### Start FastAPI

```bash
python -m uvicorn main:app --reload
```

### Main API

```text
http://127.0.0.1:8000/
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

# 🎯 25. Concepts Learned

At this stage, we have learned:

- [x] FastAPI installation
- [x] Virtual environment
- [x] Uvicorn
- [x] Pydantic introduction
- [x] Creating a FastAPI application
- [x] `FastAPI()`
- [x] `app` object
- [x] Routes
- [x] GET requests
- [x] Decorators
- [x] Endpoint functions
- [x] JSON responses
- [x] Python Dictionary
- [x] Dictionary vs JSON
- [x] `main:app`
- [x] `--reload`
- [x] Swagger UI
- [x] `/docs`
- [x] Basic debugging when `main.py` cannot be found

---

# 🧠 Quick Revision

### FastAPI

```python
from fastapi import FastAPI

app = FastAPI()
```

### Route

```python
@app.get("/")
def home():
    return {
        "Message": "Hello World"
    }
```

### Uvicorn

```bash
python -m uvicorn main:app --reload
```

### Swagger

```text
http://127.0.0.1:8000/docs
```

### Basic Flow

```text
Client
   ↓
HTTP GET Request
   ↓
FastAPI Route
   ↓
Python Function
   ↓
Python Dictionary
   ↓
JSON Response
   ↓
Client
```

---

# 🚀 What's Next?

After understanding the first API, the next important FastAPI concepts are:

1. Path Parameters
2. Query Parameters
3. Request Body
4. Pydantic Models
5. Data Validation
6. POST Requests
7. PUT Requests
8. DELETE Requests
9. HTTP Status Codes
10. Response Models
11. Error Handling
12. Dependency Injection
13. Routers
14. Database Integration
15. Authentication & Authorization
16. Async/Await
17. Middleware
18. Project Structure
19. Testing
20. Deployment

---

## 📚 Learning Note

This README is part of an ongoing **FastAPI learning journey**.

As new concepts, commands, code examples, errors, debugging solutions, and best practices are learned, they can be added to this documentation to eventually build a complete **FastAPI Handbook**.
