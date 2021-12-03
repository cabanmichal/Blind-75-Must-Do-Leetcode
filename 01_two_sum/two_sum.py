"""https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    >>> two_sum([2, 7, 11 ,15], 9)
    [0, 1]
    >>> two_sum([3, 2, 4], 6)
    [1, 2]
    >>> two_sum([3, 3], 6)
    [0, 1]
    """
    checked = {}
    for i, num in enumerate(nums):
        missing = target - num
        if missing in checked:
            return sorted([i, checked[missing]])
        checked[num] = i

    return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
