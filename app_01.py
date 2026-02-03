# Run - uvicorn app_01:app --reload
from fastapi import FastAPI,Path, HTTPException,Query
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

@app.get("/cars/{cars_id}")
def Show_Cars_Data(cars_id: int = Path(..., description="ID Present in ShowRoom Database", example="1", ge=1, le=10)):
    data = Load_data()

    for car in data:
        if car['id'] == cars_id:
            return car
    
    raise HTTPException(status_code=404, detail="cars data not found")

@app.get("/sort")
def sorting_data(
    sort_by: str = Query(..., description="Sorting By 'brand','model','year','transmission"),
    order_by: str = Query("asc",description="The Order Sorting is 'asc','desc'"),
    page: int = Query(1,ge=1),
    limit: int = Query(2, ge=2, le=50)
):
    valid_field = ['brand', 'model', 'year', 'transmission']

    if sort_by not in valid_field:
        raise HTTPException(status_code=400, detail=f"Invalid Field {valid_field}")
    
    if order_by not in ['asc', 'desc']:
        raise HTTPException(status_code=400,detail="Invlid Order, Select 'asc' OR 'desc' ")
    
    data = Load_data()

    sort_order  = True if order_by== 'desc' else False
    
    sorted_data = sorted(
        data, 
        key = lambda x: str(x.get(sort_by, "")).lower(), 
        reverse= sort_order
        )
    
    start = (page - 1) * limit

    end = start + limit

    paginated_data = sorted_data[start:end]

    return {
        "page": page,
        "limit": limit,
        "total": len(sorted_data),
        "data": paginated_data
    }

# EX.- "http://127.0.0.1:8000/sort?sort_by=brand&order_by=desc"
