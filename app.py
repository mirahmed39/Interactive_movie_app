from movie import Movie
from user import User
import json
import os

def menu():
    #ask the user for their name
    username = input("Please enter your name: ")
    #check if a file exists for a user
    filename = "{}.txt".format(username)
    #if exists, then load their file.
    if file_exists(filename):
        with open(filename, 'r') as file:
            json_data = json.load(file)
        user = User.from_json(json_data)
    else: #create a user
        user = User(username)
    #provide user with list of options
        print("----------------------------")
    choice = input("Enter 'a' to add a movie\n"
                   "'s' to see the list of movies\n"
                   "'w' to set a movie as watched\n"
                   "'d' to delete a movie\n"
                   "'l' to see the list of watched movies\n"
                   "'f' to save\n"
                   "'q' to save and quit\n"
                   )
    print("----------------------------")
    while choice != 'q':
        if choice == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter the movie genre: ")
            user.addMovie(movie_name, movie_genre)
        elif choice == 's':
            for movie in user.movies:
                print("Name: {} || Genre: {} || Watched: {}".format(movie.name, movie.genre, movie.watched))
        elif choice == 'w':
            movie_name = input("Enter the movie name to be set as watched: ")
            user.setWatched(movie_name)
        elif choice == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.deleteMovie(movie_name)
        elif choice == 'l':
            for movie in user.watchedMovies():
                print("Name: {} || Genre: {} || Watched: {}".format(movie.movie_name, movie.genre, movie.watched))
        elif choice == 'f':
            with open(filename, 'w') as file:
                json.dump(user.json(), file)
        print("----------------------------")
        choice = input("Enter 'a' to add a movie\n"
                       "'s' to see the list of movies\n"
                       "'w' to set a movie as watched\n"
                       "'d' to delete a movie\n"
                       "'l' to see the list of watched movies\n"
                       "'f' to save\n"
                       "'q' to quit\n"
                       )
        print("----------------------------")
    print("Thank you!!! Enjoy watching movies.")

def file_exists(filename):
    return os.path.isfile(filename)

menu()