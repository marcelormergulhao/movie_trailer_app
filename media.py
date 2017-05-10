# Class representing a movie, storing the relevant information to our app and
# with a methods to get and use this data.
class Movie():
    # Initialize movie just by setting the instance variables
    def __init__(self, title, poster, trailer, date, main_cast):
        self.title = title
        self.poster = poster
        self.trailer = trailer
        self.date = date
        self.main_cast = main_cast

    # Return movie information in dictionary with standard keys
    def get_info(self):
        return  { "title": self.title,
                  "poster": self.poster,
                  "trailer": self.trailer,
                  "release_date": self.date,
                  "main_cast": self.main_cast}

    #Print Movie information, helpful on debug
    def print_info(self):
        print("Movie:", self.title)
        print("Poster URL", self.poster)
        print("Trailer URL", self.trailer)
        print("Release Year:", self.date)
        print("Cast:")
        for actor in self.main_cast:
            print(actor, "as", self.main_cast[actor])
