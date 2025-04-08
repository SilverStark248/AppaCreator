from fastapi import FastAPI
from app.routes import prompt_engine, upload_app

app = FastAPI(title="NovaForge Backend")

app.include_router(prompt_engine.router)
app.include_router(upload_app.router)

@app.get("/")
def root():
    return {"message": "NovaForge backend is running"}
