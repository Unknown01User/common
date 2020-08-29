a = [10, 27, 42, 36]

def max_value(a):
    max_val = 0;
    for i in range(0, len(a)):
        if a[i] > max_val:
            max_val = a[i]

    print(max_val)
    return max_val


max_value(a)


arr_value = [10, 20, 30, 40]
arr_index = []
arr_with_tuples = []
def enumerate(arr_value):
    for index in range(0, len(arr_value)):
        b = (index, arr_value[index])
        arr_with_tuples.append(b)
    #arr_with_tuples = [(arr_index, arr_value) for index in arr_index for value in arr_value ]
    print(arr_with_tuples)
    return arr_with_tuples


enumerate(arr_value)
