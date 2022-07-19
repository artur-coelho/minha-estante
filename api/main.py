from app.database import get_db
from fastapi import FastAPI  
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import app.crud as crud, app.models as models, app.schemas as schemas
from app.database import SessionLocal, engine
app = FastAPI()

@app.get('/user/')
def listar_todos_usuarios(db: Session = Depends(get_db)):
    db_user = crud.listar_todos_usuarios(db)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Usuário não encontrado.")
    return db_user

@app.get('/user/{id}')
def listar_usuario_por_id(id: int, db: Session = Depends(get_db)):
    db_user = crud.buscar_usuario_por_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Usuário não encontrado.")
    return db_user

@app.post("/user")
def adicionar_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.buscar_usuario_por_email(db, user_email=user.email)
    if db_user:
         raise HTTPException(
                  status_code=status.HTTP_400_BAD_REQUEST, 
                  detail="O email já existe.")
    return crud.criar_usuario(db=db, user=user)

@app.post("/livro")
def adicionar_livro(livro: schemas.Livro, db: Session = Depends(get_db)):
   
    # db_user = crud.get_user_by_id(db, id=id)
    # if db_user:
    #      raise HTTPException(
    #               status_code=status.HTTP_400_BAD_REQUEST, 
    #               detail="Id Nao existe")
    return crud.create_livro(db=db, livro=livro)

@app.get('/livros/')
def listar_livros(db: Session = Depends(get_db)):
    db_livro = crud.listar_todos_os_livros(db)
    if db_livro is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="O usuário não existe.")
    return db_livro

@app.put("/livros/{isbn}")
def atualizar_livros(isbn:int, livro:schemas.LivroUpdate, session = Depends(get_db)):
    livroObj = session.query(models.Livro).get(isbn)
    if livroObj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Livro não encontrado.")
    livroObj.nome = livro.nome
    livroObj.descricao = livro.descricao
    livroObj.edicao = livro.edicao
    livroObj.editora = livro.editora
    livroObj.genero = livro.genero
    livroObj.tipo_capa = livro.tipo_capa
    session.commit()
    return "O livro foi atualizado."

@app.delete("/{id}")
def apagar_livros(isbn:int, session = Depends(get_db)):
    livroObj = session.query(models.Livro).get(isbn)
    if livroObj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Livro não encontrado.")
    session.delete(livroObj)
    session.commit()
    session.close()
    return 'O livro foi apagado.'

