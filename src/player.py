# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, start_location):
        self.location = start_location

    def change_location(self, new_location):
        self.location = new_location

    def __repr__(self):
        return "Current Location: {}".format(self.location)

    def __str__(self):
        return "Current Location: {}".format(self.location)

        # player has one attribute i.e. location
