"""
Created on Tue Mar  9 19:10:04 2021

@author: 0xch3f

_Invariant: If the target value X is present in the array, then the target value is present in the current range_

"""

<img src="https://github.com/yeesunch/Leetcode/blob/master/Images/binary_search.jpg" width="600" height="300"/><br/>

---
Implementation: A standard Binary Search algo has two implementations: 
```
# 1. [left, right)
def binary_search(nums, target):
    low, high = 0, len(nums)
    while low < high:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid
    return -1

# 2. [left, right]
def binary_search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```



---
Python Bisect

|bisect|left|  |bisect|right| 
:-:|:-:|:-:|:-:|:-:
|<|>=| |<=|>|
|low|high| |low|high| 

(since we update low and high by low = mid + 1 & high = mid)  

```
# 1. Bisect left - Find the lower bound of >= target
def bisect_left(nums, target):
    low, high = 0, len(nums)
    while low < high:
        mid = low + (high - low) // 2
        if target >= nums[mid]:
            high = mid
        else:
            low = mid + 1
    return low

# 2. Bisect right - Find the lower bound of > target
def bisect_right(nums, target):
    low, high = 0, len(nums)
    while low < high:
        mid = low + (high - low) // 2
        if target < nums[mid]:
            high = mid
        else:
            low = mid + 1
    return low

```
