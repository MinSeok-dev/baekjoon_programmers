from collections import deque
import sys

def one(queue, x):
    queue.appendleft(x)
def two(queue, x):
    queue.append(x)
def three(queue):
    return queue.popleft() if queue else -1
def four(queue):
    return queue.pop() if queue else -1
def five(queue):
    return len(queue)
def six(queue):
    return 0 if queue else 1
def seven(queue):
    return queue[0] if queue else -1
def eight(queue):
    return queue[-1] if queue else -1

# 명령과 함수를 매핑하는 딕셔너리
commands = {
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight
}

queue = deque()
N = int(input())

for _ in range(N):
    command_line = sys.stdin.readline().split()
    command = command_line[0]
    if command == '1' or command == '2':
        commands[command](queue, int(command_line[1]))
    else:
        print(commands[command](queue))