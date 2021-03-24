import json

class Fruit():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __eq__(self, other):
        if not isinstance(other, Fruit):
            return NotImplemented

        return self.name == other.name and self.description == other.description
