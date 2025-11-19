import unicodedata
import re

def treat_comment(comment: str):
    # print(comment)
    comment = normalize_text(comment)
    return comment

def normalize_text(comment: str):
    comment = comment.lower()
    comment = ''.join(
        c for c in unicodedata.normalize('NFKD', comment)
        if not unicodedata.combining(c)
    )

    comment = re.sub(r'\s+', ' ', comment).strip()
    comment = re.sub(r'[^a-zA-Z0-9 ]+', '', comment)

    return comment