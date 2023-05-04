from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db_config.connect import SessionFactory
from models.requests import ArtworkRequest
from models.models import Artwork
from repository.artwork import ArtworkRepository
from typing import List


router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/artwork/add")
def add_signup(req: ArtworkRequest, sess:Session = Depends(sess_db)):
    repo:ArtworkRepository = ArtworkRepository(sess)

    artwork = Artwork(
        description_id=req.description_id
        )
    
    result = repo.insert_artwork(artwork)
    if result == True:
        return artwork
    else: 
        return JSONResponse(content={'message':'create signup problem encountered'}, status_code=500)

@router.get("/artwork/list", response_model=List[ArtworkRequest])
def list_artworks(sess:Session = Depends(sess_db)):
    repo:ArtworkRepository = ArtworkRepository(sess)
    result = repo.get_all_artworks()

    return result


@router.patch("/artwork/update") 
async def update_artwork(artwork_id:int, req:ArtworkRequest, sess:Session = Depends(sess_db)): 
    artwork_dict = req.dict(exclude_unset=True)
    repo:ArtworkRepository = ArtworkRepository(sess)
    result = repo.update_artwork(artwork_id, artwork_dict )
    if result: 
        return JSONResponse(content={'message':'Artwork updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update artwork error'}, status_code=500)

@router.delete("/artwork/delete/{id}") 
async def delete_artwork(artwork_id:int, sess:Session = Depends(sess_db)): 
    repo:ArtworkRepository = ArtworkRepository(sess)
    result = repo.delete_artwork(artwork_id)
    if result: 
        return JSONResponse(content={'message':'artwork deleted successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete artwork error'}, status_code=500)

@router.get("/artwork/get/{id}")
async def get_login(id:int, sess:Session = Depends(sess_db)): 
    repo:ArtworkRepository = ArtworkRepository(sess)
    result = repo.get_artwork(id)
    return result