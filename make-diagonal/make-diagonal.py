import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    n=len(v)
    mat=np.zeros((n,n))
    row,col=np.diag_indices_from(mat)
    mat[row,col]=v
    return mat
