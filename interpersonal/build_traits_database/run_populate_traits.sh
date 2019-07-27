#!/usr/bin/env bash

# run_populate_traits.sh
# used if you want to generate the traits database traits.db

echo "Welcome to traits database populator!"
echo "This script populates your own Traits database (traits.db)"

# this is a temporary workaround because we could not figure out how to import TraitDao.py when it was in its original directory
echo "Copying TraitDao.py into current directory"
cp ../classes/TraitDao.py .

if wc -c < GoogleNews-vectors-negative300.bin.gz | grep 1647046227; then
    echo "GoogleNews-vectors is already downloaded"
else
    echo "Downloading GoogleNews-vectors (1.57 GB)"
    link="https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"
    wget -c $link 2>/dev/null || curl -L -O -C - $link || curl -L -O $link
fi



if wc -c < brown.zip | grep 3314357; then
    echo "Brown Corpus is already downloaded"
else
    echo "Downloading Brown Corpus (3.3 MB)"
    link="https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/brown.zip"
    wget -c $link 2>/dev/null || curl -L -O -C - $link || curl -L -O $link
fi


echo "Initializing the Traits database file"
echo "This operation should take a few minutes"
python3 ./populate_traits.py
