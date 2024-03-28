def generate_lsp(p: str):
    """generate the longest suffix prefix array of the pattern string

    :param str p: _description_
    :return _type_: _description_
    """
    # 初始化数组元素全部为 0
    m = len(p)
    lsp = [0 for _ in range(m)]

    # left表示前缀串开始所在的下标位置, right 表示后缀串开始所在的下标位置
    left = 0
    for right in range(1, m):
        while left > 0 and p[left] != p[right]:
            # 匹配不成功, 往前找是否有别的前缀满足条件，即left进行回退,
            # left == 0时走到头了，退无可退
            left = lsp[left - 1]
        if p[left] == p[right]:
            # 匹配成功，找到相同的前后缀，先让 left += 1，此时 left 为前缀长度
            left += 1
        # 记录前缀长度，更新 next[right], 结束本次循环, right += 1
        lsp[right] = left

    return lsp


if __name__ == "__main__":
    p = "abcabf"
    print(generate_lsp(p))
