import datetime
from typing import List, Optional  
from pydantic import BaseModel
    
 

class UserBase(BaseModel):
    nome: str
    email: str
class UserCreate(UserBase):
    senha: str
class User(UserBase):
    id: int
    
class Config:         
        orm_mode = True


class LivroBase(BaseModel):
    pass


class LivroCreate(LivroBase):
    pass

class LivroUpdate(LivroBase):
    edicao: Optional[str]
    editora: Optional[str]
    nome:Optional[str]
    descricao: Optional[str]
    tipo_capa: Optional[str]
    genero:Optional[str]

class Livro(LivroBase):
    isbn: int
    usuario_id: Optional[int]
    edicao: Optional[str]
    editora: Optional[str]
    nome:Optional[str]
    descricao: Optional[str]
    tipo_capa: Optional[str]
    genero:Optional[str]
    data_cadastro: datetime.datetime
   

    def dict(self, *args, **kwargs):
        # Force conversion to dict not use alias
        kwargs.update(by_alias=False, exclude_none=True, exclude_defaults=True)
        return super().dict(*args, **kwargs)

    class Config:
        orm_mode = True
        validate_assignment = True
        by_alias = False