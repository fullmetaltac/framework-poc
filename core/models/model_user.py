from pydantic import BaseModel, Field


class UserDC(BaseModel):
    name: str = Field()
    email: str = Field()
