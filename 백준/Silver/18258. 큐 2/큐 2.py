from collections import deque
import sys

def push(queue, x):
    queue.append(x)

def pop(queue):
    return queue.popleft() if queue else -1

def size(queue):
    return len(queue)

def empty(queue):
    return int(not queue)

def front(queue):
    return queue[0] if queue else -1

def back(queue):
    return queue[-1] if queue else -1

# 명령과 함수를 매핑하는 딕셔너리
commands = {
    'push': push,
    'pop': pop,
    'size': size,
    'empty': empty,
    'front': front,
    'back': back
}

queue = deque()
N = int(input())

for _ in range(N):
    command_line = sys.stdin.readline().split()
    command = command_line[0]
    if command == 'push':
        commands[command](queue, int(command_line[1]))
    else:
        print(commands[command](queue))