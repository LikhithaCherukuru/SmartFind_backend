from fastapi import FastAPI

from app.core.config import settings
from app.core.database import supabase

from app.api.auth.routes import router as auth_router

from app.api.users.routes import (
    router as user_router
)

from app.api.files.routes import router as file_router

from app.api.indexing.routes import router as indexing_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(file_router)
app.include_router(indexing_router)

@app.get("/")
def home():
    return {
        "message": "Smart File Finder Backend Running",
        "version": settings.APP_VERSION,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.get("/test-db")
def test_db():
    response = (
        supabase
        .table("profiles")
        .select("*")
        .limit(1)
        .execute()
    )

    return response.data