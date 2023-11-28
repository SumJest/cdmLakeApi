import asyncio
import json
import time
from io import TextIOWrapper, IOBase, BytesIO

import aiohttp
from aiohttp import ClientSession, ClientTimeout

from lakeApi.exception import RequestError


class ApiClient:
    __session: ClientSession
    __base_url: str
    __timeout: ClientTimeout
    __is_closed: bool

    def __init__(self, base_url: str, timeout: float = 10):
        self.__base_url = base_url
        self.__timeout = aiohttp.ClientTimeout(total=timeout)
        self.__session = None

    async def __get_session(self) -> ClientSession:
        if not self.__session:
            self.__session = ClientSession(base_url=self.__base_url, connector=aiohttp.TCPConnector(ssl=False),
                                           timeout=self.__timeout)
        self.__is_closed = False
        return self.__session

    async def __make_request(self, method_name: str, url: str, data: object = None, headers: dict = {}):
        async with ((await self.__get_session()).request(method=method_name, url=url, data=data, headers=headers) as
                    response):
            if not response.ok:
                print(response)
                raise RequestError("Server returns non successful response")
            return await response.read()

    async def request(self, method_name: str, url: str, data: object = None, headers: dict = {}):
        return await self.__make_request(method_name, url, data, headers)

    async def download(self, url: str, data: object = {}, headers: dict = {}):
        return await self.__make_request(method_name="GET", url=url, data=data, headers=headers)

    async def upload(self, url: str, fileio: BytesIO, headers: dict = {}):
        return await self.__make_request(method_name="POST", url=url, data={"file": fileio}, headers=headers)

    async def json_request(self, method_name: str, url: str, data: object = None):
        response = await self.__make_request(method_name, url, data)
        return json.loads(response)

    async def close(self):
        session = await self.__get_session()
        await session.close()
