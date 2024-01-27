def isSafe(mat, r, c):
    for i in range(r):
        if mat[i][c] == 'Q':
            return False

    i, j = r, c
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1

    i, j = r, c
    while i >= 0 and j < len(mat):
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1

    return True

def printSolution(mat):
    for i in mat:
        print(" ".join(i))
    print()

def NQueen(mat, r):
    if r == len(mat):
        printSolution(mat)
        return

    for i in range(len(mat)):
        if isSafe(mat, r, i):
            mat[r][i] = 'Q'
            NQueen(mat, r + 1)
            mat[r][i] = '-'

n = int(input("Enter number of queens: "))
mat = [['-' for x in range(n)] for y in range(n)]
print("Solutions are")
NQueen(mat, 0)
