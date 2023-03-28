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

# ----------------------------------------------------------------------------------
# unit tests for forward_sub:
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
