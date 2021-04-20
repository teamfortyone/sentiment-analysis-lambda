import json
import spacy

loaded_model = spacy.load('/opt/model_artifacts')

HEADERS = {
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': '*',
    'Content-Type': 'application/json',
}

def lambda_handler(event, context):
    try:
        input_text = event['queryStringParameters']['q']
    except KeyError:
        return {
            'statusCode': 400,
            'headers': HEADERS,
            'body': json.dumps({
                'error': 'Please provide input text'
            }),
        }
    # Generate prediction    
    parsed_text = loaded_model(input_text)
    # Determine prediction to return
    # if parsed_text.cats['pos'] > parsed_text.cats['neg']:
    #     prediction = 'Positive'
    #     score = parsed_text.cats['pos']
    # else:
    #     prediction = 'Negative'
    #     score = parsed_text.cats['neg']

    response = {
        'statusCode': 200,
        'headers': HEADERS,
        'body': json.dumps({
            'positive': round(parsed_text.cats['pos'], 5),
            'negative': round(parsed_text.cats['neg'], 5),
        }),
    }
    return response
