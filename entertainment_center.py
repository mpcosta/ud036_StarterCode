import fresh_tomatoes
import media


# Created instances of the class Movie Manually
titanic = media.Movie("Titanic",
                    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                    "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")


wonder_woman = media.Movie("Wonder Woman",
                    "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                    "https://www.youtube.com/watch?v=5lGoQhFb4NM")


terminator_salvation = media.Movie("Terminator Salvation",
                    "https://upload.wikimedia.org/wikipedia/en/9/95/Terminator-salvation-poster.jpg",
                    "https://www.youtube.com/watch?v=-Czz-TcWCkA")



# Created instances of the class Movie by just providing the movie name

ex_machina = media.Movie("Ex Machina")

the_martian = media.Movie("The Martian")

logan = media.Movie("Logan")



# Create Movie List and add Movies inside
movies = [titanic, wonder_woman, terminator_salvation, ex_machina, the_martian]



# Called the method open_movies_page in order to create the movies webpage
fresh_tomatoes.open_movies_page(movies)
    
