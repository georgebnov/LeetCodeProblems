mat = [[1,2,3], [4,5,6], [7,8,9]]
print(len(mat))
print()

def diagonalSum(mat): #first try
    sum = 0
    if (len(mat) % 2) == 0:
        for i in range(len(mat)):
            if i == len(mat) / 2:
                sum  = mat[i][i] + mat[i][len(mat) - i] + mat[len(mat) - i][i] + mat[len(mat) - i][len(mat) - i]
                return sum
            else:
                sum  = mat[i][i] + mat[i][len(mat) - i] + mat[len(mat) - i][i] + mat[len(mat) - i][len(mat) - i]
    
    else:
        for i in range(len(mat)):
            if i == (len(mat) // 2):
                sum  = mat[i][i]
                return sum
            else:
                sum  = mat[i][i] + mat[i][len(mat) - i] + mat[len(mat) - i][i] + mat[len(mat) - i][len(mat) - i]

print(diagonalSum(mat))


def diagonalSum(mat): #second
    n = len(mat)
    total = 0
    for i in range(n):
        total += mat[i][i]
        total += mat[i][n - 1 - i]
    if n % 2 == 1: 
        total -= mat[n // 2][n // 2]
    return total

mat = [[1,2,3], [4,5,6], [7,8,9]]