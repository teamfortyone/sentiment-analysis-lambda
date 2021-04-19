import json
import spacy

loaded_model = spacy.load('/opt/model_artifacts')

def lambda_handler(event, context):
    try:
        input_text = event['queryStringParameters']['q']
    except KeyError:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
            },
            'body': 'Please provide input text',
        }
    # Generate prediction    
    parsed_text = loaded_model(input_text)
    # Determine prediction to return
    if parsed_text.cats['pos'] > parsed_text.cats['neg']:
        prediction = 'Positive'
        score = parsed_text.cats['pos']
    else:
        prediction = 'Negative'
        score = parsed_text.cats['neg']

    response = {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*',
        },
        'body': json.dumps({
            'sentiment': prediction,
            'score': score,
        }),
    }
    return response
