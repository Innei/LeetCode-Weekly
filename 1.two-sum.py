#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (42.97%)
# Total Accepted:    1.6M
# Total Submissions: 3.8M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#
#
#

'''
### 大意

给定一个列表和目标值, 请算出在给定的列表中任选两个元素使得他们相加等于目标值, 每个元素不能重复, 答案有唯一值. 返回他们的列表下标值的列表.

### 思路一

既然答案有唯一解, 那么我首先想到的是, 两重遍历相加如果等于给定值, 把他的下标加入新的列表.

```python3
 for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


```

但是这样做, 耗费的时间和内存太大, 那么有没有其他方式呢.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
