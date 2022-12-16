import pandas as pd
from IPython.display import display

liked_books = ["4408 ", "31147619", "29983711", "9401317", "9317691", "20494944"]

csv_book_mapping = {}
with open("data/book_id_map.csv", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        csv_id, book_id = line.strip().split(",")
        csv_book_mapping[csv_id] = book_id

overlap_users = set()

with open("data/goodreads_interactions.csv", "r") as f2:
    while True:
        line2 = f2.readline()
        if not line2:
            break
        user_id, csv_id, _, rating, _ = line2.split(",")

        if user_id in overlap_users:
            continue
        try:
            rating = int(rating)
        except ValueError:
            continue

        book_id = csv_book_mapping[csv_id]

        if book_id in liked_books and rating >= 4:
            overlap_users.add(user_id)

rec_lines = []
with open("data/goodreads_interactions.csv", "r") as f3:
    while True:
        line3 = f3.readline()
        if not line3:
            break
        user_id, csv_id, _, rating, _ = line3.split(",")

        if user_id in overlap_users:
            book_id = csv_book_mapping[csv_id]
            rec_lines.append([user_id, book_id, rating])

recs = pd.DataFrame(rec_lines, columns=["user_id", "book_id", "rating"])
recs["book_id"] = recs["book_id"].astype(str)
print("1\n")
display(recs)
top_recs = recs["book_id"].value_counts().head(10)
top_recs = top_recs.index.values

books_titles = pd.read_json("data/books_titles.json")
books_titles["book_id"] = books_titles["book_id"].astype(str)

books_titles[books_titles["book_id"].isin(top_recs)]  # do usuniecia

all_recs = recs["book_id"].value_counts()
all_recs = all_recs.to_frame().reset_index()
print("2\n")
display(all_recs)
all_recs.columns = ["book_id", "book_count"]

all_recs = all_recs.merge(books_titles, how="inner", on="book_id")

display(all_recs)

all_recs["score"] = all_recs["book_count"] * (
    all_recs["book_count"] / all_recs["ratings"]
)
all_recs.sort_values("score", ascending=False).head(10)
print("3\n")
display(all_recs)

popular_recs = all_recs[all_recs["book_count"] > 75].sort_values(
    "score", ascending=False
)
