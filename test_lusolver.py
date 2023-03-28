import unittest

import numpy as np

from module_lab2_task1 import LUSolver


class TestLUSolver(unittest.TestCase):
    def test_read_system_from_file(self):
        solver = LUSolver()
        solver.read_system_from_file('problem0.txt')

        # check that matrix A was read correctly
        expected_a = np.array([[2, -1, 3], [-8, 3, -8], [-2, -2, 7]])
        test1 = solver.matrix_a == expected_a
        print(solver.matrix_a)
        print(expected_a)
        print(test1)

        # check that vector b was read correctly
        expected_b = np.array([-5, 20, 3])
        test2 = solver.vector_b == expected_b
        print(solver.vector_b)
        print(expected_b)
        print(test2)

        solver = LUSolver()
        solver.read_system_from_file('problem27.txt')

        # check that matrix A was read correctly
        expected_a = np.array([[5, 2, 8, 3], [5, 3, 13, 6], [15, 11, 51, 26], [10, 5, 27, 21]])
        test1 = solver.matrix_a == expected_a
        print(solver.matrix_a)
        print(expected_a)
        print(test1)

        # check that vector b was read correctly
        expected_b = np.array([101, 159, 621, 386])
        test2 = solver.vector_b == expected_b
        print(solver.vector_b)
        print(expected_b)
        print(test2)

# ----------------------------------------------------------------------------------
    def test1_forward_sub(self):
        solve = LUSolver()
        solve.read_system_from_file('problem27.txt')
        solve.lu_factors()
        solve.forward_sub()

        solve.vector_y == ([101, 58, 28, 42])
        assert all(solve.vector_y) == all([101, 58, 28, 42])

    def test2_forward_sub(self):
        solve = LUSolver()
        solve.read_system_from_file('problem0.txt')
        solve.lu_factors()
        solve.forward_sub()

        solve.vector_y == np.array([-5, 0, -2])
        assert all(solve.vector_y) == all([-5, 0, -2])
# ----------------------------------------------------------------------------------
    def test_lu_factors(self):
        A = LUSolver()
        A.read_system_from_file(file_path='problem27.txt')
        A.lu_factors()

        l = str(A.matrix_l)
        u = str(A.matrix_u)

        assert(u == str(np.array([[5., 2., 8., 3.], [0., 1., 5., 3.], [0., 0., 2., 2.], [0., 0., 0., 6.]])) and l ==
               str(np.array([[1., 0., 0., 0.], [1., 1., 0., 0.], [3., 5., 1., 0.], [2., 1., 3., 1.]])))


    def test_backward_sub(self):
        solver = LUSolver()
        solver.read_system_from_file('problem0.txt')
        solver.lu_factors()
        solver.forward_sub()
        solver.backward_sub()
        assert all(solver.vector_x) == all([-2, 4, 1])

    def test_write_solution_to_file(self):
        solver = LUSolver()
        solver.read_system_from_file('problem0.txt')
        solver.lu_factors()
        solver.forward_sub()
        solver.backward_sub()
        solver.write_solution_to_file("method5_test.txt")
        value_string = np.loadtxt("method5_test.txt")
        assert all(value_string) == all([-2, 4, 1, None])




