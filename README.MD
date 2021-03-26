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

## Summary

Hello! This repository is a data engineering proof-of-concept project. The goal of the project is to orchestrate a series of financial-market data pipelines into a data-lake. Against which, I'll be running a series of Machine Learning Jupyter Notebooks. The results of these analysis will be broadcast onto a Business Intelligence Dashboard.

## Techstack

<!--- 
TODO #18 create mermaid charts for data pipeline flow
TODO #19 add inline images for techstack 
TODO #26 incorporate sphinx documentation
--->

#### Container Orchestrator

Kubernetes will be orchestrating the Docker containers in this repository. Because Kubernetes is a autonomous container manager, it'll be able to start, inspect, and restart containers while the program is in execution. This ensures that there's a reasonable amount of autonomous infrastructure upholding the integrity of the dagster pipelines. Kubernetes also keeps the opportunity open for this project to be hosted in a cloud-native format like Amazon EC2- autonomously increasing and decreasing cloud presence as needed to meet variable demand.

#### Data Engineering Orchestrator

Dagster, and its user interface Dagit, will be the primary means of observing the data pipelines. Dagster, because of the deliberate abstraction of its design, is able to continuously integrate more specialized tools like Airflow, Great Expectations, or Jupyter Notebooks. This keeps the data-pipeline infrastructure modular and easily maintainable because it's able to swap tools in and out at will. And more fundamentally, because Dagster is primarily interfaced with through Python, the code remains broadly human-readable and accessible.

##### Direct Object Storage

Minio mocks Cloud S3 bucket containers. This allows for project development to remain local until cloud-operational costs become sustainable. Minio is a Kubernetes-native hosted S3 server, so its S3 storage can be containerized and autonomously orchestrated by the same software (Kubernetes) that's underlying every other part of the project. This means that all of the project's infrastructure can be tested via CI/CD methods- for example, GitHub Actions.  

##### Storage Schema

Apache Delta Lake is a revolutionary technology that I don't understand. However, I know what it's definitely not: an OLAP cube. Apache Delta Lake side steps the need for MDX queries and slow-moving datawarehouses, while also ensuring the strongest level of data isolation: serializibility. With Delta Lake, it's possible to freeze data in-time: allowing for roll-backs, audits at specific datetimes, and reproducing expiriments. More over, it's highly optimized for data streaming.

#### Machine Learning

Jupyter Notebooks with SciKit Learn are actually orchestrated within Dagster pipelines. So as data is refined into a certain shape or quality, it can be analyzed at specific checkpoints for insight.

More over, because of the inclusion of Apache Delta Lake, it's also possible to run ML/AI algorithims against the summation of all the data itself with MLFlow, or perhaps Kedro.

#### Business Intelligence

Metabase, with its deep interaction, pretty graphs, and especially share-able dashboards make for a natural choice. This would be best considered as the packaging for the final, informational "product".
