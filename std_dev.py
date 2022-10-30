# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/30/2022
# Description: Write a class that has two private data members, the person's name and age.
# Write a separate function (not part of the Person class) called std_dev that takes as a
# parameter a list of Person objects and returns the standard deviation of all their ages.

class Person:
    """Represents the standard deviation of a person's age."""

    def __init__(self, name, age):
        self._name = name  # Assigns value to a person's name
        self._age = age  # Assigns value to a person's age

    def get_age(self):
        """Returns the age of a person in the list"""
        return self._age


def std_dev(people_list):
    """Returns the standard deviation of the ages for a list of persons."""
    N = len(people_list)  # N is the size of the population
    mean = 0
    for person in people_list:  # Takes the age of the person and adds it to the total mean
        mean += person.get_age()

    mean = mean / N  # Calculates the mean by the population
    sta_dev = 0

    for person in people_list:
        sta_dev += ((person.get_age() - mean) ** 2)  # Adds to the standard deviation

    sta_dev = sta_dev / N  # Divides the standard deviation by N
    sta_dev = sta_dev ** 0.5  # Takes the square root of the standard deviation

    return sta_dev  # Returns the value


person_one = Person("Kyoungmin", 73)  # Test cases
person_two = Person("Mercedes", 24)
person_three = Person("Beatrice", 48)

person_list = [person_one, person_two, person_three]
answer = std_dev(person_list)

# print("Answer: ", answer)
