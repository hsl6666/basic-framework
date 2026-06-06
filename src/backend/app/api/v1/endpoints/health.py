from fastapi import APIRouter, Depends

from app.api.deps import get_settings
from app.core.config import Settings
from app.db.postgres import PostgresClient
from app.db.redis import RedisClient
from app.schemas.health import DependencyHealthResponse, HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health(settings: Settings = Depends(get_settings)) -> HealthResponse:
    return HealthResponse(
        service=settings.app_name,
        status="ok",
        version=settings.app_version,
    )


@router.get("/health/dependencies", response_model=DependencyHealthResponse)
def dependency_health(
    settings: Settings = Depends(get_settings),
) -> DependencyHealthResponse:
    postgres_ok = PostgresClient(settings.database_url).ping()
    redis_ok = RedisClient(settings.redis_url).ping()
    return DependencyHealthResponse(
        service=settings.app_name,
        postgres=postgres_ok,
        redis=redis_ok,
    )

