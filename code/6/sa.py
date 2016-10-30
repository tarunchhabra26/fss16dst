from __future__ import division, print_function
import random
import math

# Set min and max values of energy
max_e = 0
min_e = 0


def compute_energy_bounds(model):
    """
    Computes value of min and max energy bounds in 100 iterations
    :param model: given model instance
    :return: energy values
    """
    global max_e, min_e
    ss = []
    for i in xrange(100):
        ss.append(model.evaluate(model.any()))
    max_e = max(ss)
    min_e = min(ss)


def sa(model):
    """
    Driver method for SA
    :param model: given model instance
    :return: best state
    """
    print("Executing simulated annealing for ", model.name)
    compute_energy_bounds(model)
    sc = model.any()
    ec = model.evaluate(sc)

    print("Initial point = %s and energy = %s" % (str(sc), str(ec)))

    sb = sc
    eb = ec
    k = 1
    kmax = 10000

    while k < kmax and eb > min_e:
        if k == 1 or k % 15 == 0:
            print("\n%d, %f, " % (k, eb), end="")  # Print the evaluation
        sn = neighbour(model, sc)  # Pick some neighbour
        en = model.evaluate(sn)  # Compute its energy
        if en < eb:  # New best found, update best
            sb = sn
            eb = en
            print("!", end="")
        if en < ec:  # Should we just to better?
            sc = sn
            ec = en
            print("+", end="")
        elif probability(ec, en, k / kmax) < random.random():  # Jump to something worse with low probability
            sc = sn
            ec = en
            print("?", end="")
        else:
            print(".", end="")
        k += 1
    print("\n\nBest solution by simulated annealing x = %s with normalized energy = %s ." % (str(sb), str(eb)))
    print
    return sb


def probability(ec, en, t):
    """
    Probability function
    :param ec: current energy
    :param en: next energy
    :param t: temperature ratio
    :return: probability value
    """
    return math.exp((ec - en) / t)


def neighbour(model, s):
    """
    Fucntion to compute neighbor
    :param model: instance of model
    :param s: given state
    :return: neighbour state
    """
    valid, sn = compute_neighbour(model, s)
    while not valid:
        valid, sn = compute_neighbour(model, s)
    return sn


def compute_neighbour(m, s):
    """
    Does the actual computation of neighbour state
    :param m: instance of model
    :param s: given state
    :return: value of neighbor and whether it is valid
    """
    sn = []
    for i in xrange(len(m.decisions)):
        d = m.decisions[i]
        dc = (d.high - d.low) / 10
        if random.randint(0, 1) == 0:
            dn = s[i] - dc
            if dn < m.decisions[i].low:
                dn = m.decisions[i].low
        else:
            dn = s[i] + dc
            if dn > m.decisions[i].high:
                dn = m.decisions[i].high
        sn.append(dn)
    return m.ok(sn), sn
