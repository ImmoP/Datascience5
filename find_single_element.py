def find_single_element(arr):
    result = 0
    for num in arr:
        result ^= num
    return result
