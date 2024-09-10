#1.4

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
from scipy.linalg import solve

def solve_dense(A, b):
    """solves a dense linear system Ax = b."""
    return solve(A, b)

def solve_sparse(A_data,A_indices, A_indptr,b):
    """solves a sparse linear system Ax = b using CSR representation."""
    A_csr= csr_matrix((A_data,A_indices,A_indptr))
    return spsolve(A_csr, b)

