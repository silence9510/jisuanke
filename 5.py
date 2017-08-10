m,n,t = map(int, input().split())
matrix = []

for i in range(m):
    row = list(map(int,input().split()))
    matrix.append(row)

if t:
    for row in reversed(matrix):
        for col in row:
            print(col, end=' ')
        else:
            print()
else:
    for row in matrix:
        for col in reversed(row):
            print(col, end=' ')
        else:
            print()

# if t:
#     for i in range(m-1, -1, -1):
#         for j in range(n):
#             print(matrix[i][j], end=' ')
#         else:
#             print()
# else:
#     for i in range(n):
#         for j in range(n-1, 0, -1):
#             print(matrix[i][j], end=' ')
#         else:
#             print()