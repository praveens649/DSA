def canJump(nums):
    reachable = 0
    for i in range(len(nums)):
        if i > reachable :
            return False
            break
        reachable = max (reachable, i+nums[i])
        if reachable >= len(nums)-1:
            return True
            break

print(canJump([3,2,1,0,4]))