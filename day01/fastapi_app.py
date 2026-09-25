from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Pltform architect API is running"}