from pydantic import BaseModel


class ScanFileRequest(BaseModel):
    user_id: str
    file_path: str