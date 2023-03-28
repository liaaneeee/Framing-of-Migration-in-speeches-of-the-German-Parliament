import pathlib
import pandas as pd

pd.options.mode.chained_assignment = None


def split_df(data, n):
    samples = []
    for i in range(n):
        sample = data.iloc[(i*50):(i+1)*50, :]
        samples.append(sample)
        sample["Frame"] = ["" for j in range(50)]
        sample.drop("Unnamed: 0", axis=1, inplace=True)
    return samples


def remove_quotes(data):
    data["Sentence"] = [sent.strip('"') for sent in data["Sentence"]]
    return data


if __name__ == '__main__':
    df = pd.read_csv("../preselection&extraction/extracted_sents.csv")
    data = df.iloc[:500, :]
    sent_samples = split_df(data, 10)
    path = pathlib.Path("samples")
    path.mkdir(parents=True, exist_ok=True)
    for i, sample in enumerate(sent_samples):
        sample.to_csv(f"samples/sample{i+1}.csv", sep="\t")