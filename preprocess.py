import csv
import spacy

nlp = spacy.load('de_core_news_sm')


def return_keywords(file: str):
    with open(file, encoding='latin1') as f:
        reader = csv.reader(f)
        keywords = [row[0] for row in reader if row][1:]
    return keywords


# Extract filenames of protocols from 2015-2017
def return_filenames(file: str):
    with open(file, encoding='latin1') as f:
        reader = csv.reader(f)
        docs = [row[0].strip() for row in reader][3:]
    return docs


def get_raw(directory: str, filenames: list, keywords: list):
    all_sents = []
    excluded = 0
    for name in filenames:
        with open(f"{directory}/{name}", "r") as f:
            raw_doc = f.read()
            c = sum([raw_doc.count(keyword) for keyword in keywords])
        if c > 100 and len(raw_doc) <= 1000000:
            doc = nlp(raw_doc)
            sents = [
                remove_nls(sent.text) for sent in doc.sents
                if not exclude(sent.text)
            ]
            print(sents)
            all_sents.extend(sents)
        else:
            excluded += 1
    return excluded, all_sents


def remove_nls(string):
    return string.strip().replace('\n', ' ')


def exclude(string):
    return string == '\n' or string == '\n\n' \
           or string.startswith('(') \
           or not string.endswith(('.', "!", "?"))


if __name__ == '__main__':
    my_filenames = return_filenames("stichwort-treffer.csv")
    my_keywords = return_keywords('stichwortliste.csv')
    excluded, raw_sents = get_raw(
        "CPP-BT_2021-02-17_DE_TXT_Datensatz",
        my_filenames,
        my_keywords
    )
    print(excluded)
    print(len(raw_sents))
