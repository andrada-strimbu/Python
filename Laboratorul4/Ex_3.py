class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

    def get(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.m:
            return self.matrix[i][j]
        else:
            raise IndexError("INDEXUL DEPASESTE DIMENSIUNEA MATRICEI")

    def set(self, i, j, value):
        if 0 <= i < self.n and 0 <= j < self.m:
            self.matrix[i][j] = value
        else:
            raise IndexError("INDEXUL DEPASESTE DIMENSIUNEA MATRICEI")

    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.set(j, i, self.get(i, j))

        return transposed

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("NU SUNT COMPATIBILE")

        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                element = sum(self.get(i, k) * other.get(k, j) for k in range(self.m))
                result.set(i, j, element)

        return result

    def apply_function(self, function):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i, j, function(self.get(i, j)))

    def iterate(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.matrix[i][j], end=" ")
            print()
                #yield i, j, self.get(i, j)

    # def __str__(self):
    #     return "\n".join(" ".join(str(self.get(i, j)) for j in range(self.m)) for i in range(self.n))


def main():
    matrix1 = Matrix(2, 3)
    matrix2 = Matrix(3, 2)

    matrix1.set(0, 0, 1)
    matrix1.set(0, 1, 2)
    matrix1.set(0, 2, 3)
    matrix1.set(1, 0, 4)
    matrix1.set(1, 1, 5)
    matrix1.set(1, 2, 6)

    matrix2.set(0, 0, 7)
    matrix2.set(0, 1, 8)
    matrix2.set(1, 0, 9)
    matrix2.set(1, 1, 10)
    matrix2.set(2, 0, 11)
    matrix2.set(2, 1, 12)

    print("Matrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    result = matrix1.multiply(matrix2)

    print("\nMatrix 1 * Matrix 2:")
    print(result)

    result.transpose()
    print("\nTranspose of the result:")
    print(result)

    result.apply_function(lambda x: x * 2)
    print("\nMatrix after applying a transformation:")
    print(result)

    print("\nIterating through elements:")
    result.iterate()
    #for i, j, value in result.iterate():
       # print(f"Element at ({i}, {j}): {value}")


main()
