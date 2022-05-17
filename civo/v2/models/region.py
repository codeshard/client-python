from dataclasses import dataclass
from typing import Any, List

from civo.v2.utils import parse_json


@dataclass
class RegionFeatures:
    iaas: bool
    kubernetes: bool

    @classmethod
    def from_json(cls, json: Any) -> "RegionFeatures":
        return parse_json(cls, **json)


@dataclass
class Region:
    code: str
    name: str
    type: str
    default: bool
    out_of_capacity: bool
    country: str
    country_name: str
    features: RegionFeatures

    @classmethod
    def from_json(cls, json: Any) -> "Region":
        return parse_json(cls, **json)


@dataclass
class Regions:
    regions: List[Region]

    @classmethod
    def from_json(cls, json: Any) -> "Regions":
        regions: List[Region] = []
        for item in json:
            regions.append(Region.from_json(item))
        del json
        return parse_json(cls, regions=regions)
