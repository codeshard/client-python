from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import List, Union

from requests import Request, Session

from civo.v2.auth import CivoAuth
from civo.v2.models import SSH, CivoError, Instance, Key, Quota, Regions, Size, SSHResponse


@dataclass
class CivoSDK:
    api_token: str
    civo_region: str = None

    def __post_init__(self):
        self.base_url = "https://api.civo.com/v2/"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}
        self.request = Request(
            headers=self.headers,
        )
        self._http = Session()

    def __hash__(self):
        return hash((self.base_url, self.api_token))

    @staticmethod
    def from_auth(
        auth: CivoAuth,
        region: str = None,
    ) -> "CivoSDK":
        return CivoSDK(auth.api_token, region)

    def prepare_request(self, method: str, path: str, data: dict = None) -> dict:
        with self._http as session:
            self.request.method = method
            self.request.data = data
            self.request.url = f"{self.base_url}{path}"
            response = session.send(self.request.prepare())
            return response.json()

    def upload_ssh_key(
        self, name: str = "default", public_key: Path = Path.home() / ".ssh/id_rsa.pub"
    ) -> Union[SSHResponse, CivoError]:
        if public_key.stat().st_size == 0:
            return CivoError(reason="Public key is empty")
        response = self.prepare_request("POST", "sshkeys", data={"name": name, "public_key": public_key.read_text()})
        if "id" not in response:
            return CivoError(**response)
        return SSHResponse.from_json(response)

    def list_ssh_keys(self) -> List[SSH]:
        return SSH.from_json(self.prepare_request("GET", "sshkeys"))

    def retrieve_ssh_key(self, ssh_key_id: str) -> Union[Key, CivoError]:
        response = self.prepare_request("GET", f"sshkeys/{ssh_key_id}")
        if "name" not in response:
            return CivoError(**response)
        return Key.from_json(response)

    def update_ssh_key(self, name: str, ssh_key_id: str) -> Key:
        response = self.prepare_request("PUT", f"sshkeys/{ssh_key_id}", data={"name": name})
        if "name" not in response:
            return CivoError(**response)
        return Key.from_json(response)

    def remove_ssh_key(self, ssh_key_id: str) -> dict:
        return self.prepare_request("DELETE", f"sshkeys/{ssh_key_id}")

    def list_instance_sizes(self) -> List[Size]:
        return self.prepare_request("GET", "sizes")

    def create_instance(
        self,
        hostname: str,
        size: str,
        network_id: str,
        template_id: str,
        count: int = 1,
        firewall_id: str = None,
        reverse_dns: str = None,
        region: str = None,
        public_ip: str = "create",
        initial_user: str = None,
        ssh_key_id: str = None,
        script: Path = None,
        tags: List = None,
    ) -> Union[Instance, CivoError]:
        response = self.prepare_request(
            "POST",
            "instances",
            data={
                "hostname": hostname,
                "size": size,
                "network_id": network_id,
                "template_id": template_id,
                "count": count,
                "firewall_id": firewall_id,
                "reverse_dns": reverse_dns,
                "region": region,
                "public_ip": public_ip,
                "initial_user": initial_user,
                "ssh_key_id": ssh_key_id,
                "script": script,
                "tags": tags,
            },
        )
        if "id" not in response:
            return CivoError(**response)
        return Instance.from_json(response)

    @lru_cache()
    def get_regions(self) -> List[Regions]:
        return Regions.from_json(self.prepare_request("GET", "regions"))

    @lru_cache()
    def get_quota(self) -> Quota:
        return Quota.from_json(self.prepare_request("GET", "quota"))
