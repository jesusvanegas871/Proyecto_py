from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

from pydantic import BaseModel, computed_field

from app.modelos.transacciones import Transaccion
from .clientes import Cliente


# Crear el modelo facturas(id, fecha, cliente, transacciones)
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


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id")