import numpy as np

def pearson_correlation(X):
    mat = np.array(X)
    if mat.ndim != 2 or mat.size < 2:
        return None

        
    n, m = mat.shape 
    mean = np.mean(mat, axis=0, keepdims=True)
    xc = mat - mean
    cov = np.dot(xc.T, xc) / (n - 1)
    std = np.sqrt(np.diag(cov))
    denom = np.outer(std, std)
    corr = np.divide(cov, denom, where=denom != 0)

    return corr