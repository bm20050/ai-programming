from numeric import *

ALPHA = 0.01
EPSILON = 0.0001
def steepest_ascent(p):
    current = random_init(p)
    values = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        (successor, value_best_of) = best_of(neighbors, p)
        if value_best_of >= values:
            break
        else:
            current = successor
            values = value_best_of
    return (current, values)


def mutants(current, p):
    neighbors = []
    for i in range(0, len(current)):
        neighbors.append(mutate(current, i, DELTA, p))
        neighbors.append(mutate(current, i, -DELTA, p))
    return neighbors


def best_of(neighbors, p):
    all = []
    for i in range(0, len(neighbors)):
        all.append(evaluate(neighbors[i], p))
    best_value = min(all)
    best = neighbors[all.index(min(all))]
    return (best, best_value)


def display_setting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

def gradient(current, p, EPSILON):

    domain = p[1] # 하한과 상한이 있어야 됨
    low = domain[1]
    up = domain[2]
    gradient = []
    for i in range(len(current)):
        value = current[i]
        derivate = current[:i]
        if (low[i] <= value + EPSILON <= up[i]):
            value = value + EPSILON
        derivate.append(value)
        derivate.extend(current[i + 1:])
        gradient.append((evaluate(derivate, p) - value) / EPSILON)
    # 미분은 기울기
    # y = ax + b
    # 점과 직선의 방정식
    pass

def take_step(current, gradient):
    suc = []

    for i in range(len(current)):
        suc.append(current[i] - gradient[i])
    return suc

if __name__ == "__main__":
    p = create_problem("./data/Convex.txt")
    current = random_init(p)
    value = evaluate(current, p)
    while True:
        gradient = gradient(current, p, EPSILON)
        next_p = take_step(current, gradient())
        next_n = evaluate(next_p, p)
        if next_n < value:
            current = next_p
            value= next_n
        else:
            break
    print(current, value)
    # solution, minimum = steepest_ascent(p)
    # describe_problem(p)
    # display_setting()
    # display_result(solution, minimum)