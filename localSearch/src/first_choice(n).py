import numeric
import random

LIMITS = 100


def first_choice(p):
    current = numeric.random_init(p)
    value_distance = numeric.evaluate(current, p)
    i = 0
    while i < LIMITS:
        successor = random_mutant(current, p)
        _value_distance = numeric.evaluate(successor, p)
        if _value_distance < value_distance:
            current = successor
            value_distance = _value_distance
            i = 0
        else:
            i += 1
    return current, value_distance


def random_mutant(current, p):
    DELTA = 0.01
    delta = [-DELTA, DELTA]
    d = random.choice(delta)
    return d

def inversion(current, i, j):
    cur_copy = current[:]
    while i < j:
        cur_copy[i], cur_copy[j] = cur_copy[j], cur_copy[i]
        i += 1
        j -= 1

if __name__ == "__main__":
    p = numeric.create_problem('../data/tsp30.txt')
    solution, minimum = first_choice(p)
    print(solution)
    print(minimum)