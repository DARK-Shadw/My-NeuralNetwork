from matrix import Matrix


a = Matrix(2,3)
b = Matrix(3,2)


a.randomize()
b.randomize()
a.printMatrix()
b.printMatrix()

c = Matrix.multiply(a,b)
c.printMatrix()