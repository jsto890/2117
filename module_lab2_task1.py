import numpy as np
import math
import zipfile

# additional imports here


class LUSolver(object):
    def __init__(self):
        self.matrix_a = None
        self.matrix_l = None
        self.matrix_u = None
        self.vector_b = None
        self.vector_x = None
        self.vector_y = None

    def read_system_from_file(self, file_path):
        with open(file_path, 'r') as file:
            # read number of unknowns
            n = int(file.readline().strip())

            # read matrix A
            A = []
            for i in range(n):
                row = list(map(float, file.readline().strip().split(',')))
                A.append(row)
            self.matrix_a = np.array(A)

            # read vector b
            b = []
            for i in range(n):
                value = float(file.readline().strip())
                b.append(value)
            self.vector_b = np.array(b)

    def lu_factors(self):
        n = math.sqrt(self.matrix_a.size)
        n = int(n)
        self.matrix_l = np.eye(n)

        self.matrix_u = self.matrix_a

        # Reduce the matrices
        for r in range(1, n):
            m = r
            for i in range(m, n):
                multiplier = self.matrix_u[i][r-1] / self.matrix_u[m-1][r-1]
                self.matrix_l[i][r-1] = multiplier
                for j in range(m-1, n):
                    self.matrix_u[i][j] = self.matrix_u[i][j] - multiplier*self.matrix_u[m-1][j]

        # Tests
        # print(self.matrix_u)
        # print(self.matrix_l)

# For testing
# A = LUSolver()
# A.read_system_from_file(file_path='problem27.txt')
# A.lu_factors()

