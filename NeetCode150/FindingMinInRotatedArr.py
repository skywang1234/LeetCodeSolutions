nums = [11,13,15,17]
left = 0
right = len(nums)-1
#in correct sequence left>mid<right
while left<right:
    mid = left+(right-left)//2
    if nums[mid]>nums[left]:
        right = mid-1
        continue
    elif nums[mid]>nums[right]:
        left = mid+1
        continue
    else:
        print(nums[mid])
        break
print(nums[mid])