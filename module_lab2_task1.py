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
        """
        Read a linear system of equations from a text file and store the matrix A and vector b.

        Args:
            file_path (str): Path to the text file.

        Return:
            None
            """
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
        """
        This method reduces the l and u matrices using gaussian elimination.

        Arguments
        _________
        No arguments.

        Returns
        _______
        No returns.

        Notes
        _____
        Note this method creates the l and u matrices and then solves for their particular uses,
        so it makes sense there are no inputs or outputs.
        """

        # define the size of the input matrix A
        n = math.sqrt(self.matrix_a.size)
        # Turn value into an integer
        n = int(n)
        # Create the identity matrix of the same size as matrix A
        self.matrix_l = np.eye(n)

        # Set the U matrix as a copy of the matrix A
        self.matrix_u = self.matrix_a

        # Reduce the matrix using gaussian elimination
        for r in range(1, n):
            m = r
            for i in range(m, n):
                multiplier = self.matrix_u[i][r - 1] / self.matrix_u[m - 1][r - 1]
                self.matrix_l[i][r - 1] = multiplier
                for j in range(m - 1, n):
                    self.matrix_u[i][j] = self.matrix_u[i][j] - multiplier * self.matrix_u[m - 1][j]

        # Tests
        # print(self.matrix_u)
        # print(self.matrix_l)

    def forward_sub(self):
        """
        method 1.3, forward_sub will use forward substitution to solve each line of vector_y
        using each line of matrix_l. It will then update vector_y with the results.

        Arguments:
            No arguments

        Returns:
            no returns
        """
        # copying over the values from vector_b into vector_y, without later changing vector_b
        self.vector_y = np.copy(self.vector_b)
        # finding the length/how many values are in vector_b
        n = len(self.vector_b)

        # initialising some indexing values to 0.
        i = 0
        k = 0
        s = 0

        # calculating what vector_y should equal to in each row.
        while i < n:
            while k < i:
                m = (self.matrix_l[i][k])
                s = m * self.vector_y[k] + s
                # increase k
                k = k + 1
            # change vector_b values in vector_y, row i, into final vector_y values
            self.vector_y[i] = self.vector_y[i] - s

            # resetting all values to zero before repeating the loop
            s = 0
            k = 0
            # increase i
            i = i + 1

    def backward_sub(self):
        """
        Completes the backwards substitution to find vector x from the U matrix factor and the vector b
        """
        # computes x
        self.vector_x = np.linalg.tensorsolve(self.matrix_u, self.vector_y)

    def write_solution_to_file(self, file_path):
        """
        Writes the x vector solution to a file

        Arguments
        ---------
        file_path : str
            Path to the file to write the solution in
        """
        with open(file_path, 'w') as fp:
            # Determine number of solutions
            n = len(self.vector_x)
            # Copy the vector into the test file, one line at a time
            for i in range(n):
                value = str(self.vector_x[i])
                fp.write(value + '\n')

# For testing
# A = LUSolver()
# A.read_system_from_file(file_path='problem27.txt')
# A.lu_factors()
# print(A.matrix_u)
# print(A.matrix_l)
