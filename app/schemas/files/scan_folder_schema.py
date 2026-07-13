from pydantic import BaseModel


class ScanFolderRequest(BaseModel):
    user_id: str
    folder_path: str