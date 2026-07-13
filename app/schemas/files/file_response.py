from pydantic import BaseModel


class FileResponse(BaseModel):

    success: bool

    message: str