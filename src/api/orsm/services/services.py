import requests

from src.api.orsm.schemas.OrsmRequest import OrsmRequest

base_url = "http://router.project-osrm.org/"


# route_service_url = "route/v1/{profile}/{coordinates}?alternatives={alternatives}&steps={steps}&geometries={geometries}&overview={overview}&annotations={annotations}".format(
#     profile=profile, coordinates=coordinates, alternatives=alternative, steps=step, geometries=geometry,
#     overview=overview, annotations=annotation)
#
# profile = "driving"
# sanjuan = "-58.27611923217773,-34.7228847459182"
# federal = "-58.332080841064446,-34.75175051870402"
# roel = "-58.31324100494384,-34.78101155893815"
# myTuple = (sanjuan, federal, roel)
# # coordinates = "13.388860,52.517037;13.397634,52.529407;13.428555,52.523219"
# coordinates = ";".join(myTuple)
# alternative = "2"  # {true|false|number}
# step = "false"  # {true | false }
# geometry = "geojson"  # {polyline|polyline6|geojson}
# overview = "false"  # {full|simplified|false}
# annotation = "false"  # {true|false}
#
# r = requests.get(base_url + route_service_url)
# print(r.json())


def orsm_route_service(orsm_request: OrsmRequest):
    algo = orsm_request
    coordinates = ";".join(algo.coordinates)
    route_service_url = "route/v1/{profile}/{coordinates}?alternatives={alternatives}&steps={steps}&geometries={geometries}&overview={overview}&annotations={annotations}".format(
        profile=algo.profile,
        coordinates=coordinates,
        alternatives=algo.alternatives,
        steps=algo.steps,
        geometries=algo.geometry,
        overview=algo.overview,
        annotations=algo.annotation)
    return requests.get(base_url + route_service_url)
