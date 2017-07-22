import fresh_tomatoes
import media


# Created instance of the class Movie
movie1 = media.Movie("Terminator",
                    "http://img.moviepostershop.com/titanic-movie-poster-1997-1020339699.jpg",
                    "https://www.youtube.com/watch?v=sA4FQfNTvm4")


movie2 = media.Movie("Terminator")

# Create Movie List and add Movies inside
movies = [movie1, movie2]




# Called the method open_movies_page in order to create the movies webpage
fresh_tomatoes.open_movies_page(movies)
    
