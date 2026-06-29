---
title : Two Sum
notes : use a hashmap to store complements
---

## Problem
Given an array of integers nums and an integer target, return indices of the two numbers that add up to target.

## Solution
def two_sum(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i
