def method_1(nums):
    """暴力枚举每一种可能性

    :param _type_ nums: _description_
    """
    n = len(nums)
    counter = 0
    for i in range(n):
        for j in range(n):
            # print(f"({i}, {j})")
            counter += 1
    print(f"method 1 counter: {counter}")


def method_2(nums):
    """根据一个数组中的数，互不相同, 缩小空间

    :param _type_ nums: _description_
    """
    n = len(nums)
    counter = 0
    for i in range(n):
        for j in range(i):
            print(f"({i}, {j})")
            counter += 1
    print(f"method 2 counter: {counter}")


def method_3(nums):
    """根据一个数组中的数，互不相同, 缩小空间

    :param _type_ nums: _description_
    """
    n = len(nums)
    counter = 0
    for i in range(n):
        for j in range(i + 1, n):
            print(f"({i}, {j})")
            counter += 1
    print(f"method 3 counter: {counter}")


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    method_1(nums)
    method_2(nums)
    method_3(nums)
