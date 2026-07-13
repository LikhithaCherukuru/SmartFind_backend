from fastapi import APIRouter, HTTPException

from app.schemas.files.register_file_schema import RegisterFileRequest
from app.schemas.files.register_folder_schema import RegisterFolderRequest

from app.services.files.file_service import FileService
from app.schemas.files.scan_folder_schema import ScanFolderRequest
from app.schemas.files.scan_file_schema import ScanFileRequest

router = APIRouter(
    prefix="/api/v1/files",
    tags=["Files"],
)

service = FileService()


# --------------------------------------------------
# Sync File Metadata
# --------------------------------------------------

@router.post("/sync")
def sync_file(request: RegisterFileRequest):

    try:

        result = service.register_file(
            request.model_dump(mode="json")
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# --------------------------------------------------
# Sync Folder Metadata
# --------------------------------------------------

@router.post("/folders/sync")
def sync_folder(request: RegisterFolderRequest):

    try:

        result = service.register_folder(
            request.model_dump(mode="json")
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# --------------------------------------------------
# Get All Files
# --------------------------------------------------

@router.get("/")
def get_files():

    return service.get_all_files()


# --------------------------------------------------
# Get All Folders
# --------------------------------------------------

@router.get("/folders")
def get_folders():

    return service.get_all_folders()


# --------------------------------------------------
# Delete File
# --------------------------------------------------

@router.delete("/{file_id}")
def delete_file(file_id: str):

    return service.delete_file(file_id)


# --------------------------------------------------
# Delete Folder
# --------------------------------------------------

@router.delete("/folders/{folder_id}")
def delete_folder(folder_id: str):

    return service.delete_folder(folder_id)

@router.post("/scan-folder")
def scan_folder(request: ScanFolderRequest):

    return service.scan_folder(

        request.user_id,

        request.folder_path

    )

@router.post("/scan-file")
def scan_file(request: ScanFileRequest):

    return service.scan_single_file(
        request.user_id,
        request.file_path
    )