from sqlalchemy.orm import Session
import app.models as models, app.schemas as schemas


def criar_usuario(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def listar_todos_usuarios(db: Session):
    usuarios = db.query(models.User).all()
    return usuarios

def listar_todos_os_livros(db: Session):
    livros = db.query(models.Livro).all()
    return livros

def buscar_usuario_por_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()

def buscar_usuario_por_email(db: Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()
    
def delete_user(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()

def apagar_usuario(db: Session, id: int) -> bool:
    if user := delete_user(db, id):
        db.delete(user)
        db.commit()
        return True

    return False

def criar_livro(db: Session, livro: schemas.Livro):
    db_livro = models.Livro(**livro.dict())
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro