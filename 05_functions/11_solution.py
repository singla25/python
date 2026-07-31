# Find maximum number

def max_number(*nums):
    if len(nums) == 0:
        return "Invalid Numbers"

    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

n = input("Enter numbers separated by spaces: ")
listofnum = [int(num) for num in n.split()]

print(max_number(*listofnum))

