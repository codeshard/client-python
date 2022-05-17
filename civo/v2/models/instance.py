from dataclasses import dataclass
from typing import Any, List
from uuid import UUID

from civo.v2.utils import parse_json


@dataclass
class Size:
    name: str
    nice_name: str
    cpu_cores: int
    ram_mb: int
    disk_gb: int
    description: str
    selectable: bool

    @classmethod
    def from_json(cls, json: Any) -> "Size":
        return parse_json(cls, **json)


@dataclass
class Instance:
    id: UUID
    name: str
    hostname: str
    account_id: UUID
    size: str
    firewall_id: UUID
    source_type: str
    source_id: str
    network_id: UUID
    initial_user: str
    initial_password: str
    ssh_key: str
    ssh_key_id: UUID
    tags: List[str]
    user_script: str
    status: str
    civostatsd_token: UUID
    public_ip: str
    private_ip: str
    ipv6: str
    namespace_id: str
    notes: str
    reverse_dns: str
    cpu_cores: int
    ram_mb: int
    disk_gb: int

    def __post_init__(self):
        self.id = UUID(str(self.id))
        self.account_id = UUID(str(self.account_id))
        self.firewall_id = UUID(str(self.firewall_id))
        self.network_id = UUID(str(self.network_id))
        self.ssh_key_id = UUID(str(self.ssh_key_id))
        self.civostatsd_token = UUID(str(self.civostatsd_token))

    @classmethod
    def from_json(cls, json: Any) -> "Instance":
        return parse_json(cls, **json)
