from typing import List
from src.api.orsm.schemas.OrsmSchema import OrsmRoute, Waypoint
from src.core.schemas.Package import Package

decimal_coord_float = 2


def trunc(a, x):
    int1 = int(a * (10 ** x)) / (10 ** x)
    return float(int1)


def func_action(loc):
    return [trunc(loc[0], decimal_coord_float), trunc(loc[1], decimal_coord_float)]


def packages_to_coordinates(packages: List[Package]):
    coordinates = []
    for package in packages:
        coord = str(package.location[0]) + "," + str(package.location[1])
        coordinates.append(coord)
    return coordinates


def coordinates_to_packages(origin_packages: List[Package], param: OrsmRoute):
    result = []
    aux_result = []
    # coord [float, float]
    # Package.location [float, float]
    # requests_trunc = map(func_action, requests_origin)
    coord_geojson = list(map(func_action, param.geometry['coordinates']))
    for package in origin_packages:
        aux_coord = func_action(package.location)
        aux_result.append((package, coord_geojson.index(aux_coord)))
    aux_result = sorted(aux_result, key=lambda p: float(p[1]))
    for item, indice in aux_result:
        result.append(item)
    return result


def find_waypoint(package: Package, param: List[Waypoint]):
    package_coord = func_action(package.location)
    for waypoint in param:
        waypoint_coord = func_action(waypoint.location)
        if set(package_coord) == set(waypoint_coord):
            return waypoint


def waypoints_to_packages(origin_packages: List[Package], param: List[Waypoint]):
    result = []
    aux_result = []
    for package in origin_packages:
        waypoint = find_waypoint(package, param)
        aux_result.append((package, waypoint.waypoint_index))
    aux_result = sorted(aux_result, key=lambda p: float(p[1]))
    for item, indice in aux_result:
        result.append(item)
    return result
