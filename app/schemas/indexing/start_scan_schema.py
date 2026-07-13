from pydantic import BaseModel


class StartScanRequest(BaseModel):
    user_id: str
    folder_path: str