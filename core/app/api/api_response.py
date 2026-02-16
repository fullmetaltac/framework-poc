from assertpy import assert_that
from pydantic import BaseModel
from requests import Response


class ApiResponse:
    def __init__(self, response: Response):
        self.response: Response = response

    @property
    def status(self) -> int:
        return self.response.status_code

    @property
    def ok(self) -> bool:
        return 200 <= self.status < 300

    def json(self) -> dict:
        return self.response.json()

    def validate_status(self, expected: int = 200):
        assert_that(self.status, expected)
        return self

    def to_model(self, model_cls: BaseModel):
        return model_cls.model_validate(self.json())
