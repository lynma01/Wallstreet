from dagster import repository

from pipes.metadata import metadata_pipeline

@repository
def metadata_repo():
    return [metadata_pipeline]