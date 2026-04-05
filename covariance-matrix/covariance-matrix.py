import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    try:
        x=np.array(X)
        n,m=x.shape
        print(n,m)
        if x.ndim!=2 or n==1:
            return None
        means=np.mean(x,axis=0,keepdims=True)
        xc=x-means
        mult=np.dot(xc.T,xc)
        return mult/(n-1)
    except:
        return None
    
    