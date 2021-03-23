from typing import Dict
from edgar import Company
import time
from dagster import (
    solid, pipeline, Field, OutputDefinition, InputDefinition, Output
)

@solid
def get_filing_metadata(context, name: str, cik: str, filing: str, no_filings: int):
    company = Company(name, cik)
    tree = company.get_all_filings(filing_type = filing)
    docs = Company.get_documents(tree, no_of_documents= no_filings, as_documents=True)

    # TODO #13 move clean_filings() into its own solid def
    def clean_filings(doc_apnd: Dict, cik: str, filing: str):
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

    if no_filings == 1:
        return clean_filings(docs, cik, filing)
    else:
        for document in docs:
            return Output(clean_filings(document, cik, filing))

@pipeline
def metadata_pipeline():
    get_filing_metadata()
