import time
from pipes import metadata as md
from dagster import (
    execute_pipeline,
    execute_solid,
    PipelineExecutionResult,
    SolidExecutionResult,
    check_dagster_type,
    Dict,
    List,
    Any
)

def test_meta_solid():
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
    
    result = execute_solid(md.get_filing_metadata, run_config=run_config)
    assert isinstance(result, SolidExecutionResult)
    assert result.success
    assert check_dagster_type(List[Dict[Any, Any]], [{"foo":"bar"}, {"foo":"bar"}]).success

    print("--- %s Seconds ---" % (time.time() - start_time))

def test_meta_pipeline():
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

