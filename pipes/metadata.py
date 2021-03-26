from typing import Dict
import common
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
    #Remove non-informational items from dict
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
    comp = Company(name, cik)
    tree = comp.get_all_filings(filing_type = filing)
    docs = comp.get_documents(tree, no_of_documents= no_filings, as_documents=True)

    filings = []

    #TODO #38 change return method to yield AssetMaterialization()
    for document in docs:
        filings.append[clean_filings(document, cik, filing)]

    #TODO #39 test to ensure output is list of dicts
    context.log.info(common.log_assert_type(filings, dict))

    return filings


@pipeline(mode_defs=[ModeDefinition(name="local")])
def metadata_pipeline():
    get_filing_metadata()
