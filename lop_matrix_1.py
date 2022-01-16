class Matrix:
    def __init__(self, n, m, matrix) -> None:
        self.n = n
        self.m = m
        self.matrix = matrix
    def mutil_with_permutation(self):
        res = []
        for i in range(self.n):
            a = []
            for j in range(self.n):
                x = 0
                for k in range(self.m):
                    x += self.matrix[i][k] * self.matrix[j][k]
                a.append(x)
            res.append(a)

        return Matrix(self.n, self.n, res)
    
    def show(self):
        for i in self.matrix:
            for j in i:
                print(j,end=' ')
            print()

t = int(input())
while t>0:
    t -= 1
    n,m = map(int, input().split())
    a = []
    for i in range(n):
        a.append([int(i) for i in input().split()])
    matrix = Matrix(n,m, a)
    res = matrix.mutil_with_permutation()
    res.show()


