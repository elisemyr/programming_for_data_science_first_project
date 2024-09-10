from matrix import DenseMatrix, SparseMatrix

def main():
#1.1
    dense_matrix = DenseMatrix([[1,2, 3], [4, 5,6], [7,8, 9]])
    print("here is a dense matrix:")
    print(dense_matrix)
    print("the shape is:", dense_matrix.shape())


    sparse_matrix_data = [(0,0, 3),(1,2, 4), (2, 2,5)]
    sparse_matrix = SparseMatrix(sparse_matrix_data)
    print("here is a sparse matrix:")
    print(sparse_matrix)
    print("and the shape is:", sparse_matrix.shape())

#1.3

from svdrecommender import eigenvalues_computation, svd_computation
import numpy as np

square_matrix = np.array([[1, 4], [3, 9]])
eigenvalues,eigenvectors = eigenvalues_computation(square_matrix)
print("eigenvalues for the square matrix:",eigenvalues)
print("eigenvectors for the square matrix:", eigenvectors)
print("\n")
non_square_matrix = np.array([[1, 2, 3], [4, 5, 6]])
U, s, Vh = svd_computation(non_square_matrix)
print("U matrix (SVD, non square matrix):", U)
print("\n")
print("singular values (SVD, non square matrix):", s)
print("\n")
print("Vh matrix (SVD, non square matrix):", Vh)

import numpy as np
from linearsolver import solve_dense, solve_sparse

# dense system example
A_dense= np.array([[3, 2], [4, 1]])
b_dense =np.array([5, 2])
x_dense= solve_dense(A_dense, b_dense)
print("solution of the dense system:", x_dense)

# sparse system example (CSR)
A_sparse_data= np.array([3,4, 5])  # non-zero
A_sparse_indices = np.array([0, 1, 2])  # column indices
A_sparse_indptr =np.array([0,1, 2, 3])  # row indices
b_sparse =np.array([5, 6,7])
x_sparse = solve_sparse(A_sparse_data, A_sparse_indices, A_sparse_indptr, b_sparse)
print("solution of the sparse system:", x_sparse)
