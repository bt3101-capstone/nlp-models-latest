DOCCANO_DATA =  'doccano/final.json' #'doccano/sg_output_data.json'

ALL_DATA = [
    DOCCANO_DATA
]

SPACY_MODELS = './spacy_models'
N_ITER = 100

TEST_DATA = [
    (
        """
        While Singapore is a small country, there is still a lot to see. Just 31 miles wide and 17 miles long, 
        Singapore has a remarkable amount of must-see neighborhoods like Little India, Bugis, Chinatown, Marina Bay, the Financial District, and Sentosa Island.
        Public Transport: The Mass Rapid Transit (MRT) is an easy and affordable way to get around Singapore. 
        The price of tickets depends on where you are going and generally runs around SGD 4 (USD 3). 
        If you are planning to explore as much of the city as possible, the Singapore Tourist Pass can be a great deal.
        """
        , {}
    )
]
