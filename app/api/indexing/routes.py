from fastapi import APIRouter

from app.schemas.indexing.start_scan_schema import StartScanRequest
from app.services.indexing.indexing_service import IndexingService

router = APIRouter(
    prefix="/api/v1/indexing",
    tags=["Indexing"]
)

service = IndexingService()


@router.post("/start")
def start_scan(request: StartScanRequest):

    return service.start_scan(
        request.user_id,
        request.folder_path
    )