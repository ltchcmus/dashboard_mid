import pandas as pd

genre_df = pd.read_csv('data/processed/movie_genres.csv')
movies_df = pd.read_csv('data/processed/movies.csv')
print(movies_df[movies_df['country'] == 'Vietnam'].head())