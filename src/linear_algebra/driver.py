from src.linear_algebra.util import find_the_determinant_value
N = int(input())
matrix_value = []
for _ in range(N):
    row = list(map(float, input().split()))
    matrix_value.append(row)
result = find_the_determinant_value(N, matrix_value)
print(result)
