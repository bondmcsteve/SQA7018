"""This problem is based on Problem 4.2.2 from the textbook"""

import re
import math
import requests
from collections import Counter
import matplotlib.pyplot as plt

def fetch_text_from_url(url):
    """Download text content from the given URL."""
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    return response.text

def extract_main_content(text):
    """Extract content between the start and end markers for Moby-Dick."""
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK MOBY-DICK"
    end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK MOBY-DICK"
    
    start_idx = text.find(start_marker)
    end_idx = text.find(end_marker)
    
    # Extract content only if both markers are found
    if start_idx != -1 and end_idx != -1:
        return text[start_idx + len(start_marker):end_idx]
    else:
        return text  # Return full text if markers are not found (for robustness)

def clean_text(text):
    """Remove punctuation and convert text to lowercase."""
    text = text.lower()
    text = re.sub(r'[!?":;,()\'\.\-\*\[\]]', '', text)  # Remove specified punctuation
    return text

def get_word_frequencies(text):
    """Clean the text and return a word frequency dictionary."""
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    
    # Count each word's frequency using
    word_counts = Counter(words)
    
    return word_counts

def top_n_words(word_counts, n=100):
    """Return the top n words sorted by frequency."""
    most_common = word_counts.most_common(n)
    return most_common

def plot_zipfs_law(word_counts, top_n=2000):
    """Plot the observed word frequencies and Zipf's Law for comparison."""
    # Get the top_n most common words
    most_common_words = word_counts.most_common(top_n)
    
    # Prepare data for Zipf's Law plot
    ranks = []
    frequencies = []
    
    for rank, (word, freq) in enumerate(most_common_words, start=1):
        ranks.append(math.log(rank))
        frequencies.append(math.log(freq))
    
    # Plot observed frequencies
    plt.figure(figsize=(10, 6))
    plt.plot(ranks, frequencies, label='Observed frequencies', color='blue')
    
    # Calculate Zipf's Law line: log(f(w)) = log(C) - a * log(r(w))
    C = frequencies[0]  # log(f(w1)) for the most frequent word
    a = 1  # Traditional value of a in Zipf's Law
    
    zipf_frequencies = [C - a * math.log(rank) for rank in range(1, top_n + 1)]
    plt.plot(ranks, zipf_frequencies, label="Zipf's Law", color='red', linestyle='--')
    
    # Configure the plot
    plt.xlabel('log(rank)')
    plt.ylabel('log(frequency)')
    plt.title("Comparison of Word Frequencies with Zipf's Law")
    plt.legend()
    plt.show()

# Main program
url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
text = fetch_text_from_url(url)

# Extract the main content between the start and end markers
main_content = extract_main_content(text)
word_counts = get_word_frequencies(main_content)

# Output the top 100 most common words
top_100_words = top_n_words(word_counts, 100)
print("Top 100 words:")
for word, count in top_100_words:
    print(f"{word}: {count}")

# Bonus exercise: Compare with Zipf's Law
plot_zipfs_law(word_counts, top_n=2000)
