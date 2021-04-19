FROM lambci/lambda:build-python3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /spacy
COPY requirements.txt /spacy
RUN pip install  -r requirements.txt -t python
RUN ["zip", "-r9", "spacy-layer.zip", "./python"]
CMD ["/bin/sh"]
