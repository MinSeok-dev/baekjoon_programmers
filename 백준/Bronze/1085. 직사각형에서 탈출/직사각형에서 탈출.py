x, y, w, h = map(int, input().split())

xline = min(w-x, x)
yline = min(h-y, y)

print(min(xline, yline))