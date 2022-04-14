# solution 1.

import re
from itertools import permutations

def cal(t1, t, t2):
    t1 = int(t1)
    t2 = int(t2)
    if t == '+':
        return t1 + t2
    elif t == '-':
        return t1 - t2
    elif t == '*':
        return t1 * t2

def solution(expression):
    answer = 0

    expression = re.split('([-|+|*])', expression)

    t_input = list(expression)

    operator = {'(': 4, ')': 4}

    for x,y,z in permutations([1,2,3],3):
        operator.update({'*':x,'-':y,'+':z})
        stack_operater = []
        stack_result = []

        for t in t_input:
            # 숫자면 넣는다.
            if '0' <= t <= '999':
                stack_result.append(t)
            # 여는 괄호거나 스택이 비어있거나 스탭탑이 여는 괄호라면 연산자 집어넣기
            elif t == '(' or not len(stack_operater) or stack_operater[-1] == '(':
                stack_operater.append(t)
            # 들어온 연산자가 스택의 연산자보다 우선순위가 높다면 추가하기(낮은 수가 높은 우선순위)
            elif operator[t] < operator[stack_operater[-1]] and t != ')':
                stack_operater.append(t)
            else:
                # 위의 내용에 해당하지 않는다면
                # 스택이 비지않거나 들어온 연산자가 스택의 탑보다 크거나 같을때까지 반복한다.
                while len(stack_operater) and operator[t] >= operator[stack_operater[-1]]:
                    # 닫는 괄호라면 괄호없애고 정지한다.
                    if stack_operater[-1] == '(':
                        stack_operater.pop()
                        break
                    # 위의 조건에 해당하지 않는다면 결과 스택에 추가한다.
                    stack_result.append(stack_operater.pop())
                # 반복이 끝난후 닫는괄호가 아닐때만 연산자스택에 추가하기
                if t != ')':
                    stack_operater.append(t)

        # 남은 연산자를 처리한다.
        while len(stack_operater):
            # 스택이 빌때까지 결과스택에 넣어준다.
            temp = stack_operater.pop()
            if temp != '(':
                stack_result.append(temp)

        # 후위연산 스택을 순회하면서 확인
        for t in stack_result:
            # 숫자라면 임시저장
            if '0' <= t <= '999':
                stack_operater.append(t)
            else:
                # 연산자면 2개를 꺼내서 계산한다.
                t2 = stack_operater.pop()
                t1 = stack_operater.pop()
                stack_operater.append(cal(t1, t, t2))
        answer=max(answer,abs(stack_operater[0]))

    return answer

expression = "50*6-3*2"
print(solution(expression))

# 참고 :
# 1. 구분자 여러개로 string to list  ( https://velog.io/@highgrace/%EA%B5%AC%EB%B6%84%EC%9E%90-%EC%97%AC%EB%9F%AC%EA%B0%9C%EB%A1%9C-string-to-list )
# 2. 계산기 알고리즘 (https://mungto.tistory.com/234)

# solution 2.
from itertools import permutations
def calc(priority, n, expression):
    if n == 2:
        return str(eval(expression))
    if priority[n] == '*':
        res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = (list(permutations(['*','-','+'], 3)))
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer

# solution 3.
import re
from itertools import permutations

def solution(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)

# solution 4.
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)