import sys
from collections import deque

N = int(input())
questack = list(map(int, sys.stdin.readline().split()))
initial_state = list(map(int, sys.stdin.readline().split()))
M = int(input())
input_state = list(map(int, sys.stdin.readline().split()))

answer = deque()

for i in range(N):
    if questack[i] == 0:
        answer.append(initial_state[i])
for i in range(M):
    answer.appendleft(input_state[i])

for i in range(M):
    print(answer.pop() , end = " ")