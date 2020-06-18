'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# initial solve
# def sliding_window_max(nums, k):
#     # make start and end vars, new array for maxes
#     start = 0
#     end = k
#     max_nums = []
    
#     # while end is less than length of nums - 1
#     while end <= len(nums):
#         # slice array
#         # get max from sliced array
#         max_num = max(nums[start:end])
#         # add max into new array
#         max_nums.append(max_num)
#         # increment start and end
#         start += 1
#         end += 1

#     return max_nums

# improved solve
def sliding_window_max(nums, k):
    # make start and end vars, new array for maxes
    left = 0
    right = k
    max_nums = []
    window = nums[0:right]
    current_max = max(window)
    max_nums.append(current_max)
    
    # while end is less than length of nums - 1
    while right != len(nums):
        remove = nums[left]
        add = nums[right]
        
        # if new number is max, and prev number is not
        if add > current_max:
            current_max = add
        
        # if prev number was max, and new number isnt
        elif current_max == remove:
            current_max = max(nums[left+1:right+1])
        # add onto window, remove first item
        max_nums.append(current_max)
        # increment left, right
        left += 1
        right += 1

    return max_nums

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
