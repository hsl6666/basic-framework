from pydantic import BaseModel


class HealthResponse(BaseModel):
    service: str
    status: str
    version: str


class DependencyHealthResponse(BaseModel):
    service: str
    postgres: bool
    redis: bool

