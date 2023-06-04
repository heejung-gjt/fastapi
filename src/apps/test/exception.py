import traceback
from fastapi.responses import JSONResponse
from enum import Enum


class ErrorCode:
    class Common(Enum):
        SUCCESS = ("000000", " ", "특정 처리에 대한 성공")
        DEFAULT_ERROR = (
            "000001",
            "일시적인 오류입니다.\n잠시 후 다시 시도해주세요.\n같은 현상이 반복되면 관리자에게 문의해주세요",
            "특정 처리에 대한 실패 (기본 에러)",
        )



class AppErrorHandler(object):
    """FastAPI 에러 핸들러 정의"""

    @staticmethod
    async def app_error_exc_handler(request, exc):
        return JSONResponse(
            status_code=400,
            content={
                "status": exc.status,
                "code": exc.code,
                "message": exc.message,
            }
            )

    @staticmethod
    async def exc_handler(request, exc):
        return JSONResponse(
            status_code=500,
            content={
            "status": "error",
            "code": ErrorCode.Common.DEFAULT_ERROR.value[0],
            "message": exc.message,
        },
        )


class JSendError(Exception):
    status: str = "error"
    code: str
    message: str

    def __init__(
        self,
        code: str,
        message: str,
    ) -> None:
        self.code: str = code
        self.message: str = message


class ExceptionError(Exception):
    message: str | None
    err_type: str | None

    def __init__(
        self,
        message: str = '',
        err_type: str = '',
    ):
        self.message = message
        self.err_type = err_type
