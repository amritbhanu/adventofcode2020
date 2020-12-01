def dataPreprocess():
    l = []
    with open("../data/day1.txt") as f:
        for x in f.readlines():
            l.append(int(x.strip()))
    return l

def sum_two_product(nums, summation=2020):
    for i in nums:
        if summation-i in nums:
            return i*(summation-i)

def sum_three_product(nums, summation=2020):
    for i in range(len(nums)-1):
        new_sum = summation-nums[i]
        for j in range(1, len(nums)):
            if new_sum-nums[j] in nums:
                return nums[j]*nums[i]*(new_sum-nums[j])

print(sum_two_product(dataPreprocess(), summation=2020))
print(sum_three_product(dataPreprocess(), summation=2020))
