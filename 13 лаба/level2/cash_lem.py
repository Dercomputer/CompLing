import sqlite3

with open("../level1/lemandstem/super_lemm.txt", encoding="utf-8") as d:
    text = (d.read()).split()
db = sqlite3.connect("lemmes.db")
cur = db.cursor()


def lemma(text: list):
    for i in range(len(text)):
        cur.execute("INSERT INTO lemm (lemma) VALUES (?) ON CONFLICT(lemma) DO NOTHING", [text[i]])
    db.commit()


lemma(text)
