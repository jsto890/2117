# Solving all 100 problems

from module_lab2_task1 import *

for i in range(101):
    Solution = LUSolver()
    Solution.read_system_from_file(f"./problems/problem{i}.txt")
    Solution.lu_factors()
    Solution.forward_sub()
    Solution.backward_sub()
    Solution.write_solution_to_file(f"./problems/solution{i}.txt")

