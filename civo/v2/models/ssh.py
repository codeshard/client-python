from dataclasses import dataclass
from typing import Any, List
from uuid import UUID

from civo.v2.utils import parse_json


@dataclass
class Key:
    id: UUID
    name: str
    fingerprint: str

    def __post_init__(self):
        self.id = UUID(str(self.id))
        self.name = str(self.name)
        self.fingerprint = str(self.fingerprint)

    @classmethod
    def from_json(cls, json: Any) -> "Key":
        return parse_json(cls, **json)


@dataclass
class SSH:
    keys: List[Key]

    @classmethod
    def from_json(cls, json: Any) -> "SSH":
        keys: List[SSH] = []
        for item in json:
            keys.append(SSH.from_json(item))
        del json
        return parse_json(cls, keys=keys)


@dataclass
class SSHResponse:
    id: UUID
    result: str

    def __post_init__(self):
        self.id = UUID(str(self.id))
        self.result = str(self.name)

    @classmethod
    def from_json(cls, json: Any) -> "SSHResponse":
        return parse_json(cls, **json)
