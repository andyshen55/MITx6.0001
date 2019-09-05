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
    results = []
    #base case is a one char string
    if len(sequence) <= 1:
        return sequence

    #expected permutations is n!, so for every n-depth position, recurse with size n-1    
    for letter in sequence:
        #for every letter, reduce the problem by recursing on the sequence with the letter removed
        results += [letter + perm for perm in get_permutations(sequence.replace(letter, ''))]
    return results

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    #test1 
    test_input1 = 'abc'
    print('Input:', test_input1)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(test_input1))
    print(len(get_permutations(test_input1)))

    #test2
    test_input2 = 'BUST'
    print('Input:', test_input2)
    print('Expected Output:', "BUST UBST SBUT BSUT USBT SUBT TUBS UTBS BTUS TBUS UBTS BUTS BSTU SBTU TBSU BTSU STBU TSBU TSUB STUB UTSB TUSB SUTB USTB".split())
    print('Actual Output:', get_permutations(test_input2))
    print(len(get_permutations(test_input2)))

    #test3 
    test_input3 = 'xy'
    print('Input:', test_input1)
    print('Expected Output:', ['xy', 'yx'])
    print('Actual Output:', get_permutations(test_input3))
    print(len(get_permutations(test_input3)))
