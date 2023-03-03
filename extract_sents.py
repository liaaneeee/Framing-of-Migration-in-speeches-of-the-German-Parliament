import json
import spacy
import csv
import preselect

nlp = spacy.load('de_core_news_sm')


def read_json(filename: str):
    with open(filename, "r") as f:
        jsonString = f.read()
    raw_sents = json.loads(jsonString)
    return raw_sents


def preprocess(string):
    new_string = string.strip()
    replacements = {'-\n': '', '\n': ' ', '\n\n': ' ', ' .': '.'}
    for old, new in replacements.items():
        new_string = new_string.replace(old, new)
    return new_string


def extract_sents(raw_sents: list, keywords: list):
    extracted = []
    for sent in raw_sents:
        if sent[0].isupper():
            for keyword in keywords:
                match = sent.count(keyword)
                if match:
                    extracted.append(preprocess(sent))
                    break
    return extracted


def save_to_csv(sents: list, filename: str):
    fields = ['Sentence']
    rows = [[sent] for sent in sents]
    with open(filename, "w") as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(rows)


if __name__ == '__main__':
    raw_sentences = read_json("raw_sents.json")
    keywords = preselect.return_keywords('stichwortliste.csv')
    extracted_sents = extract_sents(raw_sentences, keywords)
    save_to_csv(extracted_sents, "extracted_sents.csv")
