def median(pool) :
    ''' Stathistical median to demonstrate.
    >>> median([2,9,9,7,9,2,4,5,8])
    6
    '''

    copy = sorted(pool)
    size = len(pool)
    if size %2 ==1:
        return copy[(size -1)/2]
    else:
        return(copy[size/2 -1] + copy[size/2])/2

if __name__=='__main__':
    import doctest
    doctest.testmod()