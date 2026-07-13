from pydantic import BaseModel


class ScanStatusResponse(BaseModel):
    scan_id: str
    status: str
    files_found: int
    new_files: int
    duplicates: int
    failed: int