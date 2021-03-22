from edgar import Company
from collections import ChainMap
import json
import time


# TODO: move SecMeta() into dagster syntax in /src/pipes 
class SecMeta:
    def __init__(self):
        pass

    @classmethod
    def clean_filings(cls, doc_apnd, cik, filing):
        doc_apnd = doc_apnd.__dict__
        doc_apnd.pop('element')

        for k in ["Documents", "Items"]:
            if k in doc_apnd['content']: 
                doc_apnd['content'].pop(k)

        doc_apnd['cik'] = cik
        doc_apnd['filing'] = filing
        doc_apnd['fingerprint'] = cik + "+" + doc_apnd['content']['Filing Date']

        for key, value in doc_apnd['content'].items():
            doc_apnd[key] = value

        del doc_apnd['content']
        return doc_apnd
    
    def get_filing_metadata(self, name, cik, filing, no_filings):
        company = Company(name, cik)
        tree = company.get_all_filings(filing_type = filing)
        docs = Company.get_documents(tree, no_of_documents= no_filings, as_documents=True)
        if no_filings == 1:
            return self.clean_filings(docs, cik, filing)
        else:
            for document in docs:
                yield self.clean_filings(document, cik, filing)