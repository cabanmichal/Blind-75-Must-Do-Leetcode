"""https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without
repeating characters.
"""
from typing import Dict


def substring_length(s: str) -> int:
    """
    >>> substring_length("abcabcbb")
    3
    >>> substring_length("bbbbb")
    1
    >>> substring_length("pwwkew")
    3
    >>> substring_length("")
    0
    >>> substring_length("abcdeafbdgcbb")
    7
    >>> substring_length(" ")
    1
    """

    memory: Dict[str, int] = {}
    longest = 0
    start = 0
    for i, c in enumerate(s):
        if c in memory:
            start = max(start, memory[c])
        memory[c] = i + 1
        longest = max(longest, memory[c] - start)

    return longest


if __name__ == "__main__":
    import doctest

    doctest.testmod()
