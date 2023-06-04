from fastapi import APIRouter
from src.apps.test.exam1.api.crud import (
    CRUD_ROUTER,
    CRUD_ROUTER_PREFIX,
    CRUD_ROUTER_TAG,
)


EXAM_ROUTER = APIRouter(prefix='/exam')

EXAM_ROUTER.include_router(
    CRUD_ROUTER,
    prefix=CRUD_ROUTER_PREFIX,
    tags=CRUD_ROUTER_TAG,
)
