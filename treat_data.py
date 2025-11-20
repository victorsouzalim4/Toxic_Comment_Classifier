from aux_functions import *
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def treat_comment(comment: str):
    tokens = parsing(comment)
    tokens = remove_stop_words(tokens)

    return tokens

def parsing(comment: str):
    comment = comment.lower()
    comment = normalize_contractions(comment)
    comment = remove_noise(comment)
    comment = normalize_text(comment)
    tokens = comment.split()

    return tokens

def remove_stop_words(tokens: list=[]):
    stop_words = set(stopwords.words('english'))

    return [t for t in tokens if t not in stop_words]

