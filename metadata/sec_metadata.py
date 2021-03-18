from edgar import Company
from collections import ChainMap
import json

class SecMeta:
    def __init__(self):
        pass

    @classmethod
    def clean_filings(cls, doc_to_append, cik):
        doc_to_append = doc_to_append.__dict__
        del doc_to_append['element']
        del doc_to_append['content']['Documents']
        doc_to_append['cik'] = cik
        return doc_to_append
    
    def get_filing_metadata(self, name, cik, filing, no_filings) -> list:
        company = Company(name, cik)
        tree = company.get_all_filings(filing_type = filing)
        docs = Company.get_documents(tree, no_of_documents= no_filings, as_documents=True)
        if no_filings == 1:
            return self.clean_filings(docs, cik)
        else:
            for document in docs:
                yield self.clean_filings(document, cik)


print((list(SecMeta().get_filing_metadata(name="Oracle Corp", cik="0001341439", filing="10-K", no_filings=5))))