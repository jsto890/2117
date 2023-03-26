import numpy as np

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
        n = self.matrix_a.size
        self.matrix_l = np.eye(n)

        self.matrix_u = self.matrix_a

        # Reduce the matrices
        for r in range(0, n-2):
            for i in range(1, n-1):
                for j in range(0, n):
                    self.matrix_u[i][j+r] = self.matrix_u[i][j+r] - (self.matrix_u[i][j+r]/self.matrix_u[i-1][j+r])*self.matrix_u[i-1][j+r]
                    self.matrix_l[i][j+r] = self.matrix_l[i][j+r] - (self.matrix_u[i][j+r]/self.matrix_u[i-1][j+r])*self.matrix_l[i-1][j+r]



