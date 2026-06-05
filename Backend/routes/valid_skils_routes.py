from fastapi import APIRouter, HTTPException
from utils.database import verified_skills # Use the MongoDB collection, not the Pydantic schema

router = APIRouter()

@router.post("/show_valid_skills/{user_id}")
async def show_valid_skills(user_id: str):
    """Returns valid_skills. Creates an empty document for the user if not found."""
    try:
        # 1. Look for the user in the collection
        document = await verified_skills.find_one({"user_id": user_id})
        
        # 2. If not found, create the default schema and insert it
        if not document:
            document = {
                "user_id": user_id,
                "verified_skills": [] 
            }
            await verified_skills.insert_one(document.copy())
            
        # 3. Clean up the response
        document.pop("_id", None)
        return document

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))