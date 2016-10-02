from __future__ import division, print_function
from sys import float_info
from random import *


class Decision:                                             #making decisions
    def __init__(self, x1, x2, x3, x4, x5, x6):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.x6 = x6
        self.f1 = f1(self)
        self.f2 = f2(self)




def f1(s):                                                      #building objectives
    return -(25 * (s.x1 - 2) ** 2 + (s.x2 - 2) ** 2 + ((s.x3 - 1) ** 2) * ((s.x4 - 4) ** 2) + (s.x5 - 1) ** 2)


def f2(s):
    return s.x1 ** 2 + s.x2 ** 2 + s.x3 ** 2 + s.x4 ** 2 + s.x5 ** 2 + s.x6 ** 2

def randomx():                                               #getting random value for each decision
    x1 = randint(0, 10)
    x2 = randint(0, 10)
    x3 = randint(1, 5)
    x4 = randint(0, 6)
    x5 = randint(1, 5)
    x6 = randint(0, 10)
    return Decision(x1, x2, x3, x4, x5, x6)

def myscore(f1, f2):
    return f1 + f2



def constraintchk(s):                                          # defining constraints
    g1 = 0 <= s.x1 + s.x2 - 2
    g2 = 0 <= 6 - s.x1 - s.x2
    g3 = 0 <= 2 - s.x2 + s.x1
    g4 = 0 <= 2 - s.x1 + 3 * s.x2
    g5 = 0 <= 4 - (s.x3 - 3) ** 2 - s.x4
    g6 = 0 <= (s.x5 - 3) ** 3 + s.x6 - 4
    return g1 and g2 and g3 and g4 and g5 and g6


def newvalid_x():                                               #function to validate constraints
    while True:
        s = randomx()
        if (constraintchk(s)):
            return s


def eosyczka(f1, f2):                                            #minimizing energyfunction of a state
    return (((f1 + f2) - min) / float((max - min)))



s = newvalid_x()
ebest = 0
max = myscore(f1(s), f2(s))
min = max
for i in xrange(100):
    s = newvalid_x()
    sc = myscore(f1(s), f2(s))
    if (sc > max):
        max = sc
    if (sc < min):
        min = sc
maxtries = 50
maxchanges = 50
thresh = 50
p = 0.5

def newenergy():
    solution = sn
    solution.f1 = f1(s)
    solution.f2 = f2(s)



for i in xrange(maxtries):
    solution = newvalid_x()

    for j in xrange(maxchanges):
        if eosyczka(solution.f1, solution.f2) < thresh:
            sb = solution
            ebest = eosyczka(solution.f1, solution.f2)

        c = randint(1, 6)
        if p < random():                                        #change a random setting in c
            while True:
                if c == 1:
                    solution.x1 = randint(0, 10)
                if c == 2:
                    solution.x2 = randint(0, 10)
                if c == 3:
                    solution.x3 = randint(1, 5)
                if c == 4:
                    solution.x4 = randint(0, 6)
                if c == 5:
                    solution.x5 = randint(1, 5)
                if c == 6:
                    solution.x6 = randint(0, 10)
                if constraintchk(solution):
                    solution.f1 = f1(solution)
                    solution.f2 = f2(solution)
                    newe = eosyczka(solution.f1, solution.f2)
                    if (newe < ebest):
                        print("!", end="")
                        ebest = newe
                        sb = solution
                break
        else:                                                     # change setting in c that minimizes score(solution)
            while True:
                if c == 1:
                    sn = solution
                    for x in xrange(1, 11):
                        sn.x1 = x
                        if constraintchk(sn):
                            newenergy()
                            newe = eosyczka(solution.f1, solution.f2)
                            if (newe < ebest):
                                print("+", end="")
                                ebest = newe
                                sb = solution
                    break
                if c == 2:
                    sn = solution
                    for x in xrange(1, 11):
                        sn.x2 = x
                        if constraintchk(sn):
                            newenergy()
                            newe = eosyczka(solution.f1, solution.f2)
                            if (newe < ebest):
                                print("+", end="")
                                ebest = newe
                                sb = solution
                    break
                if c == 3:
                    sn = solution
                    for x in xrange(1, 6):
                        sn.x3 = x
                        if constraintchk(sn):
                            newenergy()
                            newe = eosyczka(solution.f1, solution.f2)
                            if (newe < ebest):
                                print("+", end="")
                                ebest = newe
                                sb = solution
                    break
                if c == 4:
                    sn = solution
                    for x in xrange(1, 7):
                        sn.x4 = x
                        if constraintchk(sn):
                            newenergy()
                            newe = eosyczka(solution.f1, solution.f2)
                            if (newe < ebest):
                                print("+", end="")
                                ebest = newe
                                sb = solution
                    break
                if c == 5:
                    sn = solution
                    for x in xrange(1, 6):
                        sn.x5 = x
                        if constraintchk(sn):
                            newenergy()
                            newe = eosyczka(solution.f1, solution.f2)
                            if (newe < ebest):
                                print("+", end="")
                                ebest = newe
                                sb = solution
                    break
                if c == 6:
                    sn = solution
                    for x in xrange(1, 11):
                        sn.x6 = x
                        if constraintchk(sn):
                            newenergy()
                            newe = eosyczka(solution.f1, solution.f2)
                            if (newe < ebest):
                                print("+", end="")
                                ebest = newe
                                sb = solution
                    break
        print(".", end="")
    print()


print('Decisions ', sb.x1, sb.x2,  sb.x2,  sb.x2, sb.x2,  sb.x2)

print('Best energy = ', ebest)
