import os
import re
from collections import Counter

# Helper function to tokenize sentences
def tokenize(sentence):
    """Convert sentence to lowercase and split into words (ignoring punctuation)."""
    return re.findall(r'\w+', sentence.lower())

# Function to load sentences from the full dataset
def load_sentences(file_path):
    sentences = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            sentence = line.strip().split('\t')[-1]  # Use the entire line as the sentence
            if sentence:  # Only add non-empty sentences
                sentences.append(sentence)
    return sentences

# Function to count n-grams (optimized)
def count_ngrams(sentences, ngram_size):
    ngrams_counter = Counter()

    for sentence in sentences:
        words = tokenize(sentence)
        if len(words) >= ngram_size:
            for i in range(len(words) - ngram_size + 1):
                ngram = tuple(words[i:i + ngram_size])
                ngrams_counter[ngram] += 1

    return ngrams_counter

# Function to print the top N frequent n-grams
def print_top_ngrams(ngrams_counter, n=20):
    """Print the top N most common n-grams from the Counter."""
    most_common_ngrams = ngrams_counter.most_common(n)
    for ngram, count in most_common_ngrams:
        print(f"{' '.join(ngram)}: {count}")

# Path to the Tatoeba corpora
DATA_DIR = 'tatoeba_corpora'

# Process each language's dataset for full corpora analysis
languages = ['eng', 'fra', 'spa', 'deu', 'por']  # English, French, Spanish, German, Portuguese

for lang in languages:
    print(f"\nProcessing {lang} dataset...")
    
    # Load sentences from the full corpus
    file_path = os.path.join(DATA_DIR, f'{lang}_sentences.tsv')
    sentences = load_sentences(file_path)
    
    # Report progress
    total_sentences = len(sentences)
    print(f"Total sentences loaded: {total_sentences}")
    
    # Compute top n-grams for the full dataset
    for n in range(2, 5):  # For 2-grams, 3-grams, and 4-grams
        print(f"\nCounting {n}-grams...")
        ngrams_counter = count_ngrams(sentences, n)
        
        # Print the top N n-grams
        print(f"\nTop 20 {n}-grams for {lang}:")
        print_top_ngrams(ngrams_counter)

        # Show progress (e.g., after every 1000 sentences processed)
        # for i in range(0, total_sentences, 1000):
        #     print(f"Processed {min(i + 1000, total_sentences)} out of {total_sentences} sentences...")
