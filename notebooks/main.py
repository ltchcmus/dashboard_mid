import pandas as pd

raw_df = pd.read_csv('data/raw/netflix_movies_detailed_up_to_2025.csv')
genre_df = pd.read_csv('data/processed/movie_genres.csv')
movies_df = pd.read_csv('data/processed/movies.csv')
country_df = pd.read_csv('data/processed/movie_countries.csv')

#the number of rowas and columns in raw dataset
print(f"Raw dataset shape: {raw_df.shape}")

#the number of movies in the dataset
print(f"Number of movies after cleaning: {len(movies_df)}")

# date range of the movies in the dataset
print(f"Date range of movies: {movies_df['date_added'].min()} to {movies_df['date_added'].max()}")

#the number of countries in the dataset
print(f"Number of countries: {country_df['country_name'].nunique()}")

# print(movies_df[movies_df['country'] == 'Vietnam'].head())