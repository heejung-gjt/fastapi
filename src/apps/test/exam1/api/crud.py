from fastapi import APIRouter


CRUD_ROUTER = APIRouter()
CRUD_ROUTER_PREFIX = "/crud"
CRUD_ROUTER_TAG = ["CRUD base router"]


@CRUD_ROUTER.get("/")
async def read():
    return {"Hello": "World"}
