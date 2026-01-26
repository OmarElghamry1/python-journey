from util import time_it


@time_it
def LinearSearch(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1


@time_it
def BinarySearch(num_list, target):
    left_index = 0
    right_index = len(num_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if target == num_list[mid_index]:
            return mid_index

        elif target > num_list[mid_index]:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1.0


@time_it
def BinarySearchRecursive(num_list, target, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2

    if mid_index >= len(num_list) or mid_index < 0:
        return -1

    mid_number = num_list[mid_index]

    mid_index = (left_index + right_index) // 2

    if target == num_list[mid_index]:
        return mid_index

    elif target > num_list[mid_index]:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return BinarySearchRecursive(numbers_list, number_to_find, left_index, right_index)


if __name__ == "__main__":
    import numpy as np

    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 21

    nums_list = [np.random.randint(0, 1000000) for i in range(100000)]
    target = 54353

    # Make sure the list is sorted before performing binary search
    nums_list.sort()

    index1 = BinarySearchRecursive(nums_list, target, 0, len(nums_list) - 1)
    index = BinarySearch(nums_list, target)

    print(f"Number found at index {index1} using recursive binary search")
    print(f"Number found at index {index} using iterative binary search")
