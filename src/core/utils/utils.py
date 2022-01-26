from typing import List

from src.api.ORSM.schemas.Orsm import Route
from src.core.schemas.Package import Package


def packages_to_coordinates(packages: List[Package]):
    coordinates = []
    for package in packages:
        coord = str(package.location[0] + "," + str(package.location[1]))
        coordinates.append(coord)
    return coordinates

def coordinates_to_packages(origin_packages: List[Package], param: Route):
    result = [ ]
    # coor [float, float]
    # Package.location [float, float]
    for package in origin_packages:
        result.append((package, param.geometry.coordinates.index(package.location)))
    result.sort()
    #return result.