from uuid import UUID

from pydantic import BaseModel, Field


class FileSchema(BaseModel):
    id: UUID = Field(...)
    name: str = Field(...)
    user: str = Field(...)


class FilesSchema(BaseModel):
    count: int = Field(...)
    files: list[FileSchema] = Field(...)
