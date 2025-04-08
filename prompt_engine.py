from fastapi import APIRouter
from app.services.ai_core import generate_code_from_prompt
from pydantic import BaseModel

router = APIRouter(prefix="/prompt", tags=["Prompt Engine"])

class PromptInput(BaseModel):
    prompt: str

@router.post("/generate")
async def handle_prompt(input: PromptInput):
    return generate_code_from_prompt(input.prompt)
