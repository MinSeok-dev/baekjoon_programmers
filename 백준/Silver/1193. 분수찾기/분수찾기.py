num = int(input())

line = 1
while num>line:
    num -= line
    line += 1
if line%2==0:
    denominator = (line-num+1)
    numerator = num
else:
    denominator = num
    numerator = (line-num+1)
print(numerator, '/', denominator, sep='')