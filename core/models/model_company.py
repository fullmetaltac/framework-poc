from pydantic import BaseModel, Field


class CompanyDC(BaseModel):
    name: str = Field()
    location: str = Field()
