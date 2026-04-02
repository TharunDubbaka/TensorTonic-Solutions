import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    arr=np.array(A)
    deter=np.linalg.det(arr)
    if arr.shape[0]!=arr.shape[1] or arr.ndim!=2 or deter==0:
        return None
    else:
        return np.linalg.inv(arr)
        
