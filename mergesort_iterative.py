''' Iterative mergesort '''

def mergesort(input_list):
    ''' Iterative merge sort '''

    split_list = [[x] for x in input_list]
    while len(split_list) > 1:
        result_list = []
        for i in range(len(split_list)/2):
            result_list.append(sort_two(split_list[i*2], split_list[i*2 + 1]))
        if len(split_list) % 2:
            result_list.append(split_list[-1])
        split_list = result_list

    return split_list[0]


def sort_two(left_list, right_list):
    ''' Sort two lists and return single list '''

    i = j = 0
    sorted_list = []
    while i < len(left_list) and j < len(right_list):
        if left_list[i] > right_list[j]:
            sorted_list.append(right_list[j])
            j += 1
        else:
            sorted_list.append(left_list[i])
            i += 1
    sorted_list = sorted_list + left_list[i:]
    sorted_list = sorted_list + right_list[j:]

    return sorted_list
