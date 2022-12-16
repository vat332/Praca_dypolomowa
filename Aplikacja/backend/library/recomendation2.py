import numpy as np
import pandas as pd
from IPython.display import display
from sklearn.metrics.pairwise import cosine_similarity

# Wczytywanie danych
books = pd.read_csv("dane/Books.csv")
users = pd.read_csv("dane/Users.csv")
ratings = pd.read_csv("dane/Ratings.csv")

# Funkcja do wyświetlania danych
def show(dane, ile) -> None:
    display(dane.head(ile))


# System rekomendacyjny oparty o popularoność
ratings_with_name = ratings.merge(books, on="ISBN")
# W opraciu o ilość
num_rating_df = (
    ratings_with_name.groupby("Book-Title").count()["Book-Rating"].reset_index()
)
num_rating_df.rename(columns={"Book-Rating": "num_ratings"}, inplace=True)

# display(num_rating_df)
# W opraciu o średnią
avg_rating_df = (
    ratings_with_name.groupby("Book-Title").mean()["Book-Rating"].reset_index()
)
avg_rating_df.rename(columns={"Book-Rating": "avg_rating"}, inplace=True)
# display(avg_rating_df)

popular_df = num_rating_df.merge(avg_rating_df, on="Book-Title")
# display(popular_df)

popular_df = popular_df[popular_df["num_ratings"] >= 250].sort_values(
    "avg_rating", ascending=False
)
# display(popular_df)

popular_df = popular_df.merge(books, on="Book-Title").drop_duplicates("Book-Title")[
    ["Book-Title", "Book-Author", "Image-URL-M", "num_ratings", "avg_rating"]
]
# display(popular_df)

# Collaborative filtering
x = ratings_with_name.groupby("User-ID").count()["Book-Rating"] > 200
padhe_likhe_users = x[x].index
# display(padhe_likhe_users)

filtered_rating = ratings_with_name[
    ratings_with_name["User-ID"].isin(padhe_likhe_users)
]

# display(ratings_with_name)

y = filtered_rating.groupby("Book-Title").count()["Book-Rating"] >= 50
famous_books = y[y].index

# display(famous_books)

final_ratings = filtered_rating[filtered_rating["Book-Title"].isin(famous_books)]
# display(final_ratings)

pt = final_ratings.pivot_table(
    index="Book-Title", columns="User-ID", values="Book-Rating"
)
pt.fillna(0, inplace=True)

similarity_scores = cosine_similarity(pt)
# display(similarity_scores)


def recommend(book_name) -> None:
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True
    )[1:6]
    for i in similar_items:
        print(pt.index[i[0]])


recommend("The Da Vinci Code")
# Niby działa
