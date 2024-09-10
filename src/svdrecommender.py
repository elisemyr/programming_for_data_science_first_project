#1.3

import numpy as np
from scipy.linalg import eig

def eigenvalues_computation(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        print("Matrix must be square")

    eigenvalues,eigenvectors = eig(matrix)
    return eigenvalues

from scipy.linalg import svd

def svd_computation(matrix):
    U, s, Vh = svd(matrix)
    return U, s, Vh

