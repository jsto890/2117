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
