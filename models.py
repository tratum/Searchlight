import uuid
from typing import Optional

from pydantic import BaseModel, Field


class SearchlightAPIModel(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
    keyword: str = Field(...)
    pdf: bytes


    class Config:
        orm_mode = True
