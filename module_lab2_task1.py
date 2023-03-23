import numpy as np
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


def read_system_from_file(cls):
    xs = [0]*9
    print(xs)
