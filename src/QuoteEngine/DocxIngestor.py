import docx
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Gets Quotes from a Docx File"""
    supported_extension = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest extension')

        doc = docx.Document(path)

        quotes = list()
        for para in doc.paragraphs:
            if para.text != "":
                body, author = para.text.split('-')
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
