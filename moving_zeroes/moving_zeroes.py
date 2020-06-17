'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # if theres no zeroes, just return the list
    if 0 not in arr:
        return arr
    
    # otherwise
    else:
        i = 0
        # loop through array
        while i < len(arr):
            # find next item that is non-zero, pop off, insert at beginning
            if arr[i] != 0:
                popped = arr.pop(i)
                arr.insert(0, popped)
                i += 1
            else:
                i += 1
        
        return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")