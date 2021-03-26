from typing import Dict
from edgar import Company
from dagster import (
    solid, 
    pipeline,
    ModeDefinition,  
    Dict
)

def clean_filings(doc_apnd: Dict, cik: str, filing: str):
    doc_apnd = doc_apnd.__dict__
    doc_apnd.pop('element')

    for k in ["Documents", "Items"]:
    #Get non-informational items out of dict
        if k in doc_apnd['content']: 
            doc_apnd['content'].pop(k)

    doc_apnd['cik'] = cik
    doc_apnd['filing'] = filing
    doc_apnd['fingerprint'] = cik + "+" + doc_apnd['content']['Filing Date']

    for key, value in doc_apnd['content'].items():
    # Moving {key:value} pairs from nested-dict to top level 
        doc_apnd[key] = value

    del doc_apnd['content']
    return doc_apnd

@solid
def get_filing_metadata(context, name: str, cik: str, filing: str, no_filings: int):
    company = Company(name, cik)
    tree = company.get_all_filings(filing_type = filing)
    docs = Company.get_documents(tree, no_of_documents= no_filings, as_documents=True)

    if no_filings == 1:
        output = clean_filings(docs, cik, filing)
        context.log.info("metadata of type: " + type(output))
        return output
    else:
        for document in docs:
            output = clean_filings(document, cik, filing)
            context.log.info("metadata of type: " + type(output))
            return output


@pipeline(mode_defs=[ModeDefinition(name="local")])
def metadata_pipeline():
    get_filing_metadata()
