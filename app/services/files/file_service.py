import os
import mimetypes

from fastapi.encoders import jsonable_encoder

from app.repositories.files.file_repository import FileRepository
from app.utils.hash_utils import generate_sha256
from app.utils.file_metadata import get_file_metadata


class FileService:

    def __init__(self):
        self.repository = FileRepository()

    # -----------------------------------------
    # Register File Metadata
    # -----------------------------------------
    def register_file(self, file_data: dict):

        # Convert datetime, UUID, etc. into JSON-compatible values
        file_data = jsonable_encoder(file_data)

        # Duplicate Check
        existing = self.repository.get_file_by_hash(
            file_data["file_hash"]
        )

        if existing:
            return {
                "success": False,
                "message": "Duplicate file already exists.",
                "data": existing
            }

        saved = self.repository.register_file(file_data)

        return {
            "success": True,
            "message": "File registered successfully.",
            "data": saved
        }

    # -----------------------------------------
    # Register Folder Metadata
    # -----------------------------------------
    def register_folder(self, folder_data: dict):

        folder_data = jsonable_encoder(folder_data)

        saved = self.repository.register_folder(folder_data)

        return {
            "success": True,
            "message": "Folder registered successfully.",
            "data": saved
        }

    # -----------------------------------------
    # Get All Files
    # -----------------------------------------
    def get_all_files(self):

        files = self.repository.get_all_files()

        return {
            "success": True,
            "count": len(files),
            "data": files
        }

    # -----------------------------------------
    # Get All Folders
    # -----------------------------------------
    def get_all_folders(self):

        folders = self.repository.get_all_folders()

        return {
            "success": True,
            "count": len(folders),
            "data": folders
        }

    # -----------------------------------------
    # Delete File
    # -----------------------------------------
    def delete_file(self, file_id: str):

        self.repository.delete_file(file_id)

        return {
            "success": True,
            "message": "File deleted successfully."
        }

    # -----------------------------------------
    # Delete Folder
    # -----------------------------------------
    def delete_folder(self, folder_id: str):

        self.repository.delete_folder(folder_id)

        return {
            "success": True,
            "message": "Folder deleted successfully."
        }

        # -----------------------------------------
    # Scan Single File
    # -----------------------------------------
    def scan_single_file(self, user_id: str, file_path: str):

        if not os.path.exists(file_path):
            return {
                "success": False,
                "message": "File does not exist."
            }

        if not os.path.isfile(file_path):
            return {
                "success": False,
                "message": "Invalid file."
            }

        metadata = get_file_metadata(file_path)

        file_hash = generate_sha256(file_path)

        existing = self.repository.get_file_by_hash(file_hash)

        if existing:
            return {
                "success": False,
                "message": "Duplicate file already exists.",
                "data": existing
            }

        mime_type = mimetypes.guess_type(file_path)[0]

        data = {

            "user_id": user_id,

            "folder_id": None,

            "file_name": metadata["file_name"],

            "original_name": metadata["file_name"],

            "extension": metadata["extension"],

            "mime_type": mime_type,

            "file_size": metadata["file_size"],

            "storage_path": None,

            "local_path": metadata["local_path"],

            "file_hash": file_hash,

            "thumbnail_path": None,

            "created_by": "Desktop Scan",

            "created_date": metadata["created_date"],

            "modified_date": metadata["modified_date"],

            "last_accessed": metadata["last_accessed"],

            "upload_source": "local",

            "is_uploaded": False

        }

        return self.register_file(data)

    # -----------------------------------------
    # Scan Folder
    # -----------------------------------------
    def scan_folder(self, user_id: str, folder_path: str):

        # Path exists?
        if not os.path.exists(folder_path):
            return {
                "success": False,
                "message": "Path does not exist."
            }

        # Single file selected
        if os.path.isfile(folder_path):
            return self.scan_single_file(user_id, folder_path)

        # Must be directory
        if not os.path.isdir(folder_path):
            return {
                "success": False,
                "message": "Invalid directory."
            }

        supported_extensions = {
            ".pdf",
            ".docx",
            ".pptx",
            ".txt",
            ".png",
            ".jpg",
            ".jpeg"
        }

        files_found = 0
        new_files = 0
        duplicates = 0
        failed = 0

        for root, dirs, files in os.walk(folder_path):

            for file in files:

                extension = os.path.splitext(file)[1].lower()

                if extension not in supported_extensions:
                    continue

                files_found += 1

                try:

                    full_path = os.path.join(root, file)

                    result = self.scan_single_file(
                        user_id=user_id,
                        file_path=full_path
                    )

                    if result["success"]:
                        new_files += 1
                    else:
                        duplicates += 1

                except Exception as e:

                    print(e)

                    failed += 1

        return {

            "success": True,

            "message": "Folder scanned successfully.",

            "summary": {

                "folders_scanned": 1,

                "files_found": files_found,

                "new_files": new_files,

                "duplicates": duplicates,

                "failed": failed

            }

        }