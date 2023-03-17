import pandas as pd
from textblob_de import TextBlobDE


def return_polarity(sent):
    blob = TextBlobDE(sent)
    return abs(blob.polarity)


def sort_by_polarity(data):
    data["polarity"] = data["Sentence"].apply(return_polarity)
    sorted_data = data.sort_values(by=["polarity"], ascending=False)
    return sorted_data


if __name__ == '__main__':
    df = pd.read_csv("extracted_sents.csv")
    sorted_df = sort_by_polarity(df)
    sorted_df.to_csv("sorted_sents.csv")


