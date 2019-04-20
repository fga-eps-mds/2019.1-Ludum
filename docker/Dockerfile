from python:3.6-slim

run apt update && apt install -y git gcc make curl

run python -m pip install --upgrade pip

add ./bot.requirements.txt /tmp

run pip install --upgrade pip && pip install -r /tmp/bot.requirements.txt
run python -c "import nltk; nltk.download('stopwords');"
RUN pip install flake8
RUN pip install pyTelegramBotAPI
RUN pip install pymongo

ADD . /2019.1-Ludum
add ./scripts /scripts

workdir /bot

env TRAINING_EPOCHS=20                     \
    MAX_TYPING_TIME=10                     \
    MIN_TYPING_TIME=1                      \
    WORDS_PER_SECOND_TYPING=5              \
    ENVIRONMENT_NAME=localhost             \
    BOT_VERSION=last-commit-hash           \
    ENABLE_ANALYTICS=False                 \

