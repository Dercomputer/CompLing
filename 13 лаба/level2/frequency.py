import nltk
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

with open("../level1/tokenstasks/txt.txt", encoding="utf-8") as f:
    text = f.read()
tokens = nltk.word_tokenize(text)
tokens = [token for token in tokens if len(token) >= 3]
fd = FreqDist(tokens)
fd.plot(50, cumulative=False)
plt.show()