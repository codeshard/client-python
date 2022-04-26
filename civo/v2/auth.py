from dataclasses import dataclass, field
from os import environ

from civo.v2.errors import CivoError
from dotenv import load_dotenv

load_dotenv()


@dataclass
class CivoAuth:
    civo_token: str = field(default=environ["CIVO_TOKEN"])

    def __post_init__(self):
        if not self.civo_token:
            raise CivoError(0, "CIVO_TOKEN not setted")
