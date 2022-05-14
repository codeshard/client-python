from dataclasses import dataclass, field
from os import environ

from civo.v2.errors import CivoError
from dotenv import load_dotenv

load_dotenv()


@dataclass
class CivoAuth:
    api_token: str = field(default=environ["API_TOKEN"])

    def __post_init__(self):
        if not self.api_token:
            raise CivoError(0, "API_TOKEN not setted")
