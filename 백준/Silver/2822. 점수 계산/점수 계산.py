arr = [int(input()) for _ in range(8)]

# 점수와 문제 번호를 같이 저장
arr_with_idx = [(score, idx+1) for idx, score in enumerate(arr)]

# 점수 기준으로 내림차순 정렬
arr_with_idx.sort(reverse=True)

# 상위 5개 뽑기
top5 = arr_with_idx[:5]

# 합 구하기
total_score = sum(score for score, _ in top5)

# 문제 번호만 뽑아서 오름차순 정렬
problem_numbers = sorted(idx for _, idx in top5)

# 출력
print(total_score)
print(*problem_numbers)