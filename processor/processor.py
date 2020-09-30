

def main():
    choice = menu()
    if choice == 1:
        a = matrix()
        b = matrix()
        return add(a, b)
    elif choice == 2:
        a = matrix()
        c = int(input())
        return const(a, c)
    elif choice == 3:
        a = matrix()
        b = matrix()
        return mult(a, b)
    elif choice == 4:
        return transpose()
    elif choice == 5:
        a = matrix()
        print("The result is:")
        return determine(a)
    elif choice == 6:
        a = matrix()
        return invert(a)
    else:
        quit()


def menu():
    print("""
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    return int(input("Your choice: "))


def matrix():
    dims = input("Enter size of matrix: ")
    if len(dims.split()) != 2:
        return "ERROR"
    rows = int(dims.split()[0])
    return [[float(e) for e in input().split()] for i in range(rows)]


def add(one, two):
    if len(one) != len(two) or len(one[0]) != len(two[0]):
        return "ERROR"
    c = [[one[i][j] + two[i][j] for j in range(len(one[0]))] for i in range(len(one))]
    print("The result is:")
    return "\n".join(" ".join(str(e) for e in c[i]) for i in range(len(c)))


def const(mat, con):
    print("The result is:")
    return "\n".join(" ".join(str(e * con) for e in mat[i]) for i in range(len(mat)))


def mult(one, two):
    if len(one[0]) != len(two):
        return "ERROR"
    else:
        c = []
        for i in range(len(one)):
            c.append([])
            for j in range(len(two[0])):
                v = 0
                for k in range(len(two)):
                    v += one[i][k] * two[k][j]
                c[i].append(v)
        print("The result is:")
        return "\n".join(" ".join(str(round(e, 2)) for e in c[i]) for i in range(len(c)))


def transpose():
    print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    choice = int(input())
    mat = matrix()
    print("The result is:")
    if choice == 1:
        return "\n".join(str(e) for e in [" ".join([str(mat[j][i]) for j in range(len(mat))]) for i in range(len(mat))])
    elif choice == 2:
        return "\n".join(" ".join(str(e) for e in g) for g in [[mat[(len(mat) - 1) - j][(len(mat) - 1) - i] for j in range(len(mat))] for i in range(len(mat))])
    elif choice == 3:
        return "\n".join(" ".join(str(e) for e in g[::-1]) for g in mat)
    else:
        return "\n".join(" ".join(str(e) for e in g) for g in reversed(mat))


def dos(mat, con=1):
    pos = 1
    neg = 1
    for i in range(2):
        pos *= mat[i][i]
        neg *= mat[i][1 - i]
    return con * (pos - neg)


def determine(mat):
    size = len(mat)
    cons = []
    matrices = []
    for i in range(size):
        if i % 2 == 0:
            con = mat[0][i]
        else:
            con = mat[0][i] * (-1)
        vas = [k for k in range(size) if k != i]
        matrix = [[mat[j][k] for k in vas] for j in range(1, size)]
        cons.append(con)
        matrices.append(matrix)
    if size > 3:
        return sum(cons[i] * determine(matrices[i]) for i in range(size))
    elif size == 1:
        return mat[0][0]
    elif size == 2:
        return dos(mat)
    else:
        return sum(dos(matrices[i], cons[i]) for i in range(size))

def invert(mat):
    size = len(mat)
    def adjoint(mat):
        adj = []
        for i in range(size):
            adj.append([])
            for g in range(size):
                sgn = (-1) if (i + g) % 2 != 0 else 1
                ras = [k for k in range(size) if k != i]
                cas = [k for k in range(size) if k != g]
                cof = [[mat[j][k] for j in ras] for k in cas]
                adj[i].append(sgn * determine(cof))
        return [[adj[j][i] for j in range(size)] for i in range(size)]
    inv = [[1 / determine(mat) * e for e in g] for g in adjoint(mat)]
    print("The result is:")
    return "\n".join(" ".join(str(e) for e in g) for g in inv)




if __name__ == "__main__":
    while True:
        print(main())