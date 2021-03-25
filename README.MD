# Wallstreet Project

- [Wallstreet Project](#wallstreet-project)
  - [Summary](#summary)
  - [Techstack](#techstack)
      - [Container Orchestrator](#container-orchestrator)
      - [Data Engineering Orchestrator](#data-engineering-orchestrator)
        - [Direct Object Storage](#direct-object-storage)
        - [Storage Schema](#storage-schema)
      - [Machine Learning](#machine-learning)
      - [Business Intelligence](#business-intelligence)
  - [Changelog](#changelog)

## Summary
Hello! This repository is a data engineering proof-of-concept project. The goal of the project is to orchestrate a series of financial-market data pipelines into a data-lake. Against which, I'll be running a series of Machine Learning Jupyter Notebooks. The results of these analysis will be broadcast onto a Business Intelligence Dashboard.

## Techstack

<!--- 
TODO #17 include justification for techstack tooling
TODO #18 create mermaid charts for data pipeline flow
TODO #19 add inline images for techstack 
--->

#### Container Orchestrator

Kubernetes

#### Data Engineering Orchestrator

Dagster -> Dagit UI

##### Direct Object Storage

Minio

##### Storage Schema

Apache Delta Lake (Potentially -> Apache Druid) / Amazon S3

#### Machine Learning

Jupyter Notebooks with SciKit Learn

#### Business Intelligence

Metabase

## Changelog

<!--- TODO #20 update changelog --->
