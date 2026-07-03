from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"message": "Bienvenido a la API de FastAPI!"}
