# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
# base case: if the sequence is empty, return a list with the empty string
    if len(sequence) == 0:
        return ['']

    # base case: if the sequence has only one character, return a list with the sequence itself
    if len(sequence) == 1:
        return [sequence]

    # recursive case: for each character in the sequence, create a permutation
    # by inserting the character into every possible position of the remaining permutations
    permutations = []
    for i in range(len(sequence)):
        char = sequence[i]
        remaining_char = sequence[:i]+sequence[i+1:]
        for p in get_permutations(remaining_char):
            permutations.append(char+p)

    


    return permutations


if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input_2 = 'cat'
    print('Input:', example_input_2)
    print('Expected Output:', ['cat', 'cta', 'act', 'atc', 'tac', 'tca'])
    print('Actual Output:', get_permutations(example_input_2))

    example_input = 'a'
    print('Input:', example_input)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'hq'
    print('Input:', example_input)
    print('Expected Output:', ['hq', 'qh'])
    print('Actual Output:', get_permutations(example_input))

    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


