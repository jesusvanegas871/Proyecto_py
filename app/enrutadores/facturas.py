from fastapi import APIRouter, HTTPException, status
from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar
from ..modelos.clientes import Cliente
from ..listas import lista_clientes, lista_facturas

rutas_facturas = APIRouter()

# lista_clientes: list[Cliente] = []  # vacia
# lista_facturas: list[Factura] = []


@rutas_facturas.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return lista_facturas


@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_factura(factura_id: int):
    # recorrer la lista_facturas
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factura con id {factura_id}, no existe."
    )


@rutas_facturas.post("/facturas", response_model=Factura)
async def crear_factura(datos_factura: FacturaCrear):
    factura_val = Factura.model_validate(datos_factura.model_dump())

    # generar id
    id_factura = len(lista_facturas) + 1
    factura_val.id = id_factura

    lista_facturas.append(factura_val)

    return factura_val


@rutas_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_factura(factura_id: int, datos_factura: FacturaEditar):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            # validar factura
            factura_val = Factura.model_validate(datos_factura.model_dump())
            factura_val.id = factura_id

            lista_facturas[i] = factura_val
            return factura_val

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factura con id {factura_id}, no existe."
    )


@rutas_facturas.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_factura(factura_id: int):
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            factura_eliminada = lista_facturas.pop(i)
            return factura_eliminada

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"La factura con id {factura_id}, no existe."
    )