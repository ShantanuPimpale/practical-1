import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Define stopwords
stop_words = set(stopwords.words("english"))

# Define the sentence
sentence = "I will walk 500 miles and I would walk 500 more, just to be the man who walks a thousand miles to fall down at your door."

# Convert the sentence to lowercase
sentence = sentence.lower()

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Tokenize the sentence into sentences
sentences = sent_tokenize(sentence)

# Remove stopwords
filtered_words = [word for word in words if word not in stop_words]

# Initialize Porter stemmer
stemmer = PorterStemmer()

# Perform stemming
stemmed_words = [stemmer.stem(word) for word in filtered_words]

# Count the frequency of stemmed words
word_counts = Counter(stemmed_words)

# Perform part-of-speech tagging
pos_tagged = nltk.pos_tag(stemmed_words)

# Count the frequency of POS tags
pos_counts = Counter(tag for _, tag in pos_tagged)

# Print results
print("Original Sentence:")
print(sentence)
print("\nTokenized Words:")
print(words)
print("\nTokenized Sentences:")
print(sentences)
print("\nStopwords:")
print(stop_words)
print("\nFiltered Words (without stopwords):")
print(filtered_words)
print("\nStemmed Words:")
print(stemmed_words)
print("\nWord Counts:")
print(word_counts)
print("\nPOS Tagging:")
print(pos_tagged)
print("\nPOS Tag Counts:")
print(pos_counts)