def solution(array, commands):
    answer = []
    for command in commands:
        shorts = []
        for x in range(command[0]-1, command[1]):
            shorts.append(array[x])
        shorts.sort()
        answer.append(shorts[command[2]-1])
    return answer