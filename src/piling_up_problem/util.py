def piling_up(n, block):
    left = 0
    right = n - 1
    top = max(block[left], block[right])

    while left <= right:
        if block[left] <= top and block[right] <= top:
            if block[left] >= block[right]:
                top = block[left]
                left += 1
            else:
                top = block[right]
                right -= 1
        elif block[left] <= top:
            top = block[left]
            left += 1
        elif block[right] <= top:
            top = block[right]
            right -= 1
        else:
            return "No"
    return "Yes"
def main():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        blocks = list(map(int, input().strip().split()))
        result = piling_up(n, blocks)
        print(result)