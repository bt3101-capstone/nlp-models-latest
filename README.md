# nlp-models

## Content
- [nlp-models](#nlp-models)
  - [Content](#content)
  - [Folder Structure](#folder-structure)
  - [Summary](#summary)
  - [Data Collection Pipeline](#data-collection-pipeline)
  - [Models](#models)

## Folder Structure
```
|__ data-collection-pipeline
    |__ .awis.py.credentials
    |__ data-collection-blogger-urls (final).ipynb
    |__ data-collection-blogger-urls (with para processing).ipynb
    |__ data-collection-awis.ipynb
    |__ reverse-entity-mapping.ipynb
    |__ Bloggers domain WIP.csv
|__ doccano
    |__ examples
|__ .gitignore
|__ README.md
```

## Summary
This repository contains NER models using different open-sourced libraries and the scripts for data collection and pre-processing.

Doccano is an open-sourced annotation tool which can be used to more easily prepare the training data required to train the NER model.
Labels can be uniquely defined based on what is required by the open-sourced training libraries being used (eg. Spacy, Gensim etc.)

## Data Collection Pipeline
1. data-collection-blogger-urls (with para processing)
Allows user to perform google search and extract text from each website of the search results. Data will be output in data-collection-pipeline folder

1. data-collection-blogger-urls (final)
Final version of data collection for blogger urls, without text extraction from domains

3. data-collection-awis
Calls the AWIS API to retrieve website metrics

4. reverse-entity-mapping
Prepares the mapping of entity for automated labelling of data

## Models
1. `spacy_models_old`: Model without negative training labels.
2. `spacy_models`: Model with negative training labels.