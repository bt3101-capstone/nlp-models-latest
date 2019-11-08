# nlp-models

## Content
- [nlp-models](#nlp-models)
  - [Content](#content)
  - [Folder Structure](#folder-structure)
  - [Summary](#summary)
  - [StanfordNER installation](#stanfordner-installation)
  - [Data Collection Pipeline](#data-collection-pipeline)
  - [Procedure](#procedure)

## Folder Structure
```
|__ spacy
    |__ ner_model.py
|__ data-collection-pipeline
    |__ .awis.py.credentials
    |__ data-collection-blogger-urls (final).ipynb
    |__ data-collection-blogger-urls (with para processing).ipynb
    |__ data-collection-awis.ipynb
    |__ reverse-entity-mapping.ipynb
    |__ Bloggers domain WIP.csv
    |__ convert_to_json.py
    |__ convert_to_json_spacey.py
    |__ activities_composite_labels_dict.json
    |__ curatour.py
    |__ mapping.py
    |__ scraping.sh
    |__ weblinks.txt
        |__ aws_model
            |__ aws.py
            |__ aws_text_format.py
        |__ testing_of_model
            |__ scraping_for_testing.sh
            |__ weblink_test.txt
            |__ convert_to_json.py
            |__ convert_to_json_spacey.py
            |__ curatour.py
            |__ mapping.py
            |__ activities_composite_labels_dict.json
|__ .gitignore
|__ README.md
```

## Summary
This repository contains NER models using different open-sourced libraries and the scripts for data collection and pre-processing.

We used one of StanfordNER's open-sourced annotation tool which can be used to more easily prepare the training data required to train the NER model.

Labels can be uniquely defined based on what is required by the open-sourced training libraries being used (eg. spaCy etc.)

## StanfordNER installation
Go to https://nlp.stanford.edu/software/CRF-NER.html
Download the zip file by following their instructions.

## Data Collection Pipeline
1. data-collection-blogger-urls (with para processing)
Allows user to perform google search and extract text from each website of the search results. Data will be output in data-collection-pipeline folder

2. data-collection-blogger-urls (final)
Final version of data collection for blogger urls, without text extraction from domains

3. data-collection-awis
Calls the AWIS API to retrieve website metrics

4. reverse-entity-mapping
Prepares the mapping of entity for automated labelling of data

5. scraping.sh
Maps the entity to the POI, for example, Little India is mapped as Attractions, Cultural.


## Procedure
1. Run google-search.ipynb 
   - input: Google search term
   - output: list of blogPostUrls [.txt]
2. Run reverse-entity-mapping.ipynb 
   - input: TripAdvisor entity-A_Type mapping csv (Provided by Curatour)
   - output: Dict of entity-labels [.json]
3. Run scraping.sh
   - input: list of blogPostUrls [.txt], Dict of entity-labels [.json]
   - output: list of annotated blogposts [.txt]
4. Run db-formatter.ipynb
   - inputs: list of annotated blogposts [.txt]
            TripAdvisor entity-latlong mapping csv (Provided by Curatour)
   - output: Dict of blogs [.json]
5. Run data-collection-awis.ipynb
   - input: list of blogPostUrls [.txt]
   - output: Dict of AWIS Metrics [.json]
6. Run training of spaCy Model
   - input: list of annotated blogposts [.txt]
   - output: spaCy Model

