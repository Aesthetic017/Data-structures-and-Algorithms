"""
Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers sorted in non-decreasing order,
find two numbers that add up to target. Return their 1-indexed positions.

Constraint: O(1) extra space -> two pointers (array is already sorted).

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # convert to 1-indexed
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []


# ---- Test cases ----
if __name__ == "__main__":
    sol = Solution()

    print(sol.twoSum([2, 7, 11, 15], 9))   # [1, 2]
    print(sol.twoSum([2, 7, 11, 15], 18))  # [2, 3]
    print(sol.twoSum([2, 3, 4], 6))        # [1, 3]
    print(sol.twoSum([-1, 0], -1))         # [1, 2]
    print(sol.twoSum([5, 25, 75], 100))    # [2, 3]