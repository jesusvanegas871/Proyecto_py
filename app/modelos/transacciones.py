from pydantic import BaseModel

class TransaccionBase(BaseModel):
    cantidad: int
    vr_unitario: float
    factura_id: int

class TransaccionCrear(TransaccionBase):
    pass

class TransaccionEditar(TransaccionBase):
    pass    

class TransaccionEditar(TransaccionBase):
    pass

class Transaccion(TransaccionBase):
    id: int
    factura_id: int