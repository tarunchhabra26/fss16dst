import random
import math


class Decision(object):
    def __init__(self, low, high):
        """
        Constructor for decisions having just the low and high value
        :param low: low value
        :param high: high value
        :return: decision instance
        """
        self.low = low
        self.high = high


class Model(object):
    def __init__(self, objectives, constraints, decisions):
        """
        Constructor for model having objectives, constraints and decisions
        :param objectives:
        :param constraints:
        :param decisions:
        :return: model instance
        """
        self.objectives = objectives
        self.constraints = constraints
        self.decisions = decisions

    def evaluate(self, solution, total = 0):
        """
        Evaluates the score for a given solution using all objectives
        :param solution: given solution
        :param total: default to 0
        :return: total score
        """
        for objective in self.objectives:
            total = total + objective(solution)
        return total

    def ok(self, solution):
        """
        Validates if given solutions is as per the constraints
        :param solution: given solution
        :return: True or False based on the contraints
        """
        if self.constraints is not None:
            for constraint in self.constraints:
                if not constraint(solution):
                    return False
        return True

    def any(self):
        """
        Generates a random solution for the given model
        :return: random solutions
        """
        valid = False
        solution = []
        while not valid:
            soln = []
            for dec in self.decisions:
                soln.append(random.randint(dec.low, dec.high))
            valid = self.ok(soln)
            if valid:
                solution = soln
        return solution


class Osyczka2(Model):
    def __init__(self):
        """
        Constructor for Osyczka2 model
        :return: instance of Osyczka2
        """
        self.name = "Osyczka"
        objectives = [ob_os_1, ob_os_2]
        constraints = [con_os_1, con_os_2, con_os_3, con_os_4, con_os_5, con_os_6]
        decisions = [Decision(0, 10), Decision(0, 10), Decision(1, 5), Decision(0, 6), Decision(1, 5), Decision(0, 10)]
        Model.__init__(self, objectives, constraints, decisions)


class Schaffer(Model):
    def __init__(self):
        """
        Constructor for Schaffer model
        :return: instance of Schaffer
        """
        self.name = "Schaffer"
        objectives = [o_sh_1, o_sh_2]
        decisions = [Decision(-10 ** 5, 10 ** 5)]
        Model.__init__(self, objectives, None, decisions)


class Kursawe(Model):
    def __init__(self):
        """
        Constructor for Kursawe model
        :return: instance of Kursawe
        """
        self.name = "Kursawe"
        objectives = [o_ku_1, o_ku_2]
        decisions = [Decision(-5, 5), Decision(-5, 5), Decision(-5, 5)]
        Model.__init__(self, objectives, None, decisions)


"""
Objectives
"""


def o_ku_1(sol):
    total = 0
    for i in xrange(len(sol) - 1):
        value = -10 * math.exp((-0.2 * ((sol[i]) ** 2) + ((sol[i + 1]) ** 2)))
        total += value
    return total


def o_ku_2(sol):
    a = 0.8
    b = 1
    total = 0
    for i in xrange(len(sol)):
        value = (abs(sol[i]) ** a) + (5 * math.sin((sol[i]) ** b))
        total += value
    return total


def o_sh_1(sol):
    return sol[0] ** 2


def o_sh_2(sol):
    return (sol[0] - 2) ** 2


def ob_os_1(sol):
    f1 = -(25 * (sol[0] - 2) ** 2 + (sol[1] - 2) ** 2 + ((sol[2] - 1) * (sol[3] - 4)) ** 2 + (sol[4] - 1) ** 2)
    return f1


def ob_os_2(sol):
    f2 = sol[0] ** 2 + sol[1] ** 2 + sol[2] ** 2 + sol[3] ** 2 + sol[4] ** 2
    return f2


"""
Constraints
"""


def con_os_1(x):
    return 0 <= x[0] + x[1] - 2


def con_os_2(x):
    return 0 <= 6 - x[0] - x[1]


def con_os_3(x):
    return 0 <= 2 - x[1] + x[0]


def con_os_4(x):
    return 0 <= 2 - x[0] + 3 * x[1]


def con_os_5(x):
    return 0 <= 4 - (x[2] - 3) ** 2 - x[3]


def con_os_6(x):
    return 0 <= (x[4] - 3) ** 3 + x[5] - 4
