class Person:
    MINIMUM_AGE = 1
    MAXIMUM_AGE = 200

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
