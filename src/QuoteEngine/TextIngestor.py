from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Gets Quotes from a txt File"""
    supported_extension = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest extension')

        quotes = list()
        with open(path, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line):
                    body, author = line.split('-')
                    new_quote = QuoteModel(body, author)
                    quotes.append(new_quote)

        return quotes
