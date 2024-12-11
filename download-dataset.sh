#!/bin/bash

# Create a directory for the datasets
mkdir -p tatoeba_corpora
cd tatoeba_corpora

# Download and unzip corpora for five languages (English, French, Spanish, German, Portuguese)
languages=("eng" "fra" "spa" "deu" "por")

for lang in "${languages[@]}"
do
    echo "Downloading ${lang} corpus..."
    wget https://downloads.tatoeba.org/exports/per_language/${lang}/${lang}_sentences.tsv.bz2 -O ${lang}_sentences.tsv.bz2

    echo "Unzipping ${lang} corpus..."
    bzip2 -d ${lang}_sentences.tsv.bz2
done

echo "Download and extraction completed."
