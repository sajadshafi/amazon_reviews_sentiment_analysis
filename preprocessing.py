# This script was used for test purpose for the cleaning the reviews, like removing emojis, punctuations, etc.


import re
import nltk
import emoji
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def remove_emojis(text):
    reg = emoji.get_emoji_regexp()
    emoji_free_text = reg.sub(r'', text)
    return emoji_free_text


# Cleaining function
def preprocess(input_text):
    lower_text = review.lower()

    punctuations = '''`!()-[]{};:'"\,<>./?@#$%^&*_~=+°'''

    lower_text = re.sub(r"@[A-Za-z0-9]+", "", lower_text)   # Removes the @mentions from the tweets
    lower_text = re.sub(r"[0-9]+", "", lower_text)          # Removes the Numbers from the tweets

    # tokenization
    tokens = word_tokenize(lower_text)

    stopwords = stopwords.words("english")
    # Removing stopwords
    filtered_text = [word for word in tokens if word not in stopwords]

    # look for empty words or words just made of two letters and remove that
    for token in filtered_text:
        if token == "":
            filtered_text.remove(token)

    filtered_text = ' '.join([word for word in filtered_text])

    clean_text = remove_emojis(filtered_text)

    # Removing punctuations in string 
    # Using loop + punctuation string 
    for ele in clean_text:  
        if ele in punctuations:  
            clean_text = clean_text.replace(ele, "")

    # Removing small words with length less than 3
    clean_text = ' '.join([t for t in clean_text.split() if len(t)>=3])

    return word_tokenize(clean_text)