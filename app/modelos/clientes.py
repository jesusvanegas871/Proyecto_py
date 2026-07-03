from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship


# Crear el modelo clientes(id, nombre, email, descripcion)
class ClienteBase(SQLModel):
    nombre: str = Field(default=None, max_length=100)
    email: str = Field(default=None, max_length=100)
    descripcion: str = Field(default=None, max_length=200)


class ClienteCrear(ClienteBase):
    pass


class ClienteEditar(ClienteBase):
    pass


class Cliente(ClienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)