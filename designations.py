class Subject:
    """Constructor of class. o_type is 0 or 1"""
    def __init__(self, o_type, length, height):
        self.o_type = o_type
        self.length = length
        self.height = height

    """Returns length"""
    def get_length(self):
        return self.length

    """Returns height"""
    def get_height(self):
        return self.height

    """Returns type of object"""
    def get_type(self):
        return self.o_type