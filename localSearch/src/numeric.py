import random

# 간단한 언덕 등반 알고리즘
## 1. 파일을 읽어보자!
## 2. Convex.txt를 사용해서 계산
def create_problem(filename):
    # 1-1. 파일을 읽자
    ini_file = open(filename, 'r')
    # 1-2. 수식과 리스트로 분리
    expression = ini_file.readline().strip()
    var_names = []
    low = []
    up = []

    for line in ini_file.readlines():
        var_names.append(line.split(',')[0])
        low.append(float(line.split(',')[1]))
        up.append(float(line.split(',')[2]))
    ini_file.close()
    domain = [var_names, low, up]
    # 1-3. 리턴
    return (expression, domain)

def random_init(p):
    expression, domain = p
    init = []
    for i in range(0, len(domain[0])):
        init.append(random.uniform(domain[1][i], domain[2][i]))
    return init

def evaluate(state, p):
    num_eval = 0
    expression = p[0]
    var_name = p[1][0]

    for i in range(len(var_name)):
        assignment = var_name[i] + '=' + str(state[i])
    return num_eval

if __name__ == "__main__":
    # 식과 인자를 분리
    p = create_problem('../data/Convex.txt')
    # 식과 인자를 출력
    describe_problem(p)