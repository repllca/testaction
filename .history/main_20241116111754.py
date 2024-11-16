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

@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}