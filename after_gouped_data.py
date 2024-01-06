import pandas as pd

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

grouped_ratings = ratings.groupby('movieId').agg({'rating': ['count', 'mean']}).reset_index()
grouped_ratings.columns = ['movieId', 'rating_count', 'rating_mean']

merged_data = pd.merge(movies, grouped_ratings, on='movieId', how='inner')


filtered_movies = merged_data[merged_data['rating_count'] > 50]


most_popular_movie = filtered_movies[filtered_movies['rating_mean'] == filtered_movies['rating_mean'].max()]


print("Most Popular Movie based on Average User Ratings:")
print(most_popular_movie[['movieId', 'title', 'genres', 'rating_count', 'rating_mean']])


top5_popular_movies = filtered_movies.sort_values(by='rating_count', ascending=False).head(5)

print("Top 5 Popular Movies based on Number of User Ratings:")
print(top5_popular_movies[['movieId', 'title', 'genres', 'rating_count', 'rating_mean']])


sci_fi_movies = filtered_movies[filtered_movies['genres'].str.contains('Sci-Fi')]


sorted_sci_fi_movies = sci_fi_movies.sort_values(by='rating_count', ascending=False)

third_most_popular_sci_fi_movie = sorted_sci_fi_movies.iloc[2]

print("Third Most Popular Sci-Fi Movie based on Number of User Ratings:")
print(third_most_popular_sci_fi_movie[['movieId', 'title', 'genres', 'rating_count', 'rating_mean']])
