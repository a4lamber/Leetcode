nums = [-1, 0, 3, 5, 9, 12]

target = 9


def dummy():
    left = 0
    right = len(nums) - 1

    while left <= right:
        # floor division
        mid = (right - left) // 2

        if nums[mid] == target:
            return nums[mid]

        elif nums[mid] > target:
            # targer is on the left of the mid, move right
            right = mid - 1
        else:
            # targer is on the right of the mid, move left
            left = mid + 1
        print(left)
        # if operation reaches here, target not in the array
    return -1


# print(dummy())
print(len(nums))
