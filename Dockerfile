FROM python:3.6-slim

RUN apt update && apt install -y git gcc make curl

RUN python -m pip install --upgrade pip

ADD ./bot.requirements.txt /tmp

RUN pip install --upgrade pip && pip install -r /tmp/bot.requirements.txt
RUN python -c "import nltk; nltk.download('stopwords');"
RUN pip install flake8
RUN pip install pyTelegramBotAPI
RUN pip install pymongo
RUN pip install requests

ADD . /2019.1-Ludum

WORKDIR /rasa

ENV TRAINING_EPOCHS=20                     \
    MAX_TYPING_TIME=10                     \
    MIN_TYPING_TIME=1                      \
    WORDS_PER_SECOND_TYPING=5              \
    ENVIRONMENT_NAME=localhost             \
    BOT_VERSION=last-commit-hash           \
    ENABLE_ANALYTICS=False                 
