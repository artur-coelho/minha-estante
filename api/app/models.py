import uuid
from typing import List

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    LargeBinary,
    func,
    TIMESTAMP,
    Sequence,
    JSON,
    Table,
)
from sqlalchemy.dialects.postgresql import JSONB, ENUM
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql.sqltypes import Float
from app.database import Base
from datetime import datetime, timezone




class User(Base):
    __tablename__ = "usuario"  # noqa

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, primary_key=True, unique=True)
    email = Column(String, primary_key=True, unique=True)
    senha = Column(String, primary_key=True, unique=True)

class Livro(Base):
    __tablename__ = "livro"  # noqa
    __table_args__ = {"extend_existing": True}

    isbn = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    #estante_id = relationship("estante", backref="owner", overlaps="metainfo")
    edicao = Column(String)
    editora =  Column(String)
    nome =  Column(String)
    descricao =  Column(String)
    tipo_capa = Column(String)
    genero =  Column(String)
    data_cadastro = Column(TIMESTAMP(timezone=True), default=func.now()) 


    @validates("metainfo_json")
    def metainfo_json_validator(self, key, value):
        if value is None:
            return None
        return value

  


# class Metainfo(Base):
#     __tablename__ = "metainfo"  # noqa
#     __table_args__ = {"extend_existing": True}

#     id = Column(Integer, primary_key=True, index=True)
#     metainfo_json = Column("metainfo_json", JSON)
#     user_id = Column(String, ForeignKey("users.user_id"))
#     owner = relationship("User", backref="owner", overlaps="metainfo")

#     @validates("metainfo_json")
#     def metainfo_json_validator(self, key, value):
#         if value is None:
#             return None
#         return value


# def generate_uuid():
#     return str(uuid.uuid4())


# audio_tag = Table(
#     "audio_tag",
#     Base.metadata,
#     Column("audio_uuid", ForeignKey("audio.uuid")),
#     Column("tag_name", ForeignKey("tag.name")),
#     extend_existing=True,
# )


# class Audio(Base):
#     __tablename__ = "audio"  # noqa

#     uuid = Column(String, primary_key=True, default=generate_uuid)
#     user_id = Column(String, ForeignKey("users.user_id"))
#     owner_audio = relationship("User", backref="owner_audio", overlaps="owner, audio")
#     original_format = Column(String)
#     format = Column(
#         ENUM(
#             AudioFormat,
#             name="audio_format",
#             values_callable=lambda x: [str(e.value) for e in AudioFormat],
#         )
#     )
#     session_id = Column(String)
#     channel = Column(String)
#     time = Column(TIMESTAMP(timezone=True), default=func.now())
#     original = Column(Boolean)
#     file = Column(String, nullable=False)
#     operation = Column(
#         ENUM(
#             Operation,
#             name="operation",
#             values_callable=lambda x: [str(e.value) for e in Operation],
#         )
#     )
#     score = Column(Float)
#     biometric_model = Column(String, nullable=False)
#     biometric_settings = Column(JSONB, nullable=False)
#     biometric_decision = Column(
#         ENUM(
#             BiometricDecision,
#             name="biometric_decision",
#             values_callable=lambda x: [str(e.value) for e in BiometricDecision],
#         ),
#         nullable=True,
#     )
#     spoofing_settings = Column(JSONB, nullable=False)
#     spoofing_decision = Column(
#         ENUM(
#             SpoofingDecision,
#             name="spoofing_decision",
#             values_callable=lambda x: [str(e.value) for e in SpoofingDecision],
#         ),
#         nullable=True,
#     )
#     audio_info = Column(JSONB, nullable=True)
#     spf_cp1 = Column(Float, nullable=True)
#     spf_cp2 = Column(Float, nullable=True)

#     tags = relationship(
#         "Tag", secondary=audio_tag, back_populates="audios", lazy="joined"
#     )

#     @property
#     def tag_list(self) -> List[str]:
#         return [tag.name for tag in self.tags]


# class Tag(Base):
#     __tablename__ = "tag"  # noqa
#     name = Column(String, primary_key=True)
#     audios = relationship("Audio", secondary=audio_tag, back_populates="tags")
