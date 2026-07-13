import os
from datetime import datetime


def get_file_metadata(file_path: str):

    stat = os.stat(file_path)

    return {
        "file_name": os.path.basename(file_path),
        "extension": os.path.splitext(file_path)[1],
        "file_size": stat.st_size,
        "created_date": datetime.fromtimestamp(stat.st_ctime),
        "modified_date": datetime.fromtimestamp(stat.st_mtime),
        "last_accessed": datetime.fromtimestamp(stat.st_atime),
        "local_path": file_path
    }