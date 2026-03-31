import numpy as np

def normalize_3d(v):
    v = np.asarray(v, dtype=float)
    norms = np.linalg.norm(v, axis=-1, keepdims=True)
    safe_norms = np.where(norms == 0, 1, norms)
    v_hat = v / safe_norms
    
    return v_hat