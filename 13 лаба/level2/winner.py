from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


def clean_text(text: str):
    clean_text = "".join(el for el in text if el.isalpha() or el.isspace())
    return clean_text


def not_stop_words(clean: str):
    clean = clean_text(clean)
    tokens = word_tokenize(clean)
    stop_words = stopwords.words("russian")
    texts = [[(el for el in tokens if el.lower() not in stop_words)]]
    return texts


with open("../level1/tokenstasks/txt.txt", encoding="utf-8") as f:
    text = f.read()
with open("text1.txt", encoding="utf-8") as ff:
    text1 = ff.read()
with open("text2.txt", encoding="utf-8") as ff:
    text2 = ff.read()
d1 = not_stop_words(text)
d2 = not_stop_words(text1)
d3 = not_stop_words(text2)
tf = TfidfVectorizer()
tfm1 = tf.fit_transform(d1)
tfm2 = tf.fit_transform(d2)
tfm3 = tf.fit_transform(d3)
feature_names1 = tf.get_feature_names_out(d1)
feature_names2 = tf.get_feature_names_out(d2)
feature_names3 = tf.get_feature_names_out(d3)
tfidf_scores1 = tfm1.toarray()[0]
tfidf_scores2 = tfm2.toarray()[0]
tfidf_scores3 = tfm2.toarray()[0]
sort_keyword_d1 = [word for _, word in sorted(zip(tfidf_scores1, feature_names1), reverse=True)]
sort_keyword_d2 = [word for _, word in sorted(zip(tfidf_scores2, feature_names2), reverse=True)]
sort_keyword_d3 = [word for _, word in sorted(zip(tfidf_scores3, feature_names3), reverse=True)]
print(sort_keyword_d1)