from docx import Document

from app.ai.extractors.base_extractor import BaseExtractor


class DOCXExtractor(BaseExtractor):

    def extract_text(self, file_path: str):

        document = Document(file_path)

        return "\n".join(

            paragraph.text

            for paragraph in document.paragraphs

        )