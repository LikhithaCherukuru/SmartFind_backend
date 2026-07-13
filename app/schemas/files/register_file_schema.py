from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RegisterFileRequest(BaseModel):
    user_id: str

    folder_id: Optional[str] = None

    file_name: str

    original_name: Optional[str] = None

    extension: str

    mime_type: str

    file_size: int

    local_path: str

    storage_path: Optional[str] = None

    file_hash: str

    thumbnail_path: Optional[str] = None

    created_by: Optional[str] = None

    created_date: datetime

    modified_date: datetime

    last_accessed: Optional[datetime] = None

    upload_source: str = "local"

    is_uploaded: bool = False