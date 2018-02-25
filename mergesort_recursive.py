''' Recursive mergesort '''

def mergesort(input_list):
    ''' Split list '''

    if len(input_list) <= 1:
        return input_list
    left_list = mergesort(input_list[::2])
    right_list = mergesort(input_list[1::2])
    return mergelists(left_list, right_list)

def mergelists(left_list, right_list):
    ''' Merge lists '''

    if not left_list or not right_list:
        return left_list + right_list
    if left_list[0] < right_list[0]:
        return [left_list[0]] + mergelists(left_list[1:], right_list)
    return [right_list[0]] + mergelists(left_list, right_list[1:])
