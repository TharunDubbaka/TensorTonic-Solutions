import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    sum=0
    a=np.array(x)
    b=np.array(y)
    return float(np.sum(np.abs(a-b)))