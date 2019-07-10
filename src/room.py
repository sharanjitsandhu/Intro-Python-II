# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.e_to = None
        self.w_to = None
        self.n_to = None
        self.s_to = None

    def getRoomsDirection(self, direction):
        if direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        elif direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        else:
            return None
