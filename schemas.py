from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PromptInput(BaseModel):
    prompt: str

class AppVersion(BaseModel):
    app_name: str
    version: Optional[int] = 1
    code: str
    timestamp: Optional[datetime]
