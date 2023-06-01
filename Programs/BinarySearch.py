# Create Binary Search method to find the target
#  https://leetcode.com/problems/binary-search/description/

def search(nums, target):        
    left, right = 0, len(nums)-1
    while left < right:
        mid = left + (right-left)//2
        if nums[mid]>=target:
            right = mid
        elif nums[mid]<target:
            left = mid+1
    if nums[left] != target:
        return -1
    return left