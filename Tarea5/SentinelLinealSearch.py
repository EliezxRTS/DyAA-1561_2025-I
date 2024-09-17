def sentinelLinearSearch (data,to_search):
    n = len(data)
    i = 0
    tmp = to_search
    data = data + [tmp]
    while data[i] != to_search:
        i = i + 1
    if i == n:
        return -1
    else:
        return i