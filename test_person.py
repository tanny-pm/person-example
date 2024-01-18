import pytest

from AgeAboveMaximumException import AgeAboveMaximumException
from AgeBelowMinimumException import AgeBelowMinimumException
from Person import Person

person_name: str = "Bob"
person_age: int = 21


def test_create_person_with_name_and_age():
    person = Person(person_name, person_age)
    assert person.name == person_name
    assert person.age == person_age


def test_constants():
    assert Person.MINIMUM_AGE == 1
    assert Person.MAXIMUM_AGE == 200


def test_constructor_throw_exception_when_age_below_minimum():
    with pytest.raises(AgeBelowMinimumException):
        Person(person_name, Person.MINIMUM_AGE - 1)


def test_constructor_throw_exception_when_age_above_maximum():
    with pytest.raises(AgeAboveMaximumException):
        Person(person_name, Person.MAXIMUM_AGE + 1)
