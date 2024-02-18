word = input().lower()
cnt = [0]*26

for char in word:
    if 'a' <= char <= 'z':
        cnt[ord(char) - ord('a')] += 1

max_cnt = max(cnt)

if cnt.count(max_cnt) == 1:
    idx = cnt.index(max_cnt)
    char = chr(idx + ord('a')).upper()
    print(char)
else:
    print('?')