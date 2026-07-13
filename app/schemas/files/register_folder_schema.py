from pydantic import BaseModel


class RegisterFolderRequest(BaseModel):

    folder_name: str

    local_path: str

    parent_path: str | None = None

    drive_name: str