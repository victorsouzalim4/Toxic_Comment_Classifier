import unicodedata
import re

CONTRACTIONS = {
    r"\bcan't\b": "cannot",
    r"\bwon't\b": "will not",
    r"\bdon't\b": "do not",
    r"\bdoesn't\b": "does not",
    r"\bdidn't\b": "did not",
    r"\bi'm\b": "i am",
    r"\bit's\b": "it is",
    r"\bhe's\b": "he is",
    r"\bshe's\b": "she is",
    r"\byou're\b": "you are",
    r"\bthey're\b": "they are",
    r"\bwe're\b": "we are",
    r"\blet's\b": "let us",
    r"\bcouldn't\b": "could not",
    r"\bshouldn't\b": "should not",
    r"\bwouldn't\b": "would not",
}
def normalize_text(comment: str):
    
    comment = ''.join(
        c for c in unicodedata.normalize('NFKD', comment)
        if not unicodedata.combining(c)
    )

    comment = re.sub(r'[^a-zA-Z0-9 ]+', ' ', comment) # remove caracteres especiais
    comment = re.sub(r'\s+', ' ', comment).strip()  # remove sequencia de espaços
 
    return comment

def remove_noise(comment: str):     
    comment = re.sub(r'http[s]?://\S+', ' ', comment)
    comment = re.sub(r'www\.\S+', ' ', comment)
    
    # 3) remover tags HTML
    comment = re.sub(r'<[^>]+>', ' ', comment)
    
    # 4) remover menções e hashtags (@user, #tag)
    comment = re.sub(r'[@#][^\s]+', ' ', comment)

    return comment


def normalize_contractions(comment):

    for pattern, replacement in CONTRACTIONS.items():
        comment = re.sub(pattern, replacement, comment)
    return comment