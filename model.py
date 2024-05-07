from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)


    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example schema!"
            }
        }


# UPDATE 라우트의 요청 바디용 모델
class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
            "item": "Read the next chapter of the book."
            }
        }


class TodoItems(BaseModel):
    todo: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos" : [
                    {
                        "item" : "Example schema 1"
                    },
                    {
                        "item" : "Example schema 2"
                    },
                ]
            }
        }