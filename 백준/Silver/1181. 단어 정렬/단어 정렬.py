n = int(input()) 
words = [input().strip() for _ in range(n)]

unique_words = list(set(words))
unique_words.sort(key=lambda x: (len(x), x))


for word in unique_words:
    print(word)