def solution(nums):
    answer = 0
    cnt = len(nums)//2
    num = list(set(nums))
    if cnt > len(num):
        answer = len(num)
    else:
        answer = cnt
    return answer