class Movie:
    def __init__(self, movie_name, genre, watched):
        self.movie_name = movie_name
        self.genre = genre
        self.watched = watched
    def __repr__(self):
        return "Movie Name: " + self.movie_name + " || Genre: " + self.genre
    def json(self):
        return {
            "movie_name" : self.movie_name,
            "genre": self.genre,
            "watched": self.watched
        }
    @classmethod
    def from_json(cls, json_data):
        return Movie(**json_data) # shortcut that uses "named parameters"