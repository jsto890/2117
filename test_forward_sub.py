import unittest
import numpy as np
from module_lab2_task1 import LUSolver


class TestLUSolver(unittest.TestCase):
    def test1_forward_sub(self):
        solve = LUSolver()

        solve.read_system_from_file('problem27.txt')
        solve.lu_factors()
        solve.forward_sub()
        test1 = solve.vector_y == ([101, 58, 28, 42])
        assert all(solve.vector_y) == all([101, 58, 28, 42])
# ----------------------------------------------------------------------------------
    def test2_forward_sub(self):
        solve = LUSolver()

        solve.read_system_from_file('problem0.txt')
        solve.lu_factors()
        solve.forward_sub()
        test2 = solve.vector_y == np.array([-5, 0, -2])
        assert all(solve.vector_y) == all([-5, 0, -2])
