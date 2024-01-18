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
