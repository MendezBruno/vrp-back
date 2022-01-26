from fastapi import APIRouter

from src.api.ORSM.schemas.OrsmRequest import OrsmRequest
from src.api.ORSM.services.services import orsm_route_service
from src.core.schemas.Route import RouteResponse, RouteSchema, RouteRequest
from src.core.utils.utils import packages_to_coordinates, coordinates_to_packages

orsm_router = APIRouter()


@orsm_router.get("/trip", response_model=RouteResponse, status_code=201, response_description="Route by ORSM")
async def get_trip_by_orsm():
    return RouteResponse()


@orsm_router.get("/route/{coordinates}", response_model=RouteResponse, status_code=201,
                 response_description="Route by ORSM")
async def get_route_by_orsm(coordinates):
    the_coordinates = [coordinates]
    orsm_request = OrsmRequest(coordinates=the_coordinates)
    orsm_response = orsm_route_service(orsm_request)
    return RouteResponse(route=orsm_response.json(), code=orsm_response.status_code, message=orsm_response.reason)




@orsm_router.post("/route", response_model=RouteResponse, status_code=201,
                 response_description="Route by ORSM with packages")
async def get_route_by_orsm_with(route_request: RouteRequest):
    coordinates = packages_to_coordinates(route_request.packages)
    orsm_request = OrsmRequest(coordinates=coordinates)
    orsm_response = orsm_route_service(orsm_request)
    if orsm_response.json().code == "ok":
        coordinates_to_packages(route_request.packages, orsm_response.json().routes[0])
        route_schema = RouteSchema(paquerId=route_request.paquerId, geojson=orsm_response.json().routes[0].geometry, packages=)
        return RouteResponse(route=route_schema, code=orsm_response.status_code, message=orsm_response.reason)
    else:
        return RouteResponse(route=orsm_response.json(), code=orsm_response.status_code, message=orsm_response.reason)
