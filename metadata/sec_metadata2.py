from edgar import Company
from collections import ChainMap
import json
import time

class SecMeta:

    def __init__(self):
        pass

    @classmethod
    def return_filings(cls, doc_to_append, appendee):
        doc_to_append = doc_to_append.__dict__
        del doc_to_append['element']
        appendee.append(doc_to_append)

    
    def get_filing_metadata(self, name, cik, filing, no_filings) -> list:
        company = Company(name, cik)
        tree = company.get_all_filings(filing_type = filing)
        docs = Company.get_documents(tree, no_of_documents= no_filings, as_documents=True)

        filings = []

        if no_filings == 1:
            self.return_filings(docs, filings)
        else:
            for document in docs:
                self.return_filings(document, filings)
        return(filings)

