
def binary_search(x: int, nums: list):
    return binary_search_helper(x, nums, 0, len(nums))


def binary_search_helper(key, nums, start, end):
    mid_index = (start + end) // 2
    if start == end:
        return False
    if nums[mid_index] > key:
        return binary_search_helper(key, nums, start, mid_index)
    elif nums[mid_index] < key:
        return binary_search_helper(key, nums, mid_index + 1, end)
    else:
        return mid_index


result = binary_search(7, [2, 3, 4, 7, 8])
print(result)
