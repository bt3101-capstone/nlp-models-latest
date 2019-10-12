import spacy
from spacy import displacy

import config

# colors = {"Country": "#fc9ce7", "City": "#FF5733", "Attractions": "#33FFD4"}
# options = {"ents": ["Country", "City", "Attractions"], "colors": colors}

# text = u"Singapore is an amazing place for holiday!"
output_dir = './spacy_models'

# nlp = spacy.load('en_core_web_sm')
nlp = spacy.load(output_dir)
# doc = nlp(u'This is a sentence.')
doc1 = nlp(u"Singapore is an amazing place for holiday! Pls go to Marina Bay Sands.")
doc2 = nlp(u"Singapore is an amazing place for holiday! Pls go to Marina Bay.")
doc3 = nlp(u"Hualien is a great destination for tourist to visit during the spring season")
doc4 = nlp(u"Hualien is a great kid since he was a young boy.")
doc5 = nlp(u"Hualien is a great kid.")
doc6 = nlp(u"Hualien is a good kid.")
doc7 = nlp(u"Singapore is a great kid.")
doc8 = nlp(u"Singapore is a good kid.")
displacy.serve([doc3, doc4, doc6], style='ent')