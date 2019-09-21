import ast
import spacy
import config

def main():
    output_dir = config.SPACY_MODELS
    spacy_model = spacy.load(output_dir)
    TEST_DATA = [line.rstrip('\n') for line in open('spacy/data/test_data.txt')]
    TEST_DATA = [list(ast.literal_eval(blog)) for blog in TEST_DATA]

    hits = 0
    total = 0
    
    for website in TEST_DATA:
        for chunk in website:
            text = chunk[0]
            entities = chunk[1]['entities']
            labels = [place[0] for place in [(text[entity[0]:entity[1]], entity[2]) for entity in entities]]
            doc = spacy_model(text)

            matched_entities = [(ent.text, ent.label_) for ent in doc.ents]
            matched_entities = set(matched_entities)  # incase match more than one
            for _ in labels:
                total += 1

            for matched_entity in matched_entities:
                if matched_entity[0] in labels:
                    hits += 1
            
            print("Correct Entities: ", labels)
            print("Found Entities: ", matched_entities)
    print(f'Accuracy: {(hits/total)*100} %')

    # test the model
#     spacy_model = spacy.load(output_dir)
#     for text, _ in TEST_DATA:
#         doc = spacy_model(text)
#         print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
        # print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])

if __name__ == "__main__":
    main()
