def insertion_sort(data):
    n = len(data)
    print("Inicio", data)
    for pivote in range(1, n, 1):
        x= pivote
        while data[x] <= data[x-1] and x>0:
            tmp = data[x]
            data[x]= data[x-1]
            data[x-1] = tmp
            x -= 1
    return data

def binary_insertion_sort(data):
    n = len(data)
    print("Inicio", data)
    for pivote in range(1, n):
        current_value = data[pivote]
        start, end = 0, pivote
        while start < end:
            mid = (start + end) // 2
            if data[mid] < current_value:
                start = mid + 1
            else:
                end = mid
        for j in range(pivote, start, -1):
            data[j] = data[j-1]
        data[start] = current_value
    return data


info1 = [34, 8, 64, 51, 32, 21] #[5,8,9,6,3]
info2 = [34, 8, 64, 51, 32, 21]

print("Final", insertion_sort(info1))

print("Final:", binary_insertion_sort(info2))