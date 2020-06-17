'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    
    # loop through array
    for i in range(0, len(arr)):
        # pop off item
        popped = arr.pop(i)
        # if item is still in array, add it back in
        if popped in arr:
            arr.append(popped)
            continue
        # else that is the single item
        else:
            return popped
        
        



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")