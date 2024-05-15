import spacy

with open("../level1/tokenstasks/txt.txt", encoding="utf-8") as f:
    text = f.read()

nlp = spacy.load("ru_core_news_sm")
doc = nlp(text)
ent = doc.ents
for i in ent:
    print(f"Сущность - {i.text}, её тип -{i.label_}")