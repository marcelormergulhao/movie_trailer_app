"""Main file for the Movie Trailer Project proposed as part of Udacity's Full
Web Developer Nanodegree"""
import os
import json
import fresh_tomatoes
from media import Movie

def load_movies_from_file(path):
    """Load movies from file and create the related classes, returning them
    as a list"""
    # Check if provided path exists, including relative folders
    split_path = path.split("/")[:-1]
    check_folder = ""
    for folder in split_path:
        check_folder += folder + "/"
        if not os.path.isdir(check_folder):
            print("""The directory specified do not exist,
                please check the path to the movie file.""")
            #Return empty movie list if failed to load file
            return []

    if os.path.isfile(path):
        # Open file, parse it as json
        with open(path) as movie_file:
            json_object = json.loads(movie_file.read())
            movie_list = []
            for element in json_object:
                movie_list.append(Movie(element["title"], element["poster"],
                                        element["trailer"], element["date"],
                                        element["main_cast"]))
            return movie_list
    else:
        print("There is no file to load movies from, check provided file.")

def movie_catalog():
    """Main catalog function, loads movies and prepare web page with related
    content"""
    movie_list = load_movies_from_file("files/movies.json")
    #If the list isn't empty, try creating the web page
    if movie_list:
        #Create and open movie page
        fresh_tomatoes.open_movies_page(movie_list)
    else:
        print("Movie list is empty, exiting.")

if __name__ == "__main__":
    movie_catalog()
