from app.services.files.file_service import FileService
from app.repositories.indexing.indexing_repository import IndexingRepository


class IndexingService:

    def __init__(self):
        self.file_service = FileService()
        self.repository = IndexingRepository()

    def start_scan(self, user_id: str, folder_path: str):
        return self.file_service.scan_folder(
            user_id=user_id,
            folder_path=folder_path
        )