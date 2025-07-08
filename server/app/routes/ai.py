from fastapi import APIRouter, Request
from app.controllers.ai_controller import generate_content

router = APIRouter()

@router.post("/generate")
async def generate(request: Request):
    body = await request.json()
    return await generate_content(body)
