''' Iterative bubble sort '''

def bubblesort(input_list):
    ''' Iterative bubble sort '''

    ordered = False
    while not ordered:
        ordered = True
        for i in range(len(input_list) - 1):
            if input_list[i+1] < input_list[i]:
                ordered = False
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
    return input_list
