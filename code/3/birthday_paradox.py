#!/bin/python

"""
1. Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list.

2. If there are 23 students in your class, what are the chances that two of you have the same
birthday? You can estimate this probability by generating random samples of 23 birthdays and
checking for matches.
"""
from __future__ import division
import random

__author__ = "Tarun Chhabra"
__copyright__ = "Copyright 2016"
__license__ = "MIT"
__version__ = "2.0"
__maintainer__ = "Tarun Chhabra"
__status__ = "Development"


def has_duplicates(input_list):
    """
    Method to check if a given collection has duplicate values
    :rtype: bool
    :param input_list: A list of values
    :return: returns True if there are any duplicate elements
    """
    if input_list is None:
        return False
    unique = set(input_list)
    if len(unique) == len(input_list):
        return False
    return True


def generate_random(n, max_range):
    """
    Generate n random numbers for a given range
    :rtype: list
    :param n: Length of random numbers
    :param max_range: The maximum value of the integer
    :return: A list of random numbers
    """
    if type(n) is not int or type(max_range) is not int:
        return None
    output = []
    for i in range(n):
        number = random.randint(1, max_range)
        output.append(number)
    return output


def count_positives(students, simulations):
    """
    Generate simulations of students and count how many of them have at least one pair of students with the
    same birthday.
    :rtype: int
    :param students:
    :param simulations:
    :return: Number of positive matches
    """
    positives = 0
    for i in range(simulations):
        random_inputs = generate_random(students, 365)
        if has_duplicates(random_inputs):
            positives += 1
    return positives


# Run the simulations and calculate the probability
students = 50
simulations = 10000
positives = count_positives(students, simulations)

print 'Number of simulations : %d' % simulations
print 'Number of positive matches : %d' % positives
print 'Probability : %3.2f ' % ((positives / simulations) * 100)

