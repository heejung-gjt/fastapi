from typing import Final, Optional
import os

def getenv(key: str) -> str:
    v: Optional[str] = os.getenv(key)
    assert v is not None, f"Settings {key} is not found"
    return v


STAGE: Final[str] = getenv("ENVIRONMENT")
