# Common-Phrases
To identify and extract commonly used phrases from everyday language. By analyzing large corpus, we uncovers patterns in language usage very very efficiently, this will help linguists, and language enthusiasts understand the core building blocks of natural communication.


A Python tool to uncover the most common, interesting, and long phrases used in day-to-day life.
What does it do?
This tool uses counting techniques to identify and rank the most frequently used phrases in a given language dataset. Whether you're a linguist, a language learner, or just a curious wordsmith, this tool can help you discover the phrases that make a language come alive.
Example Use Cases:
Formal Greetings: Identify phrases like "It's a pleasure to meet you" or "I'm delighted to make your acquaintance".
Common Expressions: Uncover phrases like "I'm so excited to see you" or "I'm really looking forward to it".
Idiomatic Phrases: Discover phrases like "It's raining cats and dogs" or "Bite off more than you can chew".
For example, if you run the tool on a dataset of English sentences, you might get output like this:
"I'm looking forward to seeing you soon" (200 occurrences)
"It was great catching up with you" (180 occurrences)
"I'm so excited to start this new project" (160 occurrences)
...

Workflow:
Tokenizes sentences into words
Counts n-grams (2-grams, 3-grams, and 4-grams)
Prints the top N frequent n-grams

Requirements:
Python 3.x
re module for regular expressions
collections module for Counter
os module for file operations

Getting Started:
Clone the repository: git clone https://github.com/your-username/frequent-phrase-extractor.git
Install the required modules: pip install -r requirements.txt
Download the Tatoeba corpora dataset and extract it to the tatoeba_corpora directory
Run the script: python frequent_phrase_extractor.py
