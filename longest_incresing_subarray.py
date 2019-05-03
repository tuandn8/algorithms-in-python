def longest_incresing_subarray(arr):
    max = 1
    length = 1
    max_index = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            length += 1
        else:
            if max < length:
                max = length
                max_index = i - max

            length = 1

    if max < length:
        max = length
        max_index = n - max

    print(arr[max_index:max_index + max])


longest_incresing_subarray([1 , 3, 5, 7 ,4 ,5])