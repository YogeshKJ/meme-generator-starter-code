import os
import subprocess
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Gets Quotes from a PDF File"""
    supported_extension = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest extension')

        temp_path = './_data/DogQuotes/dog.txt'
        subprocess.run(['pdftotext', '-layout', path, temp_path])

        quotes = list()
        with open(temp_path) as f:
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line):
                    body, author = line.split('-')
                    new_quote = QuoteModel(body, author)
                    quotes.append(new_quote)

        if temp_path:
            os.remove(temp_path)

        return quotes
