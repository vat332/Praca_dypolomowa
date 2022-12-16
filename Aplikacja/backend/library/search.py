import gzip
import json
import pandas as pd
from IPython.display import display
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

# print("1\n")
# f = gzip.open("data/goodreads_books.json.gz", "r")
# line = f.readline()
# print("2\n")


def prase_field(lines):
    data = json.loads(lines)
    return {
        "book_id": data["book_id"],
        "title": data["title"],
        "ratings": data["ratings_count"],
        "url": data["url"],
        "cover_image": data["image_url"],
    }


print("3\n")
# Wczytwanie danych za pomoca gzip w celu zmiejszenia poboru ramu
books_titles = []  # Deklaracja listy z ksiazkami
f2 = gzip.open("data/goodreads_books.json.gz", "r")  # Wczytywanie
while True:  # Petla w celu odczytania wszystkich rekordow
    line2 = f2.readline()
    if not line2:
        break
    fields = prase_field(line2)

    try:
        ratings = int(fields["ratings"])
    except ValueError:
        continue
    if ratings > 15:  # Odrzucamy ksiażki z ilością ocen mniejszą od 15
        books_titles.append(fields)
print("4\n")
titles = pd.DataFrame.from_dict(books_titles)  # utworzenia dataframe za pomoca pandasa
titles["ratings"] = pd.to_numeric(titles["ratings"])
# Rozwiazanie problemu z róznymi zapisami tych samych tytułów np Harry Potter i harry potter
print("5\n")
titles["mod_title"] = titles["title"].str.replace("[^a-zA-Z0-9 ]", "", regex=True)

display(titles)
print("6\n")

titles["mod_title"] = titles["mod_title"].str.lower()  # Zmiana tytułów na małe litery
titles["mod_title"] = titles["mod_title"].str.replace(
    r"\s+", " ", regex=True
)  # usuniecie nadmiarowych spacji

display(titles)

titles = titles[titles["mod_title"].str.len() > 0]
titles.to_json("data/books_titles.json")  # zapisanie do json obrobionej bazy

# silnik wyszukiwania
vectorizer2 = TfidfVectorizer()

tfidf = vectorizer2.fit_transform(titles["mod_title"])


def search(query, vectorizer):
    # Usuniecie spacji cyfr duzych liter
    processed = re.sub("[^a-zA-Z0-9 ]", "", query.lower())
    query_vec = vectorizer.transform([processed])
    similarity = cosine_similarity(query_vec, tfidf).flatten()
    indices = np.argpartition(similarity, -10)[-10:]
    results = titles.iloc[indices]
    # sortowanie po ilosc ocen
    results = results.sort_values("ratings", ascending=False)
    # wypisanie 5 rekordow
    return results.head(5)


print(search("Eden of East", vectorizer2))
