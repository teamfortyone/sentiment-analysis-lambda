import spacy

loaded_model = spacy.load("/opt/model_artifacts")

TEST_REVIEW = """
Transcendently beautiful in moments outside the office, it seems almost
sitcom-like in those scenes. When Toni Colette walks out and ponders
life silently, it's gorgeous.<br /><br />The movie doesn't seem to decide
whether it's slapstick, farce, magical realism, or drama, but the best of it
doesn't matter. (The worst is sort of tedious - like Office Space with less humor.)
"""

def lambda_handler(event, context):
    try:
        input_text = event['queryStringParameters']['q']
    except KeyError:
        return {
            "error": "Please provide input text"
        }
    # Generate prediction    
    parsed_text = loaded_model(input_text)
    # Determine prediction to return
    if parsed_text.cats["pos"] > parsed_text.cats["neg"]:
        prediction = "Positive"
        score = parsed_text.cats["pos"]
    else:
        prediction = "Negative"
        score = parsed_text.cats["neg"]

    response = {
        "sentiment": prediction,
        "score": score,
    }
    return response
