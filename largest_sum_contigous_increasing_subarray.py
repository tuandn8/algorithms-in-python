# Write an efficient program to find the sum of contiguous subarray
# within a one-dimensional array of numbers which has the largest sum.


def max_subarray_sum(arr):
    max_sum = arr[0]
    cur_max = arr[0]

    for i in range(1, len(arr)):
        cur_max = max(arr[i], cur_max + arr[i])
        max_sum = max(max_sum, cur_max)

    return max_sum


print(max_subarray_sum([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]))