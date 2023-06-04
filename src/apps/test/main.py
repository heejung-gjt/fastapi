from fastapi import FastAPI
from src.packages.db.connect import init_pool
from fastapi.middleware.cors import CORSMiddleware
from src.apps.test.exception import (
    AppErrorHandler,
    JSendError,
    ExceptionError,
)
from src.apps.test.exam1.urls import EXAM_ROUTER

DOCS = """fastapi base 개발 환경입니다"""


app = FastAPI(
    title="FastAPI",
    version="1.0.0",
    description=DOCS,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(EXAM_ROUTER)

app.add_exception_handler(
    JSendError,
    AppErrorHandler.app_error_exc_handler,
)

app.add_exception_handler(
    ExceptionError,
    AppErrorHandler.exc_handler
)


# @app.on_event("startup")
# async def startup():
#     await init_pool()
