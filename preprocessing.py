import numpy as np
import pandas as pd
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
#from transformers import BertTokenizer, BertModel
#from sklearn.metrics.pairwise import cosine_similarity


# Read the entire book in chunks
def read_book(file_path, chunk_size=10000):
    book = ""
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            book += chunk
    return book


book_path = r'D:\Gethub\GP\Novels_Text\A Christmas Carol.txt'
book_content = read_book(book_path)
#print('book size: ', len(book_content))
#print(book_content[:100000])


#Clean the book text by removing special symbols, punctuation, extra whitespace and convert to lowercase.
def clean_text(text):
    # Remove special symbols and punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Convert to lowercase
    text = text.lower()
    return text


cleaned_book = clean_text(book_content)
#print('cleaned book size: ', len(cleaned_book))
#print(cleaned_book)


# Tokenize book into words
Tokenized_book = word_tokenize(cleaned_book)
#print('Tokenized book size: ', len(Tokenized_book))
#print(Tokenized_book)


# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_book = [word for word in Tokenized_book if word.lower() not in stop_words]
#print('filtered book size: ', len(filtered_book))
#print(filtered_book)


# Convert the text into numerical vectors
# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer()
# Fit and transform the book into TF-IDF vectors
numerical_book = vectorizer.fit_transform(filtered_book)
print('numerical book size: ', len(numerical_book.toarray()))
print(pd.DataFrame(numerical_book.toarray()))