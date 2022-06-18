import pandas
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Gets Quotes from a CSV File"""
    supported_extension = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest extension')

        quotes = list()
        csv = pandas.read_csv(path, header=0)
        for index, row in csv.iterrows():
            new_quote = QuoteModel(row[0], row[1])
            quotes.append(new_quote)

        return quotes
