import hashlib


def generate_sha256(file_path: str) -> str:
    """
    Generate SHA256 hash of a file.
    """

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:

            data = file.read(65536)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()