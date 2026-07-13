import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.ai.extractors.extractor_factory import ExtractorFactory

file_path = r"D:\pdfs\sem5\AE_UNIT_2.pdf"

extension = ".pdf"

extractor = ExtractorFactory.get_extractor(extension)

text = extractor.extract_text(file_path)

print(text[:2000])