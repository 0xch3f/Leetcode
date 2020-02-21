# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:45:20 2020

@author: yeesun
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, first in enumerate(nums):
            second = target - first
            pop = nums[:i] + nums[i+1:]
            if second in pop:
                j = (pop).index(second)
                if j >= i:
                    return [i, j+1]
                else:
                    return [i, j]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if j != i:
                        return [i, j]
