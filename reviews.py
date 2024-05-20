import pandas as pd

wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

print(wine_reviews)

#group by country
reviews = wine_reviews.groupby(["country"])

#find number of reviews and average points
reviews = reviews.points.agg([len, "mean"])

#round to one decimal
reviews = reviews.round(decimals=1)

#sort countries in descending order
reviews = reviews.sort_values(by="len", ascending=False)

#clean up column names (unsure why I can't get "Country" to capitalize in the output)
reviews = reviews.rename(columns={"country": "Country", "len": "Number of Reviews", "mean": "Average Points"})

#write data to new file
reviews.to_csv("data/reviews-per-country.csv")
