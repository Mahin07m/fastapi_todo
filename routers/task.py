from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database,models,oauth2
from sqlalchemy.orm import Session

router = APIRouter()

get_db= database.get_db


@router.get('/task',response_model=List[schemas.ShowTask] ,tags= ['tasks'])
def all(db:Session= Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    tasks= db.query(models.Task).all()
    return tasks


@router.post('/task', status_code= status.HTTP_201_CREATED, tags= ['tasks'])
def create(request: schemas.Task, db:Session= Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    new_task = models.Task(title= request.title, content= request.content,user_id= request.user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get('/task/{id}', status_code=200, response_model= schemas.ShowTask,tags= ['tasks'])
def show(id, db:Session= Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    task=db.query(models.Task).filter(models.Task.id== id).first()
    if not task:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Task with the id {id} does not exist')
        
        # the other way 
        # response.status_code = status.HTTP_404_NOT_FOUND 
        # return {'details':f'Task with the id {id} does not exist'}
    return task


# @app.get('/task',tags= ['tasks'])
# def all(db:Session= Depends(get_db)):
#     tasks= db.query(models.Task).all()
#     return tasks


@router.delete ('/task/{id}', status_code= status.HTTP_204_NO_CONTENT,tags= ['tasks'])
def delete(id, db:Session= Depends(get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    task=db.query(models.Task).filter(models.Task.id== id)
    if not task.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} doesn't exist in the database")
    task.delete(synchronize_session=False)
    db.commit()
    return {'Task Deleted'}
    
    

@router.put ('/task/{id}', status_code= status.HTTP_202_ACCEPTED,tags= ['tasks'])
def update(id, request: schemas.Task, db:Session= Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    task=db.query(models.Task).filter(models.Task.id==id)
    if not task.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} doesn't exist in the database")
    task.update(request.dict())
    db.commit()
    return 'updated'
