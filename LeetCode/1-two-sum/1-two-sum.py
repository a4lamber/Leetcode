
num = [2,7,11,15]
num = [3,2,4]

def test(nums,target):
    result = []
    for i, item_x in enumerate(nums):
        for j, item_y in enumerate(nums):
            if item_x + item_y == target:
                result.append(i)
                result.append(j)
                
                break_out_flag = True
                break
        if break_out_flag:
            break
    
    return result


print(test(num,6))
