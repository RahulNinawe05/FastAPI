# Run - uvicorn main:app --reload
from fastapi import FastAPI,Path
import json
app = FastAPI()

def Load_data():
    with open("cars.json", 'r') as f:
        data = json.load(f)
    return data 

@app.get("/&")
def rahul():
    return {"message": "Hii I am Rahul, I am interestd in Machine Learning"}

@app.get("/@")
def Show():
    data = Load_data()

    return data

@app.get("/Cars/{Cars_id}")
def Show_Cars_Data(Cars_id: int = Path(..., description="ID Present in ShowRoom Database", example="1", ge=1, le=10)):
    data = Load_data()

    for car in data:
        if car['id'] == Cars_id:
            return car
    
    return {"error": "cars data not found"}