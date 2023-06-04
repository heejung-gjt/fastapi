from fastapi import FastAPI
from src.packages.db.connect import init_pool
from fastapi.middleware.cors import CORSMiddleware


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


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.on_event("startup")
async def startup():
    await init_pool()