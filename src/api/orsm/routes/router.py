from fastapi import APIRouter

from src.api.orsm.schemas.OrsmSchema import OrsmRoute
from src.api.orsm.schemas.OrsmRequest import OrsmRequest, OrsmTripRequest
from src.api.orsm.services.services import orsm_route_service, orsm_trip_service
from src.core.schemas.Route import RouteResponse, RouteSchema, RouteRequest
from src.core.helpers.utils import packages_to_coordinates, coordinates_to_packages

orsm_router = APIRouter()


@orsm_router.post("/trip", response_model=RouteResponse, status_code=201, response_description="Route by orsm")
async def get_trip_by_orsm(route_request: RouteRequest):
    coordinates = packages_to_coordinates(route_request.packages)
    orsm_trip_request = OrsmTripRequest(coordinates=coordinates)
    orsm_response = orsm_trip_service(orsm_trip_request)
    # if orsm_response.json()['code'] == "Ok":
    #     packages = coordinates_to_packages(route_request.packages, OrsmRoute.parse_obj(orsm_response.json()['routes'][0]))
    #     route_schema = RouteSchema(paquerId=route_request.paquerId, geojson=orsm_response.json()['routes'][0]['geometry'], packages=packages)
    #     return RouteResponse(route=route_schema, code=orsm_response.status_code, message=orsm_response.reason)
    # else:
    #     return RouteResponse(route=orsm_response.json(), code=orsm_response.status_code, message=orsm_response.reason)


@orsm_router.get("/route/{coordinates}", response_model=RouteResponse, status_code=201,
                 response_description="Route by orsm")
async def get_route_by_orsm(coordinates):
    the_coordinates = [coordinates]
    orsm_request = OrsmRequest(coordinates=the_coordinates)
    orsm_response = orsm_route_service(orsm_request)
    return RouteResponse(route=orsm_response.json(), code=orsm_response.status_code, message=orsm_response.reason)


@orsm_router.post("/route", response_model=RouteResponse, status_code=201,
                 response_description="Route by orsm with packages")
async def get_route_by_orsm_with(route_request: RouteRequest):
    coordinates = packages_to_coordinates(route_request.packages)
    orsm_request = OrsmRequest(coordinates=coordinates)
    orsm_response = orsm_route_service(orsm_request)
    if orsm_response.json()['code'] == "Ok":
        packages = coordinates_to_packages(route_request.packages, OrsmRoute.parse_obj(orsm_response.json()['routes'][0]))
        route_schema = RouteSchema(paquerId=route_request.paquerId, geojson=orsm_response.json()['routes'][0]['geometry'], packages=packages)
        return RouteResponse(route=route_schema, code=orsm_response.status_code, message=orsm_response.reason)
    else:
        return RouteResponse(route=orsm_response.json(), code=orsm_response.status_code, message=orsm_response.reason)
