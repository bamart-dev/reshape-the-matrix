

def reshape_matrix(nums, r, c):
    elements = len(nums) * len(nums[0])
    is_invalid = r * c != elements

    if is_invalid or elements == 0:
        return nums

    joined = []
    for row in nums:
        joined += row

    result = []

    for i in range(r):
        start = i * c
        end = start + c

        result.append(joined[start:end])

    return result
