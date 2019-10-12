import ast
import spacy
from spacy.gold import GoldParse
from spacy.scorer import Scorer

import config

def evaluate(ner_model, examples):
    scorer = Scorer()
    for input_, annot in examples:
        doc_gold_text = ner_model.make_doc(input_)
        gold = GoldParse(doc_gold_text, entities=annot)
        pred_value = ner_model(input_)
        scorer.score(pred_value, gold)
    return scorer.scores

# example run

examples = [
    ('Hualien is an amazing place to visit during the spring season',
     [(0, 7, 'City')]),
    ('Hualien is a good boy.',
     [])
]

def main():
    ner_model_path = './spacy_models'
    ner_model = spacy.load(ner_model_path)

    test_data_file = 'spacy/data/test_data.txt' # 'spacy/data/test_data.txt'
    TEST_DATA = [line.rstrip('\n') for line in open(test_data_file)]
    TEST_DATA = [list(ast.literal_eval(blog)) for blog in TEST_DATA]

    # print(len(TEST_DATA))
    # print(TEST_DATA[0])
    # print(TEST_DATA[0][0])
    final_eval_data_format = []

    for website in TEST_DATA:
        for chunk in website:
            text = chunk[0]
            entities = chunk[1]['entities']
            final_eval_data_format.append((text, entities))
    results = evaluate(ner_model, final_eval_data_format)
    print(results)
    
    for entity in results['ents_per_type']:
        entity_results = results['ents_per_type'][entity]
        precision = entity_results['p']
        recall = entity_results['r']
        f_score = entity_results['f']
        print(f'Performance ({entity}):')
        print(f'Precision: {round(precision, 2)}%\n')
        # print(f'Recall: {round(recall, 2)}%')
        # print(f'F-score: {round(f_score, 2)}%\n')

if __name__ == "__main__":
    main()

# ner_model = spacy.load(ner_model_path) # for spaCy's pretrained use 'en_core_web_sm'
# results = evaluate(ner_model, examples)
# print(results)