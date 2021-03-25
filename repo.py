from dagster import repository

from pipes.metadata import metadata_pipeline

@repository
def wallstreet_repo():
    return [metadata_pipeline]