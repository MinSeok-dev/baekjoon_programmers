from collections import deque

def solution(progresses, speeds):
    working = deque()
    answer = []
    for x, y in zip(progresses, speeds):
        cnt = 0
        while x<100:
            x += y
            cnt += 1
        working.append(cnt)
        
    while working:
        x = working.popleft()
        result = 1
        while len(working) >= 1 and x >= working[0]:
            working.popleft()
            result += 1
        answer.append(result)
    return answer