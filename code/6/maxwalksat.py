from __future__ import division, print_function
from random import *

RANGES = [(0, 10), (0, 10), (1, 5), (0, 6), (1, 5), (0, 10)]


def mws(m):
    """
    Driver method for MaxWalkSat
    :param m: instance of model
    :return: None
    """
    print("Running max walk sat for ", m.name)
    tries = 15;
    changes = 75;
    p = 0.5
    best = m.any()
    for i in xrange(tries):
        current = m.any()
        for j in xrange(changes):
            if m.evaluate(current) < m.evaluate(best):
                say("!")
                best = current[:]
            if p < random():
                prev = current[:]
                current = mutate_any(m, current)
            else:
                prev = current[:]
                current = mutate_x(m, current)
            if m.evaluate(current) < m.evaluate(best):
                say("!")
                best = current[:]
            elif m.evaluate(current) < m.evaluate(prev):
                say("+")
            else:
                say(".")
        print(", ", round(m.evaluate(best), 5))
    print("#iterations:", tries)
    print("best solution:", best)
    print("best score:", m.evaluate(best))


def mutate_any(m, x):
    """
    Mutate a decision for a problem
    :param m: instance of model
    :param x: decision
    :return: mutated decision
    """
    i = randint(0, len(x) - 1)
    x[i] = randint(RANGES[i][0], RANGES[i][1])
    while not m.ok(x):
        x[i] = randint(RANGES[i][0], RANGES[i][1])
    return x


def mutate_x(m, x):

    def mutate_ith(x, i):
        """
        Mutate ith decision
        :param x: decision
        :param i: ith index
        :return: murated decision
        """
        xi = x[i]
        delta = (RANGES[i][1] - RANGES[i][0]) / 10
        if random() < 0.5:
            xi = max(xi - delta, RANGES[i][0])
        else:
            xi = min(xi + delta, RANGES[i][1])
        return xi

    for i in xrange(len(x)):
        x[i] = mutate_ith(x, i)
        while not m.ok(x):
            x[i] = mutate_ith(x, i)
    return x


def say(x):
    print(x, end="")
