from fastapi import APIRouter, File, UploadFile
from app.services.versioning import save_version
from app.services.ai_core import regenerate_from_upload
import shutil
import os

router = APIRouter(prefix="/upload", tags=["App Upload"])

@router.post("/legacy")
async def upload_legacy_app(file: UploadFile = File(...)):
    upload_path = f"temp/{file.filename}"
    
    # Save file
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Call AI regeneration logic
    regenerated_code = regenerate_from_upload(upload_path)

    # Save version
    app_name = file.filename.replace(".zip", "")
    save_version(app_name=app_name, code=regenerated_code)

    return {"message": "App regenerated successfully", "code": regenerated_code}


