from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db_config.connect import SessionFactory
from models.requests import UserRequest
from models.models import User
from models.views import UserView
from repository.user import UserRepository
from typing import List


router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/user/add")
def add_user(req: UserRequest, sess:Session = Depends(sess_db)) -> UserView:
    repo:UserRepository = UserRepository(sess)

    user = User(
        firstname = req.firstname,
        lastname = req.lastname,
        )
    
    result = repo.insert_user(user)
    if result == True:
        return user
    else: 
        return JSONResponse(content={'message':'create signup problem encountered'}, status_code=500)

@router.get("/user/list", response_model=List[UserView])
def list_users(sess:Session = Depends(sess_db)):
    repo:UserRepository = UserRepository(sess)
    result = repo.get_all_users()
    return result


@router.patch("/user/update") 
async def update_user(user_id:int, req:UserRequest, sess:Session = Depends(sess_db)): 
    user_dict = req.dict(exclude_unset=True)
    repo:UserRepository = UserRepository(sess)
    result = repo.update_user(user_id, user_dict )
    if result: 
        return JSONResponse(content={'message':'User updated successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'update user error'}, status_code=500)

@router.delete("/user/delete/{id}") 
async def delete_user(user_id:int, sess:Session = Depends(sess_db)): 
    repo:UserRepository = UserRepository(sess)
    result = repo.delete_user(user_id)
    if result: 
        return JSONResponse(content={'message':'user deleted successfully'}, status_code=201)
    else: 
        return JSONResponse(content={'message':'delete user error'}, status_code=500)

@router.get("/user/get/{id}")
async def get_user(id:int, sess:Session = Depends(sess_db)): 
    repo:UserRepository = UserRepository(sess)
    result = repo.get_user(id)
    return result