# Recommender-system-using-Python---pandas

Wiki Definition of a recommender system is - A recommender system or a recommendation system is a subclass of information filtering system that seeks to predict the "rating" or "preference" a user would give to an item. 
I have used 100k dataset from movielens in this project. I have extensively used dataframes hence the clear choice of library is pandas. 
This project aims to predict the top five movies users will like based on their preference. I have used item based collaborative filtering because finding the relationship between items is better than finding relationship between people. I have established relationship between movies and based on the correlation, this code will suggest top five movies to consider watching.

Steps:
1. Read .data and .tem files from the dataset and merged to get an uniform dataframe. 
2. Created a pivot table to make all the movies as columns. This way we can see the ratings each user has given to the movies they've watched. 
3. Passed movie name as argument to extract the details for that particular movie and stored in a series. 
4. Created a datafram for similar movies by findig correlation between all the columns and the argument. '
5. Calculated the mean rating and filtered the dataframes with size > 50(Movies watched more than 50 times). This is done on original table.
6. Joined this table with the similarity dataframe. 
7. Sorted by correlation and displyed top five highly correlated movies. 

I have tried to make this code well commented. Hope that helps explain the algorithm. 
