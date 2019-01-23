import pandas as pd
cols1 = ['user_id','movie_id','rating']
df1 = pd.read_csv('C:/Users/anupr/Documents/Machine Learning Project/Recommender System/ml-100k/u.data', sep='\t', names=cols1, usecols=range(3), encoding="ISO-8859-1")
#chose first 3 columns - range(3)
#names - used items from list cols1 as column headers
#changed default encoding
            #print(df1.head())
cols2 =['movie_id', 'title']
df2 =  pd.read_csv('C:/Users/anupr/Documents/Machine Learning Project/Recommender System/ml-100k/u.item', sep='|', names=cols2, usecols=range(2), encoding="ISO-8859-1")
            #print(df2.head())

movie_ratings = pd.merge(df1,df2)
print(movie_ratings.head())

# viewing the data user wise instead of movie wise. hence making a pivot table and making all the movies as column
rating_pivot = movie_ratings.pivot_table(index='user_id', columns='title', values='rating')
            #print(rating_pivot.head())
# saving ratings of a movie in a series
movie_argument = rating_pivot['Apollo 13 (1995)']
print(movie_argument.head())

# creating dataframe for similar movies

similar_movies = rating_pivot.corrwith(movie_argument)
similar_movies_df = pd.DataFrame(similar_movies.dropna().sort_values(ascending=False))
            #print(similar_movies_df.head())

#create mean of all the columns grouped by movies
movie_mean = movie_ratings.groupby('title').mean()
            #print(movie_mean.head())

#filtering the dataframe to keep only those movies which is watched by more than 50 people to get more reliable recommendations
movie_mean['size'] = movie_ratings.groupby('title').size()
popular_movies = movie_mean[movie_mean['size']>50]
            #print(popular_movies.head())

#showing average ratings for the dataframe

columns = ['rating']
title_mean_rating = pd.DataFrame(popular_movies, columns = columns)
print(title_mean_rating.head())
correlated_movie = title_mean_rating.join(similar_movies_df).sort_values(by=0, ascending=False)
correlated_movie[0] = correlated_movie[0]*100
correlated_movie.columns = ['Rating','Similarity percentage']

print("Top five recommended movies for you are:")
print(correlated_movie.head())