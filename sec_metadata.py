from edgar import Company
import json

class EdgarMetadata():

    def __init__(self, name, cik, filing, no_filings):
        self.name = name
        self.cik = cik
        self.filing = filing
        self.no_filings = no_filings
        self.get_filing_metadata()

    @classmethod
    def get_filing_metadata(cls) -> list:
        company = Company(name, cik)
        tree = company.get_all_filings(filing_type = filing)
        docs = Company.get_documents(tree, no_of_documents=no_filings, as_documents=True)

        filings = []

        for document in docs:
            doc = (document.__dict__)

            if 'element' in doc.keys():
                del doc["element"]
            filings.append(doc)

        return(filings)