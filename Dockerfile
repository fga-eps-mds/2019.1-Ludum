FROM python:3.6

RUN pip install rasa_core
RUN pip install rasa_nlu[spacy] && \
    python -m spacy download pt

RUN pip install rasa_nlu[tensorflow]

RUN pip install pymongo
RUN pip install requests

RUN mkdir /2019.1-Ludum

ADD . /2019.1-Ludum
