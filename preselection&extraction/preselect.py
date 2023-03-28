import csv
import spacy
import json

nlp = spacy.load('de_core_news_sm')


def return_keywords(file: str, encoding):
    with open(file, encoding) as f:
        reader = csv.reader(f)
        keywords = [row[0] for row in reader if row][1:]
    return keywords


# Extract filenames of protocols from 2015-2017
def return_filenames(file: str, encoding):
    with open(file, encoding) as f:
        reader = csv.reader(f)
        docs = [row[0].strip() for row in reader][3:]
    return docs


def preselect(directory: str, filenames: list, keywords: list):
    selected = []
    excluded = []
    for name in filenames:
        with open(f"{directory}/{name}", "r") as f:
            raw_doc = f.read()
            c = sum([raw_doc.count(keyword) for keyword in keywords])
        # Arbitrary criteria, manually check excluded docs!
        if c > 50 and len(raw_doc) <= 1000000:
            filename = name.removeprefix("CPP-BT_Bundestag_Plenarprotokoll_")\
                .removesuffix(".txt")
            selected.append((filename, raw_doc))
        else:
            excluded.append(name)
    return selected, excluded


def get_raw_sents(preselected: list):
    raw_sents = []
    for filename, raw_doc in preselected:
        doc = nlp(raw_doc)
        sents = [sent.text for sent in doc.sents if not exclude(sent.text)]
        for sent in sents:
            raw_sents.append((filename, sent))
    return raw_sents


def exclude(sent):
    return sent == '\n' or sent == '\n\n' \
           or sent.startswith('(') \
           or not sent.endswith(('.', "!", "?"))


def save_raw_sents(raw_sents: list, filename: str):
    jsonString = json.dumps(raw_sents)
    with open(filename, "w") as f:
        f.write(jsonString)


if __name__ == '__main__':
    # Extract filenames
    my_filenames = return_filenames("stichwort-treffer.csv", 'latin1')
    # Extract keywords
    my_keywords = return_keywords('stichwortliste.csv', 'latin1')
    # Preselection
    selected_docs, excluded_docs = preselect(
        "CPP-BT_2021-02-17_DE_TXT_Datensatz",
        my_filenames,
        my_keywords
    )
    # Retrieve raw sentences
    raw_sentences = get_raw_sents(selected_docs)
    # Save raw sentences to json
    save_raw_sents(raw_sentences, "raw_sents.json")