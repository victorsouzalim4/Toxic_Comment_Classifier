import pandas as pd
from treat_data import treat_comment

df = pd.read_csv(
    "Arquivos/train.csv/train.csv",
    sep=",",        
    quotechar='"',    
    engine="python"   
)

print(df.head())

df["comment_text"] = df["comment_text"].apply(treat_comment)

print(df.head())
# print(treat_comment(df.loc[1, "comment_text"]))