# Movie recomendation engine
This project is aimed at utilizing NLP in python to develop content based movie recomendation engine.
As source of movies i used https://www.kaggle.com/tmdb/tmdb-movie-metadata . Engine creates similarity matrix based on cast, director and short text overview of the movie,
then it returns 5 most similar movies to the one you input. At the end i also created sqlite3 database file with all movies with their recomendations.
