import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    sumval=0
    n=len(A)
    m=len(A[0])
    for i in range(n):
        for j in range(m):
            if i==j:
                sumval+=A[i][j]
    return sumval