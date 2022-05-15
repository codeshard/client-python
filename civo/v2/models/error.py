from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CivoError:
    code: Optional[str] = field(default=None)
    result: Optional[str] = field(default=None)
    reason: Optional[str] = field(default=None)
