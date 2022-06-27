from app.database import get_db
from fastapi import FastAPI  
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import app.crud as crud, app.models as models, app.schemas as schemas
from app.database import SessionLocal, engine
app = FastAPI()

@app.get('/user/')
def read_user(db: Session = Depends(get_db)):
    db_user = crud.get_all_users(db)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return db_user

# get user by id
@app.get('/user/{id}')
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return db_user

@app.post("/user")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email=user.email)
    if db_user:
         raise HTTPException(
                  status_code=status.HTTP_400_BAD_REQUEST, 
                  detail="Email already registered")
    return crud.create_user(db=db, user=user)
