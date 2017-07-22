import urllib2
import webbrowser
import json

class Movie():
    """ This class stores information related to Movies """

    # Initialize the movie constructor with the defined parameters
    def __init__(self, movieTitle, moviePoster = "", movieTrailer = ""):
        self.title = movieTitle
        # If there is not moviePoster or movieTrailer supplied,
        # The program will search and return the closest Movie Info by using movieTitle
        if moviePoster == "" or movieTrailer == "":
            movieInfo = self.getMovieInfo()
            self.title = movieInfo[0]
            self.poster_image_url = movieInfo[1]
            self.trailer_youtube_url = movieInfo[2]
        else:    
            self.poster_image_url = moviePoster
            self.trailer_youtube_url = movieTrailer


    # Method that initializes the trailer of a movie
    def init_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


    # Get Movie Information from the The TMDb API and return an array with the info
    def getMovieInfo(self):
        infoJson = self.getProcessedJson("https://api.themoviedb.org/3/search/movie?api_key=bb4016586720f201b8ac862369b47e87&language=en-US&query="+self.title+"&page=1&include_adult=false")
        #Grab Movie Info (ID + Title + Poster URL)
        movieID = infoJson['results'][0]['id']
        movieTitle = infoJson['results'][0]['title']
        moviePoster = "http://image.tmdb.org/t/p/w185//"+infoJson['results'][0]['poster_path']
        #Grab Movie Trailer
        videoJson = self.getProcessedJson("https://api.themoviedb.org/3/movie/"+str(movieID)+"/videos?api_key=bb4016586720f201b8ac862369b47e87&language=en-US")
        movieTrailer = "https://www.youtube.com/watch?v=" + videoJson['results'][0]['key']
        
        movieInfo = [movieTitle, moviePoster, movieTrailer]
        return movieInfo
    
    
    #Request + Process Json from an URL and Return it
    def getProcessedJson(self, url):
        connection = urllib2.Request(url)
        opener = urllib2.build_opener()
        fileJson = opener.open(connection)
        finalJson = json.loads(fileJson.read())
        return finalJson
