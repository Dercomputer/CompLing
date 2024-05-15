from pymystem3 import Mystem

with open("../level1/lemandstem/not_stop_words.txt", encoding="utf-8") as d:
    text = d.read()
m = Mystem()
lemmes = m.lemmatize(text)
with open("super_stem.txt", "w", encoding="utf-8") as stop:
    for i in range(len(lemmes)):
        stop.write(lemmes[i])
tic = m.analyze(text)
print(tic)
