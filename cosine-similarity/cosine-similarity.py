import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    A=np.array(a)
    Sqr=np.sqrt(np.sum(np.square(A)))
    B=np.array(b)
    Sqr1=np.sqrt(np.sum(np.square(B)))
    print(Sqr)
    print(np.dot(A,B))
    magn=Sqr*Sqr1
    print(Sqr, Sqr1)
    if magn==0:
        return 0
    else:
        ans=(np.dot(A,B))/magn
        return ans