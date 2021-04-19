# Movie Review Sentiment Analysis with AWS Lambda

## Pre-requisites

Built and tested on WSL2 Ubuntu 20.04

- Python v3.8
- Docker (Tested on WSL2)
- AWS CLI ([install instructions](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html))
- Model artifacts from the NLP repo (link here)

## Deployment

1. Create a python virtual envionment

```
<project-root>$ python -m venv .venv
<project-root>$ source .venv/bin/activate
(.venv) <project-root>$ pip install -r requirements-dev.txt
```

2. Go to `./layers` and build & extract the spaCy dependency layer.

```
(.venv) ../layers$ docker build -t spacy-layer .
(.venv) ../layers$ docker run -d -it --name spacy spacy-layer

(.venv) ../layers$ docker cp spacy:/spacy/spacy-layer.zip .
```

This will copy the spacy.zip file from the container to host.

3. Ensure that the `model_artifacts.zip` from the NLP repo is placed in the project root.

4. Run `aws configure` and add AWS Access, Secret Keys, and select your default region and response format (json).
   [Learn how to create AWS Access & Secret Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).
5. From project root directory: `sam deploy --guided`

## Request and Response format

After deployment, SAM will print the API endpoint URL. It accepts a query parameter `q` with the text as input.

### Request:

```
GET /predict?q=<input-text-here>
```

### Response (Success):

Sentiment: Positive/Negative

Score: Between 0 & 1

```
{
    "sentiment": "Positive",
    "score": 0.9999545812606812
}
```

### Response (Failure):

```
{
    "error": "Please provide input text"
}
```
