import spacy

with open("../level1/lemandstem/not_stop_words.txt", encoding="utf-8") as d:
    text = d.read()
nlp = spacy.load("ru_core_news_sm")
doc = nlp(text)
with open("spacelem.txt", "w", encoding="utf-8") as sl:
    for token in doc:
        sl.write(token.lemma_)
        sl.write(" ")
with open("spacegram.txt", "w", encoding="utf-8") as sg:
    for token in doc:
        sg.write(token.pos_)
        sg.write(" ")