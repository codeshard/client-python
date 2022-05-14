from dataclasses import dataclass
from functools import lru_cache
from typing import List

from requests import Request, Session

from civo.v2.auth import CivoAuth
from civo.v2.models import Quota, Regions
from civo.v2.models.ssh import SSH, Key


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

    def prepare_request(self, method: str, path: str) -> dict:
        with self._http as session:
            self.request.method = method
            self.request.url = f"{self.base_url}{path}"
            response = session.send(self.request.prepare())
            response.raise_for_status()
            return response.json()

    def upload_ssh_key(self, ssh_key: str) -> None:
        pass

    def list_ssh_keys(self) -> List[SSH]:
        return SSH.from_json(self.prepare_request("GET", "sshkeys"))

    def retrieve_ssh_key(self, ssh_key_id: str) -> Key:
        try:
            return Key.from_json(self.prepare_request("GET", f"sshkeys/{ssh_key_id}"))
        except Exception as e:
            return {"status_code": 404, "text": str(e)}

    def update_ssh_key(self, ssh_key_id: str) -> Key:
        pass

    def delete_ssh_key(self, ssh_key_id: str) -> dict:
        pass

    @lru_cache()
    def get_regions(self) -> List[Regions]:
        return Regions.from_json(self.prepare_request("GET", "regions"))

    @lru_cache()
    def get_quota(self) -> Quota:
        return Quota.from_json(self.prepare_request("GET", "quota"))
