def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm(test_cases):
    results = []
    for case in test_cases:
        a, b = case
        results.append(lcm(a, b))
    return results

if __name__ == "__main__":
    T = int(input())
    test_cases = [list(map(int, input().split())) for _ in range(T)]

    result = find_lcm(test_cases)

    for res in result:
        print(res)
