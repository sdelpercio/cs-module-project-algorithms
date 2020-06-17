'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # make start and end vars, new array for maxes
    start = 0
    end = k
    max_nums = []
    
    # while end is less than length of nums - 1
    while end <= len(nums):
        # slice array
        # get max from sliced array
        max_num = max(nums[start:end])
        # add max into new array
        max_nums.append(max_num)
        # increment start and end
        start += 1
        end += 1

    return max_nums

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
