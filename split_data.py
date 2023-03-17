import pathlib
import pandas as pd


def split_df(data, n):
    samples = []
    for i in range(n):
        sample = data.sample(50, random_state=10, axis=0)\
            .drop(["Unnamed: 0"], axis=1)
        sample["Frame"] = ["" for i in range(50)]
        samples.append(sample)
    return samples


if __name__ == '__main__':
    df = pd.read_csv("extracted_sents.csv")
    sent_samples = split_df(df, 10)
    path = pathlib.Path("samples")
    path.mkdir(parents=True, exist_ok=True)
    for i, sample in enumerate(sent_samples):
        sample.to_csv(f"samples/sample{i+1}.csv")