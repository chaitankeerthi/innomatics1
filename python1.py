import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
tags = pd.read_csv('tags.csv')

merged_data = pd.merge(ratings, movies, on='movieId')

movies_to_check = ['Matrix', 'Pulp Fiction', 'Forrest Gump', 'Shawshank Redemption']

for movie in movies_to_check:
    if any(merged_data['title'].str.contains(movie)):
        print(f"{movie} is in the list.")
        

max_rated_movie = merged_data['movieId'].value_counts().idxmax()
max_rated_movie_info = movies[movies['movieId'] == max_rated_movie]

print("Movie with the maximum number of user ratings:")
print(max_rated_movie_info[['title', 'genres']])

matrix_movie = movies[movies['title'] == 'Matrix, The (1999)']


merged_data2 = pd.merge(tags, matrix_movie, on='movieId')

print("Tags submitted by users for 'Matrix, The (1999)':")
print(merged_data2[['userId', 'tag']])


terminator_movie = movies[movies['title'] == 'Terminator 2: Judgment Day (1991)']

merged_data3 = pd.merge(ratings, terminator_movie, on='movieId')

average_rating = merged_data3['rating'].mean()

print(f"Average user rating for 'Terminator 2: Judgment Day (1991)': {average_rating:.2f}")

fight_club_movie = movies[movies['title'] == 'Fight Club (1999)']

merged_data4 = pd.merge(ratings, fight_club_movie, on='movieId')

plt.hist(merged_data4['rating'], bins=[0.5, 1.5, 2.5, 3.5, 4.5, 5.5], edgecolor='black')
plt.title('User Ratings Distribution for "Fight Club (1999)"')
plt.xlabel('Rating')
plt.ylabel('Number of Ratings')
plt.xticks([1, 2, 3, 4, 5])
plt.show()
