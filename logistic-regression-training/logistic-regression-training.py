import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))
def logloss(y, preds):
    y = np.array(y)
    preds = np.array(preds)
    eps = 1e-15
    preds = np.clip(preds, eps, 1 - eps)
    loss = -np.mean(y * np.log(preds) + (1 - y) * np.log(1 - preds))
    return loss

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    w=np.zeros((len(X[0]),))
    b=0.0
    for i in range(steps):
        multi=np.dot(X,w)
        linearcomb=multi+b
        preds=_sigmoid(linearcomb)
        loss=logloss(y,preds)
        wgrads=np.dot(X.T, (preds-y))/len(X)
        bgrads=np.sum(preds-y)/len(X)
        w=w-(lr*wgrads)
        b=b-(lr*(bgrads))
    return w,b