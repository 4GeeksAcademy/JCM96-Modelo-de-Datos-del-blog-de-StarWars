from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(80), nullable=False)
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    lastname: Mapped[str] = mapped_column(String(60), nullable=False)
    favoritos: Mapped[list['Favoritos']] = relationship(back_populates='user')

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "lastname": self.lastname,
            "favorito": self.favoritos
        }


class Favoritos(db.Model):
    __tablename__ = 'favoritos'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    planeta_id: Mapped[int] = mapped_column(ForeignKey('planeta.id'), nullable=True)
    personaje_id: Mapped[int] = mapped_column(ForeignKey('personaje.id'), nullable=True)

    user: Mapped['User'] = relationship(back_populates='favoritos')
    planeta: Mapped['Planeta'] = relationship(back_populates='favoritos')
    personaje: Mapped['Personaje'] = relationship(back_populates='favoritos')


class Planeta(db.Model):
    __tablename__ = 'planeta'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    population: Mapped[int] = mapped_column(Integer)
    habitable: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favoritos: Mapped[list['Favoritos']] = relationship(back_populates='planeta')


class Personaje(db.Model):
    __tablename__ = 'personaje'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    lastname: Mapped[str] = mapped_column(String(60), nullable=True)
    side: Mapped[str] = mapped_column(String(40))
    favoritos: Mapped[list['Favoritos']] = relationship(back_populates='personaje')
