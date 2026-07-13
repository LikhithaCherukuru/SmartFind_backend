from app.ai.extractors.base_extractor import BaseExtractor


class TXTExtractor(BaseExtractor):

    def extract_text(self, file_path: str):

        with open(

            file_path,

            "r",

            encoding="utf-8",

            errors="ignore"

        ) as file:

            return file.read()