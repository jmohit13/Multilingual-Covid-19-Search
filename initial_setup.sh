#!/bin/sh

python -m nltk.downloader stopwords
python -m nltk.downloader punkt
python -m nltk.downloader words
python -m spacy download en
python -m laserembeddings download-models
