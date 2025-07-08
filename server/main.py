from fastapi import FastAPI
from app.routes import ai

app = FastAPI()
app.include_router(ai.router, prefix="/api/ai")
