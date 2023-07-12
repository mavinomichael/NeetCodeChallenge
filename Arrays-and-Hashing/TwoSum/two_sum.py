from typing import List


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict = {}
    for i, n in enumerate(nums):
        if n in dict:
            return dict[n], i
        else:
            dict[target - n] = i
