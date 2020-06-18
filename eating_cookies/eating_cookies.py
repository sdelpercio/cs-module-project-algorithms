'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # base cases
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2
    # if no cache, create one
    if cache is None:
        cache = [0 for i in range(n + 1)]
    # recursive cases with cache
    
    if cache[n]:
        return cache[n]
        
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    return cache[n]
        
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
