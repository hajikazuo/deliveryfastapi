from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def orders():
    """
    Rota de pedidos
    """
    return {"message": "List of orders"}