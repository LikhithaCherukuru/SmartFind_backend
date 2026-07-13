import fitz

from app.ai.extractors.base_extractor import BaseExtractor


class PDFExtractor(BaseExtractor):

    def extract_text(self, file_path: str):

        document = fitz.open(file_path)

        text = ""

        for page in document:

            text += page.get_text()

        document.close()

        return text