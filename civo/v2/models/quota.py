from dataclasses import dataclass
from datetime import datetime
from typing import Any
from uuid import UUID

from civo.v2.utils import parse_json
from dateutil.parser import parse


@dataclass
class Quota:
    id: UUID
    instance_count_limit: int
    instance_count_usage: int
    cpu_core_limit: int
    cpu_core_usage: int
    ram_mb_limit: int
    ram_mb_usage: int
    disk_gb_limit: int
    disk_gb_usage: int
    disk_volume_count_limit: int
    disk_volume_count_usage: int
    disk_snapshot_count_limit: int
    disk_snapshot_count_usage: int
    public_ip_address_limit: int
    public_ip_address_usage: int
    subnet_count_limit: int
    subnet_count_usage: int
    network_count_limit: int
    network_count_usage: int
    security_group_limit: int
    security_group_usage: int
    security_group_rule_limit: int
    security_group_rule_usage: int
    port_count_limit: int
    port_count_usage: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    default_user_id: UUID
    account_id: UUID
    clusters_lifetime_count: int
    instances_lifetime_count: int
    clusters_current_count: int
    disks_lifetime_count: int
    loadbalancer_count_limit: int
    loadbalancer_count_usage: int
    loadbalancers_lifetime_count: int

    def __post_init__(self):
        self.id = UUID(str(self.id))
        if self.default_user_id:
            self.default_user_id = UUID(str(self.default_user_id))
        self.account_id = UUID(str(self.account_id))
        self.created_at = parse(str(self.created_at))
        self.updated_at = parse(str(self.updated_at))
        if self.deleted_at:
            self.deleted_at = parse(str(self.deleted_at))

    @classmethod
    def from_json(cls, json: Any) -> "Quota":
        return parse_json(cls, **json)
