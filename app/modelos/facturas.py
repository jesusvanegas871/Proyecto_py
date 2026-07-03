from datetime import datetime
from sqlmodel import SQLModel, Field, relationship

from pydantic import BaseModel, computed_field

from app.modelos.transacciones import Transaccion
from .clientes import Cliente


# Crear el modelo facturas(id, fecha, cliente, transacciones)
class FacturaBase(SQLModel):
    fecha: str = Field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    cliente: Cliente
    transacciones: list[Transaccion] = []

    @computed_field
    @property
    def vr_total(self) -> float:
        factura_id_actual = getattr(self, "id", None)
        total_factura = 0.0

        if not factura_id_actual or not self.transacciones:
            return total_factura

        for transaccion in self.transacciones:
            if transaccion.factura_id == factura_id_actual:
                total_factura += (
                    transaccion.vr_unitario
                    * transaccion.cantidad
                )

        return 0.0


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase):
    id: int | None = None