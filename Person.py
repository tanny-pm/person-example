from AgeAboveMaximumException import AgeAboveMaximumException
from AgeBelowMinimumException import AgeBelowMinimumException


class Person:
    MINIMUM_AGE = 1
    MAXIMUM_AGE = 200

    def __init__(self, name: str, age: int):
        if age < self.MINIMUM_AGE:
            raise AgeBelowMinimumException()
        if age > self.MAXIMUM_AGE:
            raise AgeAboveMaximumException()
        self.age = age
        self.name = name
