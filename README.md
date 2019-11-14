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
    |__ data-collection-awis.ipynb
    |__ data-collection-combined-awis-and-scraped-data.ipynb
    |__ data-collection-google-trends.ipynb
    |__ reverse-entity-mapping.ipynb
    |__ Bloggers domain WIP.csv
    |__ convert_to_json.py
    |__ convert_to_json_spacey.py
    |__ activitiesCompositeLabelsDict.json
    |__ cleaned_scraped_data_full.csv
    |__ curatour.py
    |__ mapping.py
    |__ scraping.sh
    |__ weblinks.txt
        |__ aws_model
            |__ aws.py
            |__ aws_text_format.py
        |__ google-trends-data
            |__ Indonesia
            |__ Japan
            |__ Singapore
            |__ South Korea
            |__ Taiwan
            |__ Thailand
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

1. data-collection-blogger-urls (final)
- Final version of data collection for blogger urls, without text extraction from domains

2. data-collection-awis
- Calls the AWIS API to retrieve website metrics

3. data-collection-combined-awis-and-scraped-data.ipynb
- formatter / data generator script

4. data-collection-google-trends.ipynb
- Extraction of manually downloaded Google Trends data from the folder "google-trends-data" and formats it

1. reverse-entity-mapping
- Prepares the mapping of entity for automated labelling of data

6. scraping.sh
- Maps the entity to the POI, for example, Little India is mapped as Attractions, Cultural.


## Procedure
1. Run data-collection-blogger-urls (final).ipynb 
   - input: 
     - Bloggers domain WIP [.csv]
     - final_for_zj_with_web_links [.txt]
   - output: 
     - listOfBlogsUrlsForScrapping [.txt] / listOfBlogsUrlsForScrapping-newBlogs [.txt] (includes a few new blogs out of the 205 domains)
     - blogDataDbInsertion [.json]
 - 
2. Run reverse-entity-mapping.ipynb 
   - input: TripAdvisor entity-A_Type mapping csv (Provided by Curatour)
   - output: Dict of entity-labels [.json]

3. Run scraping.sh
   - input: list of blogPostUrls [.txt], Dict of entity-labels [.json]
   - output: list of annotated blogposts [.txt]
  
4. Run data-collection-awis.ipynb
   - input: 
     - Bloggers domain WIP [.csv]
   - output: 
     - finalBlogsAWISMetricsDbInsertion [.json]

5. Run data-collection-combined-awis-and-scraped-data.ipynb
   - inputs: 
     - blogsAWISMetricsDbInsertion [.json]
     - blogDataDbInsertion [.json]
     - Bloggers domain WIP [.csv]
     - tempBlogsAWISMetricsDbInsertion [.json]
     - entitiesCountryDict [.json]
            TripAdvisor entity-latlong mapping csv (Provided by Curatour)
   - output: 
     - finalAwisAndBlogsDataDbInsertion [.json]
     - dateEntitiesDbInsertion [.json]
     - timePeriodEntitiesDbInsertion [.json]
     - finalMedianLoadTimeDbInsertion [.json]
     - finalMedianMetricsDbInsertion [.json]
     - finalBlogsAWISMetricsDbInsertion [.json]

6. Run data-collection-google-trends.ipynb
   - inputs: 
     - Full_Activities_ZJ [.csv]
     - dateEntitiesDbInsertion [.json]
     - timePeriodEntitiesDbInsertion [.json]
   - output:
     - finalDateEntitiesDbInsertion [.json]
     - finalMonetizeEntitiesDbInsertion [.json]
     - finalTimePeriodEntitiesDbInsertion [.json]
  
7. Run training of spaCy Model
   - input: list of annotated blogposts [.txt]
   - output: spaCy Model

