FROM python:alpine3.7
RUN apk update
RUN apk add make automake gcc g++ subversion python3-dev

COPY . /app
WORKDIR /app
# RUN pip install /Users/you/en_core_web_sm-2.1.0.tar.gz
# RUN pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.0.0/en_core_web_md-2.0.0.tar.gz
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./ner-model/server.py