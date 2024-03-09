import math

ja1, mo1 = map(int, input().split())
ja2, mo2 = map(int, input().split())

ja = ja1*mo2 + ja2*mo1
mo = mo1*mo2
gcd = math.gcd(ja, mo)

print(f'{ja//gcd} {mo//gcd}')