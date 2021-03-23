import pytest
import time
from pipes import metadata as md

from dagster import (
    pipeline, solid, execute_pipeline, execute_solid,
    SolidExecutionResult, PipelineExecutionResult
)


def test1():
    start_time = time.time()

    run_config={
            "solids": {
                "get_filing_metadata": {
                    "inputs": {
                            "name":"Oracle Corp", 
                            "cik": "0001341439", 
                            "filing": "10-K", 
                            "no_filings": 5
                        }
                    }   
                }
            }
    
    result = execute_pipeline(md.metadata_pipeline, run_config=run_config)
    assert isinstance(result, PipelineExecutionResult)
    assert result.success

    print("--- %s Seconds ---" % (time.time() - start_time))
