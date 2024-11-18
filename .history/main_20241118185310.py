from fastapi import FastAPI

app = FastAPI()

user_dict = {
    "user1": "password1",
    "user2": "password2"    
}
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/{user_name}")
def read_user(user_name: str):
    user_password = user_dict.get(user_name)
    return{"user_password": user_password}