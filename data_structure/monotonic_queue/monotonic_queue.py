"""
 # @ Author: adam
 # @ Create Time: 2024-02-22 10:19:38
 # @ Modified by: adam
 # @ Modified time: 2024-02-22 13:41:37
 # @ Description: visualize internal state of monotonic queue
 """

from collections import deque


def max_sliding_window(nums, k):
    """export the maximum value of each sliding window, the brute force way

    :param _type_ nums: _description_
    :param _type_ k: _description_
    """
    n = len(nums)
    res = []
    for i in range(n - k + 1):
        best = min(nums) - 1
        for j in range(k):
            best = max(best, nums[i + j])
        res.append(best)

    return res


def monotonic_increasing(nums):
    """
    monotonically increasing queue

    :param _type_ nums: _description_
    """
    queue = deque()
    n = len(nums)
    print("monotonically increasing queue:")
    print("*" * 40)
    for i in range(n):
        # 把小的往左塞
        while queue and nums[i] <= queue[-1]:
            queue.pop()
        queue.append(nums[i])
        print(f"{i}: {queue}")
    print("\n")


def monotonic_decreasing(nums):
    """
    monotonically decreasing queue

    :param _type_ nums: _description_
    """
    queue = deque()
    n = len(nums)
    print("monotonically decreasing queue:")
    print("*" * 40)
    for i in range(n):
        # 把大的往左塞
        while queue and nums[i] >= queue[-1]:
            queue.pop()
        queue.append(nums[i])
        print(f"{i}: {queue}")
    print("\n")


if __name__ == "__main__":
    # nums = [0, -1, 2, 8, -4, -9, 10, 3, 0, 1]
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # print(max_sliding_window(nums, 5))
    monotonic_increasing(nums)
    monotonic_decreasing(nums)
