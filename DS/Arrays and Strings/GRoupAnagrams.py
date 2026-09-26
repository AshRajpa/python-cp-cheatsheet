# Problem
#
# You get a list of strings strs. Group together the strings that are anagrams of each other, and return the groups in any order.
#
# Two words are anagrams when they use exactly the same letters, the same number of times, in a different order. For example, "eat", "tea" and "ate" are all anagrams because each has one e, one a and one t.
#
# Examples
#
# Example 1
#
# Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# "eat", "tea" and "ate" share the letters a, e, t.
# "tan" and "nat" share the letters a, n, t.
# "bat" has no anagram in the list, so it forms a group on its own.
#
# Example 2
#
# Input:  strs = [""]
# Output: [[""]]
#
# The empty string is a valid word and forms its own group.
#
# Example 3
#
# Input:  strs = ["a"]
# Output: [["a"]]
# Constraints
# 1 ≤ len(strs) ≤ 10⁴
# 0 ≤ len(strs[i]) ≤ 100
# Every string contains only lowercase English letters.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pass