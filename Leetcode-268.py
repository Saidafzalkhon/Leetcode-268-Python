nums = list(map(int,input().split()))
nums.sort()
son = 0
for i in range(len(nums)-1):
    if nums[i]+1 != nums[i+1]:
        son = nums[i]+1
        break
if son == 0:
    if(nums[0] == 0):
        son = nums[len(nums)-1]+1
print(son)