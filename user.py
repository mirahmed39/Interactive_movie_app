from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []
    def __repr__(self):
        return self.name

    #returns a list of watched movies
    def watchedMovies(self):
        return list(filter(lambda x : x.watched, self.movies))

    def addMovie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def deleteMovie(self, name):
        if len(self.movies) == 0:
            print("Sorry you don't have any movies yet.")
        else:
            for movie in self.movies:
                if name == movie.movie_name:
                    self.movies.remove(movie)

    # given a movie name, marks it to watched.
    def setWatched(self, name):
        for movie in self.movies:
            if name == movie.movie_name:
                movie.watched = True

    def json(self):
        return {
            "name": self.name,
            "movies": [ movie.json() for movie in self.movies]
        }
    @classmethod
    def from_json(cls, json_data):
        user = User(json_data["name"])
        movies = []
        for movie_data in json_data["movies"]:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies
        return user
