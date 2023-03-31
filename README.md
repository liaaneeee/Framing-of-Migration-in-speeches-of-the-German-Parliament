# **Framing of Migration in Speeches of the German Parliament**

- **Authors:** Veronika Hentze, Thao Van Liane Nguyen

- **Contact:** hentze@uni-potsdam.de, nguyen12@uni-potsdam.de


***
# Description
This repository contains the course project for the seminar **Automatische Textanalyse in den Politikwissenschaften** of the University of Potsdam.

It contains a corpus with annotations for the framing of migration in speeches of the German Parliament and an implementation of a classifier for the automatic classification of stereotypes. <br>
This project is an attempt to replicate the study ***How Do You Speak about Immigrants? Taxonomy and StereoImmigrants Dataset for Identifying Stereotypes about Immigrants*** by Sánchez et al. (2021).
  
***
# Required packages
- Numpy
- Pandas
- NLTK
- Spacy
- Matplotlib 
- textblob-de
- scikit-learn



***
# Directories and files
## */annotation*
#### */annotated data*
- Contains the annotated samples
#### */samples*
- Contains the samples from the data that were extracted for annotation
#### *Annotationsrichtlinie.pdf*
- Guidelines for annotation
#### *join_annotated_samples.py*
- Script for joining the annotated samples back into one file *data/combined_samples.csv*
#### *split_for_annotation.py*
- Script for extracting the first 500 sentences from *preselection&extraction/extracted_sents.csv* and splitting them into 10 samples

## */data*
#### *combined_samples.csv*
- All final annotated data

## */preselection&extraction*
#### *extract_sents.py*
- Script for extraction and minimal preprocessing of relevant sentences (at least one keyord match)from *raw_sents.json*
#### *extracted_sents.csv*
- All sentences extracted for potential annotation
#### *preselect.py*
- Script for extracting raw sentences from speeches in the corpus containing more than 50 keyword matches 
#### *stichwort-treffer.csv*
- Contains table with filenames of all speeches from 2015-2017 + counts of keyword matches (for us only the filenames were relevant)
#### *stichwortliste.csv*
- keyword list for extracting relevant speeches and sentences

## *InhaltsverzeichnisReportEntwurf.docx*
- Plan and structure for project report

## ***Stereotype classification.ipynb***
- Jupyter notebook with **main code** (preprocessing, feature extraction, training of model and evaluation) as well as the **project report**