import typing as tp
import dataclasses
import os
import json
import pathlib
import typing as tp
from collections import defaultdict

BASE_FILES_LOC: str = os.path.join(
    pathlib.Path(__file__).parent.parent.parent, "resources"
)





@dataclasses.dataclass
class City:
    city_in_english: str
    city_in_russian: str
    population: float
    radius_km: float
    lat: float
    lon: float





def read_cities() -> tp.List[City]:
    with open(os.path.join(BASE_FILES_LOC, "russian-cities.json")) as json_f:
        data = json.load(json_f)
        results = []
        columns = list(data.keys())
        entries = [key for key in data[columns[0]]]

        for key in entries:

            dct = {}
            for column in columns:
                dct[column] = data[column][key]

            results.append(City(**dct))
    return results

