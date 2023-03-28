import pandas as pd

if __name__ == '__main__':
    samples = []
    for i in range(1, 11):
        df = pd.read_csv(f"annotated_data/sample{i}.csv", sep="\t")
        samples.append(df)
    data = pd.concat(samples, axis=0)
    data.drop("Unnamed: 0", axis=1, inplace=True)
    data.to_csv("../data/combined_samples.csv", sep="\t")