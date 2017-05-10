class Movie():
    """Class representing a movie, storing the relevant information to our app and
    with a methods to get and use this data."""
    # Initialize movie just by setting the instance variables
    def __init__(self, title, poster, trailer, date, main_cast):
        self.title = title
        self.poster = poster
        self.trailer = trailer
        self.date = date
        self.main_cast = main_cast

    def get_info(self):
        """Return movie information in dictionary with standard keys"""
        return  {"title": self.title,
                 "poster": self.poster,
                 "trailer": self.trailer,
                 "release_date": self.date,
                 "main_cast": self.main_cast}

    def print_info(self):
        """Print Movie information, helpful on debug"""
        print("Movie:", self.title)
        print("Poster URL", self.poster)
        print("Trailer URL", self.trailer)
        print("Release Year:", self.date)
        print("Cast:")
        for actor in self.main_cast:
            print(actor, "as", self.main_cast[actor])
