''' Return all permutations of a string '''

def string_permutation(input_string):
    ''' Every character at first position, recurse suffixes '''

    if len(input_string) <= 1:
        return input_string
    permutation_list = []
    for i, character in enumerate(input_string):
        suffix_list = [x for x in string_permutation(input_string[0:i] + input_string[i+1:])]
        for suffix in suffix_list:
            permutation_list.append(character + suffix)
    return permutation_list
