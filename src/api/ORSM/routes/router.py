from fastapi import APIRouter

from src.api.ORSM.services.services import orsm_route_service
from src.core.schemas.Route import RouteResponse

orsm_router = APIRouter()


@orsm_router.get("/trip", response_model=RouteResponse, status_code=201, response_description="Route by ORSM")
async def get_trip_by_orsm():
    return RouteResponse()

@orsm_router.get("/route/{coordinates}", response_model=RouteResponse, status_code=201, response_description="Route by ORSM")
async def get_route_by_orsm(coordinates):
    return orsm_route_service(coordinates)