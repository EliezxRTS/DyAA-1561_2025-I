def linearSearch (data,to_search):
    n = len(data)
    i = 0
    while i < n and data[i] != to_search:
        i = i + 1
    if i == n:
        return -1
    else:
        return i