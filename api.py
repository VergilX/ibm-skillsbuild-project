from fastapi import Depends, FastAPI, WebSocket, HTTPException, status, Request, Cookie,  Form, WebSocketDisconnect, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr
from typing import Annotated, Optional

import requests

API_KEY = "MgVdm6w-DvhBlw9XxYaKaXW-cAwEdRa0k_cBw6tJSwte"

templates = Jinja2Templates(directory="frontend")

app = FastAPI()

# Middleware

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
            request=request,
            name="index.html"
    )

# async def predict(request: Request, data: HeartData = Form(...)):

@app.post("/predict")
async def predict(
    request: Request,
    age: int = Form(...),
    sex: int = Form(...),
    chest_pain_type: int = Form(...),
    bp: int = Form(...),
    cholestrol: int = Form(...),
    fbs_over: int = Form(...),
    ekg: int = Form(...),
    max_hr: int = Form(...),
    exercise_angina: int = Form(...),
    st_depression: float = Form(...),
    slope_st: int = Form(...),
    vessels_fluro: int = Form(...),
    thallium: int = Form(...),
    ):
    # Obtain the token
    token_response = requests.post(
        'https://iam.cloud.ibm.com/identity/token',
        data={
            "apikey": API_KEY,
            "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'
        }
    )
    mltoken = token_response.json()["access_token"]

    # Define headers with the obtained token
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # Define input fields and values
    array_of_input_fields = ["Age", "Sex", "Chest pain type", "BP", "Cholesterol", "FBS over 120", "EKG results", "Max HR", "Exercise angina", "ST depression", "Slope of ST", "Number of vessels fluro", "Thallium"]
    array_of_values_to_be_scored = [age, sex, chest_pain_type, bp, cholestrol, fbs_over, ekg, max_hr, exercise_angina, st_depression, slope_st, vessels_fluro, thallium]

    # Define payload for scoring
    payload_scoring = {
        "input_data": [
            {
                "fields": array_of_input_fields,  # Fixed 'field' to 'fields'
                "values": [array_of_values_to_be_scored]  # Include both sets of values
            }
        ]
    }

    # Send the scoring request
    response_scoring = requests.post(
        'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/heartdiseaseapi/predictions?version=2021-05-01',
        json=payload_scoring,
        headers=header
    )

    # Print the scoring response
    print("Scoring response")
    result = response_scoring.json()['predictions'][0]['values'][0]
    print(result)
    prediction = "Heart disease present" if result[0] == 'Presence' else "Heart disease not present"
    prob = result[1][1]
    print(f"prediction: {prediction}, prob: {prob}")

    return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "prediction": prediction,
                "probability": prob,
            }
    )
    # Change to result page
    return response_scoring.json()
