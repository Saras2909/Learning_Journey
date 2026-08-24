from fastapi import FastAPI
app = FastAPI()

products = {
    "Electronics": {
        "Laptop": 55000,
        "Smartphone": 25000,
        "Headphones": 3000,
        "Keyboard": 1500
    },

    "Clothing": {
        "T-Shirt": 800,
        "Jeans": 1800,
        "Jacket": 3500,
        "Shoes": 2500
    },

    "Grocery": {
        "Rice": 1200,
        "Wheat": 600,
        "Milk": 70,
        "Eggs": 120
    },

    "Furniture": {
        "Chair": 2500,
        "Table": 7000,
        "Sofa": 25000,
        "Bed": 18000
    },

    "Books": {
        "Python": 600,
        "Java": 700,
        "Database": 800,
        "Machine Learning": 1200
    }
}

users = [
    {
        "user_id": 101,
        "name": "Saras",
        "risk_score": 0.12,
        "city": "Chennai"
    },
    {
        "user_id": 102,
        "name": "Krish",
        "risk_score": 0.78,
        "city": "Mumbai"
    },
    {
        "user_id": 103,
        "name": "Rahul",
        "risk_score": 0.45,
        "city": "Delhi"
    },
    {
        "user_id": 104,
        "name": "Aman",
        "risk_score": 0.91,
        "city": "Bangalore"
    },
    {
        "user_id": 105,
        "name": "Priya",
        "risk_score": 0.23,
        "city": "Hyderabad"
    },
    {
        "user_id": 106,
        "name": "Riya",
        "risk_score": 0.67,
        "city": "Pune"
    },
    {
        "user_id": 107,
        "name": "Arjun",
        "risk_score": 0.35,
        "city": "Kolkata"
    },
    {
        "user_id": 108,
        "name": "Neha",
        "risk_score": 0.84,
        "city": "Jaipur"
    },
    {
        "user_id": 109,
        "name": "Vikram",
        "risk_score": 0.56,
        "city": "Ahmedabad"
    },
    {
        "user_id": 110,
        "name": "Ananya",
        "risk_score": 0.18,
        "city": "Chandigarh"
    }
]

@app.get("/product/{category}") #Category used as path
def greeting(category:str,product:str): #product used as query
    if category not in products:
        return {"message":"Category Not Found"}
    if product not in products[category]:
        return {"message":"Product Not Found"}
    return {"message":f"The price of {product} is {products[category][product]}"}

@app.get("/users")
def get_users(city:str,min_score:float=0):
    result = [x for x in users if(x["city"] == city and x["risk_score"]>= min_score)] #For filtering we used query parameter
    return result

@app.get("/greeting")
def greeting(name: str | None = None):
    if name:
        return {"message":f"Hello {name}"}
    else:
        return {"message":"Hello World"}