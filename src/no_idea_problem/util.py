def calculate_happiness(n, m, arr, a, b):
    happiness = 0
    for num in arr:
        if num in a:
            happiness += 1
        elif num in b:
            happiness -= 1
    return happiness
def main():

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))

    happiness = calculate_happiness(n, m, arr, a, b)
    print(happiness)