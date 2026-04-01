def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code here
    rows=len(data)
    cols=len(data[0])
    res=[[0]*(cols) for _ in range(rows)]
    maxarr=[]
    minarr=[]
    
    for col in range(cols):
        maxval=float('-inf')
        minval=float('inf')
        for row in range(rows):
            maxval=max(maxval,data[row][col])
            minval=min(minval,data[row][col])
        maxarr.append(maxval)
        minarr.append(minval)
    colrange=0
    for col in range(cols):
        colrange=maxarr[col]-minarr[col]
        for row in range(rows):
            if colrange==0:
                res[row][col]=0.0
            else:
                res[row][col]=(data[row][col]-minarr[col])/(maxarr[col]-minarr[col])
    return res
            
            