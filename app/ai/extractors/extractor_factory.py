from app.ai.extractors.pdf_extractor import PDFExtractor
from app.ai.extractors.docx_extractor import DOCXExtractor
from app.ai.extractors.pptx_extractor import PPTXExtractor
from app.ai.extractors.txt_extractor import TXTExtractor
from app.ai.extractors.image_extractor import ImageExtractor


class ExtractorFactory:

    @staticmethod
    def get_extractor(extension: str):

        extension = extension.lower()

        mapping = {

            ".pdf": PDFExtractor(),

            ".docx": DOCXExtractor(),

            ".pptx": PPTXExtractor(),

            ".txt": TXTExtractor(),

            ".png": ImageExtractor(),

            ".jpg": ImageExtractor(),

            ".jpeg": ImageExtractor()

        }

        return mapping.get(extension)