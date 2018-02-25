''' Recursive bubble sort '''

def bubblesort(input_list, ordered=False):
    ''' Recursive bubble sort '''

    if ordered:
        return input_list
    ordered = True
    for i in range(len(input_list) - 1):
        if input_list[i+1] < input_list[i]:
            ordered = False
            input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
    return bubblesort(input_list, ordered)
