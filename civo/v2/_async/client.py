from dataclasses import dataclass, field
from typing import List

from civo.v2.auth import CivoAuth
from civo.v2.http_clients import AsyncClient
from civo.v2.models import Regions
from civo.v2.utils import validate_response
from httpx._config import DEFAULT_TIMEOUT_CONFIG
from httpx._types import TimeoutTypes


@dataclass
class AsyncCivoClient:
    civo_token: str
    civo_region: str = None
    timeout: TimeoutTypes = field(default=DEFAULT_TIMEOUT_CONFIG)

    def __post_init__(self):
        self.base_url = "https://api.civo.com/v2/"
        self.headers = {"Authorization": f"Bearer {self.civo_token}"}
        self.http_client = AsyncClient(
            base_url=self.base_url,
            headers=self.headers,
            timeout=self.timeout,
        )

    async def __aenter__(self) -> "AsyncCivoClient":
        return self

    async def __aexit__(self, exc_t, exc_v, exc_tb) -> None:
        await self.close()

    async def close(self) -> None:
        await self.http_client.aclose()

    @staticmethod
    def from_auth(
        auth: CivoAuth,
        region: str = None,
        timeout: TimeoutTypes = DEFAULT_TIMEOUT_CONFIG,
    ) -> "AsyncCivoClient":
        return AsyncCivoClient(auth.civo_token, region, timeout)

    async def get_regions(self) -> List[Regions]:
        """
        Function to listing the regions
        :return: object json
        """
        r = await self.http_client.get("regions")
        validate_response(r)
        return Regions.from_json(r.json())
