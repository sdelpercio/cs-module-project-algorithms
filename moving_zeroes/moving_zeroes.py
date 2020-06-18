'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # if theres no zeroes, just return the list
    if 0 not in arr:
        return arr
    
    # initialize left, right pointers
    left = 0
    right = len(arr) - 1
    
    # loop through array with pointers
    while left < right:
        # if left sees zero and right doesnt
        if arr[left] == 0 and arr[right] != 0:
            # swap, then move inwards
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else:
            # continue if non-zero on left
            if arr[left] != 0:
                left += 1
            # continue if zero on right
            if arr[right] == 0:
                right -= 1
    
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")