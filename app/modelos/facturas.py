from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from pydantic import computed_field

from .clientes import Cliente, ClienteBase


class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    @computed_field
    @property
    def vr_total(self) -> float:
        return 0.0


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass




# modelo de respuesta que sí incluye los datos del cliente
class FacturaConCliente(FacturaBase):
    id: int
    cliente_id: int
    cliente: ClienteBase

class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id")
    cliente: Cliente | None = Relationship(back_populates="facturas")
    transacciones: list["Transaccion"] = Relationship(back_populates="factura")