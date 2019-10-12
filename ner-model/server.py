from typing import List
from typing import Tuple

from flask import Flask, request, jsonify
import spacy
import config

app = Flask(__name__)

@app.route('/ner', methods=['POST'])
def get_ner_tags():
    """
    Generates NER tags for input text.
    """

    try:
        req_data = request.get_json()
        input_text = req_data['input_text']
        print(f'Input text: {input_text}')

        output_dir = config.SPACY_MODELS
        spacy_model = spacy.load(output_dir)

        doc = spacy_model(input_text)
        matched_entities = [(ent.text, ent.label_) for ent in doc.ents]
        print(f'Printing matched entities\n')
        print(matched_entities)

        final_resp = create_response(
            matched_entities,
            200,
            'OK - Successfully found NER tags!'
        )
    except Exception as e:
        print(e)
        final_resp = create_response(
            f'{type(e)} - {str(e)}',
            400,
            'Bad Request - Failed to find NER tags!'
        )

    return jsonify(final_resp)

def create_response(results: List[Tuple[str,str]], status: int, message: str) -> dict:
    '''
    Create API response object.
    '''
    response = {
        'metadata': {
            'status': status,
            'message': message
        },
        'data': results
    }

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=True, port=5000)
