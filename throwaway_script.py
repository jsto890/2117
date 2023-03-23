"""import numpy as np
import os

from module_lab2_task1 import LUSolver


class LUSolver(object):
    def __init__(self):
        self.matrix_a = None
        self.matrix_l = None
        self.matrix_u = None
        self.vector_b = None
        self.vector_y = None
        self.vector_x = None

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


    solver = LUSolver()
    folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', '2117', '2117', 'problems')
    solver.read_system_from_file(folder_path, 'problem0.txt')
    print("Matrix A:")
    print(solver.matrix_a)
    print("Vector b:")
    print(solver.vector_b)
"""