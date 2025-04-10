# status: accepted


def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


if __name__=="__main__":
    case = [2, 7, 11, 15]
    target = 9

    ret = two_sum(case, target)
    print(ret)
