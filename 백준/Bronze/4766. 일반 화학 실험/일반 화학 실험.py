pre = None
while True:
    c = float(input())
    if abs(c - 999) < 1e-6:
        break
    if pre is None:
        pre = c
        continue
    print(f"{c - pre:.2f}")
    pre = c
    
    