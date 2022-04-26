from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CivoError(Exception):
    status_code: int
    status_message: Optional[str] = field(default=None)
