def gardener_bot(array):
    first_list = []
    columns = len(array[0])
    arr_len = len(array)
    ready_list = []
    for i in range(columns):
        for j in range(arr_len):
            first_list.append(array[j][i])
        if i % 2 == 0:
            first_list.reverse()
        ready_list.extend(first_list)
        first_list = []
    return ready_list
