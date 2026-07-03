from fastapi import APIRouter, HTTPException, status
from ..modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from ..modelos.facturas import Factura
from ..listas import lista_facturas, lista_transacciones

rutas_transacciones = APIRouter()

# lista_facturas: list[Factura] = []
# lista_transacciones: list[Transaccion] = []


@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones():
    return lista_transacciones


@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transaccion(id_transaccion: int):
    # recorrer la lista_transacciones
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:
            return obj_transaccion

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La transaccion con id {id_transaccion}, no existe."
    )


@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transaccion(factura_id: int, datos_transaccion: TransaccionCrear):

    # validar que exista la factura
    for obj_factura in lista_facturas:
        if obj_factura.id == factura_id:

            transaccion_val = Transaccion.model_validate(
                datos_transaccion.model_dump()
            )

            # generar id
            id_transaccion = len(lista_transacciones) + 1
            transaccion_val.id = id_transaccion

            # asociar factura
            transaccion_val.factura_id = factura_id

            lista_transacciones.append(transaccion_val)

            # agregar a la factura
            obj_factura.transacciones.append(transaccion_val)

            return transaccion_val

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factura con id {factura_id}, no existe."
    )


@rutas_transacciones.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(
    id_transaccion: int,
    datos_transaccion: TransaccionEditar
):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:

            transaccion_val = Transaccion.model_validate(
                datos_transaccion.model_dump()
            )

            transaccion_val.id = id_transaccion
            transaccion_val.factura_id = obj_transaccion.factura_id

            lista_transacciones[i] = transaccion_val

            # actualizar también dentro de la factura
            for factura in lista_facturas:
                if factura.id == transaccion_val.factura_id:
                    for j, transaccion in enumerate(factura.transacciones):
                        if transaccion.id == id_transaccion:
                            factura.transacciones[j] = transaccion_val
                            break

            return transaccion_val

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La transaccion con id {id_transaccion}, no existe."
    )


@rutas_transacciones.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    for i, obj_transaccion in enumerate(lista_transacciones):
        if obj_transaccion.id == id_transaccion:

            transaccion_eliminada = lista_transacciones.pop(i)

            # eliminar de la factura
            for factura in lista_facturas:
                if factura.id == transaccion_eliminada.factura_id:
                    factura.transacciones = [
                        t for t in factura.transacciones
                        if t.id != id_transaccion
                    ]
                    break

            return transaccion_eliminada

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La transaccion con id {id_transaccion}, no existe."
    )