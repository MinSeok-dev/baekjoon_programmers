a = input()
cnt = 0
for i in range(len(a)):
    if a[i] in ["a", "e", "i", "o", "u"]:
        cnt += 1
    
print(cnt)