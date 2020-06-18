'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # initialize dictionary
    singles_only = {}
    
    # loop through array
    for i in arr:
        # if number is duplicate, delete
        if i in singles_only:
            del singles_only[i]
        
        # else add to dictionary
        else:
            singles_only[i] = 1
        
    return next(iter(singles_only))


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")