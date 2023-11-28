import uuid
from io import BytesIO
from uuid import UUID

from lakeApi.client import ApiClient
from lakeApi.methods import ApiMethod
from lakeApi.schemas import FilesSchema


class LakeApi:
    __api_url: str
    __client: ApiClient

    def __init__(self, url):
        self.api_url = url
        self.__client = ApiClient(self.api_url)

    async def get_files(self) -> FilesSchema:
        data = await self.__client.json_request("GET", ApiMethod.get_files.value)
        return FilesSchema(**data)

    async def get_file(self, id: UUID) -> bytes:
        data = await self.__client.download(ApiMethod.get_file.value.format(id=id.hex))
        return data

    async def get_files_by_user(self, user: str) -> FilesSchema:
        data = await self.__client.json_request("GET",
                                                ApiMethod.get_files_by_user.value.format(user_name=user))
        return FilesSchema(**data)

    async def find_files_by_name(self, file_name: str) -> FilesSchema:
        data = await self.__client.json_request("GET",
                                                ApiMethod.find_files.value.format(file_name=file_name))
        return FilesSchema(**data)

    async def upload_file(self, name: str, user: str, file: BytesIO) -> UUID:
        id = uuid.uuid4()
        await self.__client.upload(ApiMethod.upload_file.value.format(id=id.hex, file_name=name, user_name=user), file)
        return id

    async def delete_file(self, id: UUID):
        return await self.__client.request("DELETE", ApiMethod.delete_file.value.format(id=id.hex))

    async def close(self):
        await self.__client.close()
