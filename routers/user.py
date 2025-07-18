import schemas, database,models
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from hashing import Hash


router = APIRouter()
get_db= database.get_db

@router.post('/user',response_model= schemas.ShowUser,tags= ['user'] )
def create_user(request:schemas.User,  db:Session= Depends(get_db)):
    new_user = models.User(name= request.name,email= request.email,password= Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/user/{id}', status_code=200, response_model= schemas.ShowUser,tags= ['user'])
def show(id, db:Session= Depends(get_db)):
    user=db.query(models.Task).filter(models.User.id== id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} does not exist')
    return user