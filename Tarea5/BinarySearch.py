def binarySearch(data,to_search):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == to_search:
            return mid
        elif data[mid] < to_search:
            left = mid + 1
        else:
            right = mid - 1
    return -1