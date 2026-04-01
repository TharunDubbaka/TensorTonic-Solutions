def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    maxval=max(values)
    minval=min(values)
    if minval==maxval:
        return [0]*(len(values))
    # Write code here
    binwidth=(maxval-minval)/num_bins
    res=[]
    for i in range(len(values)):
        res.append(min((values[i]-minval)//binwidth,num_bins-1))
    return res