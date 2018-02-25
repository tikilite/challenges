''' Power Function in python '''

def power_func(int_x, int_y):
    ''' Raise x to the power of y '''

    if int_y == 1:
        return int_x
    else:
        return int_x * power_func(int_x, int_y - 1)
