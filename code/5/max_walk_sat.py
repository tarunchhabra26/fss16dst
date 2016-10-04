"""
MaxWalkSat implementation
"""

from __future__ import division
import random

__author__ = "Tarun Chhabra"


class MaxWalkSat:
    """
    Class containing all the methods to run MaxWalkSat
    """
    bounds = (
        (0, 10),
        (0, 10),
        (1, 5),
        (1, 5),
        (0, 6),
        (0, 10)
    )  # All the intial bounds
    constraints = [
        lambda x: all([0 <= (x[0] + x[1] - 2),
                       0 <= (6 - x[0] - x[1]),
                       0 <= (2 - x[1] + x[0]),
                       0 <= (2 - x[0] + 3 * x[1])]),

        lambda x: 0 <= (4 - (x[0] - 3) ** 2 - x[1]),
        lambda x: 0 <= ((x[0] - 3) ** 3 + x[1] - 4)
    ]  # Constraints for Osyczka2 model

    def __init__(self):
        """
        Default constructor
        :return: None
        """
        pass

    def get_functions(self, x):
        """
        Contains the function for the given model
        :param x: The value of list x
        :return: Functions f1 and f2
        """
        f1 = -1 * (
            25 * (x[0] - 2) ** 2 +
            (x[1] - 2) ** 2 +
            ((x[2] - 1) ** 2) * ((x[3] - 4) ** 2) +
            (x[4] - 1) ** 2
        )
        f2 = sum([i ** 2 for i in x])
        return f1, f2

    def get_score(self, x, functions=None):
        """
        Evaluates the score of the function or values
        :param x:
        :param functions:
        :return: The evaluated score
        """
        if functions is None:
            f1, f2 = self.get_functions(x)
            return f1 + f2
        else:
            return x[0] + x[1]

    def generate_decisions(self, b_list, constraint_lst, retries=100):
        """
        Generates random decisions
        :param b_list: List of bounds
        :param constraint_lst: List of constrainsts
        :param retries: Default value of retries set to 100
        :return: None if no value is found else returns list of possible values (as per bound)
        """
        if retries < 0:
            print retries
            return None
        bound1, bound2 = b_list
        value1 = random.uniform(bound1[0], bound1[1])
        value2 = random.uniform(bound2[0], bound2[1])
        if not constraint_lst((value1, value2)):
            return self.generate_decisions(b_list, constraint_lst, retries - 1)
        return [value1, value2]

    def generate_solutions(self,bounds):
        """
        Generates solutions based on decisions and constraints
        :return: None if length of solutions is not correct else returns the solutions
        """
        solutions = []
        for i in range(3):
            solutions.extend(self.generate_decisions([self.bounds[i * 2], self.bounds[i * 2 + 1]], self.constraints[i]))

        if len(solutions) == 6:
            return solutions
        else:
            return None

    def mutate_solutions(self, x):
        """
        Mutates the solutions with a probability of 10%
        :param x: Values of x
        :return: New mutated solutions
        """
        global bounds
        probability = 0.1
        mutated_bounds = []
        for i in xrange(6):
            less = min(x[i] - probability * self.bounds[i][0], self.bounds[i][0])
            more = max(x[i] + probability * self.bounds[i][0], self.bounds[i][0])
            new_bound = (less, more)
            mutated_bounds.append(new_bound)
        return self.generate_solutions(mutated_bounds)

    def mws_optimizer(self, max_tries=20, max_changes=60):
        """
        The optimizer driver method
        :param max_tries: Maximum number of tries to get to the right answer
        :param max_changes: Maximum number of changes to the solution
        :return:
        """
        optimum_solution = self.get_score(self.generate_solutions(self.bounds))
        probability = 0.5
        threshold = -100
        print "MaxWalkSat by : %s for Osyczka2 model" % __author__
        for i in xrange(max_tries):
            solution = self.generate_solutions(self.bounds)
            print "?",
            for j in xrange(max_changes):
                new_sol = self.get_score(solution)
                if new_sol < threshold and new_sol < optimum_solution:
                    optimum_solution = new_sol
                    print "!",
                else:
                    print ".",

                random_index = random.randint(0, 2)
                if probability < random.random():
                    decision = self.generate_decisions(
                        [self.bounds[random_index * 2], self.bounds[random_index * 2 + 1]],
                        self.constraints[random_index])
                    solution[2 * random_index] = decision[0]
                    solution[2 * random_index + 1] = decision[1]
                else:
                    mutant = self.mutate_solutions(solution)
                    if self.get_score(mutant, 1) > self.get_score(solution, 1):
                        print "+",
                    solution = mutant
            print ""
        return optimum_solution


optimizer = MaxWalkSat()
print "The optimum solution found : %f " % optimizer.mws_optimizer()

