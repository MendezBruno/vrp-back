from fastapi import APIRouter

from src.core.schemas.Route import RouteResponse

orsm_router = APIRouter()


@orsm_router.get("/calculate", response_model=RouteResponse, status_code=201, response_description="Route by ORSM")
async def get_route_by_orsm():
    pass
