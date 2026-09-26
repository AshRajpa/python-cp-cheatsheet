#1. Two Sum (Easy)

# You get an integer array nums and an integer target. Return the indices of the two numbers that add up to target.
#
# Exactly one valid answer exists.
# You can't use the same element twice.
# You can return the two indices in any order.
# Input	Output	Why
# nums = [2,7,11,15], target = 9	[0,1]	2 + 7 = 9
# nums = [3,2,4], target = 6	[1,2]	2 + 4 = 6
# nums = [3,3], target = 6	[0,1]
#
# Constraints: 2 ≤ len(nums) ≤ 10⁴, values range from -10⁹ to 10⁹.
# Follow-up: Can you do better than O(n²)?

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []

    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement]!= i:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
        return []


if __name__ == "__main__":
    sol = Solution()
    examples = [
        # (nums, target, expected)
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([1, 2, 3], 100, []),          # no answer
    ]
    for inp in examples:
        sol1 = sol.twoSum(inp[0], inp[1])
        sol2 = sol.twoSum1(inp[0], inp[1])
        print(f"{sol1},{sol2},{inp[2]}")
        print(f"{sol1 == inp[2]}")
        print(f"{sol2 == inp[2]}")
        print(f"test")
