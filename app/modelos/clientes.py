from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .facturas import Factura


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
    facturas: list["Factura"] = Relationship(back_populates="cliente")