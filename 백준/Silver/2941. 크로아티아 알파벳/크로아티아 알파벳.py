word = input()

croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
index = 0

while index < len(word):
    # 크로아티아 알파벳인지 확인
    found = False
    for croatian in croatian_alphabets:
        if word[index:index+len(croatian)] == croatian:
            count += 1
            index += len(croatian)
            found = True
            break

    # 크로아티아 알파벳이 아니면 한 글자씩 세기
    if not found:
        count += 1
        index += 1

print(count)