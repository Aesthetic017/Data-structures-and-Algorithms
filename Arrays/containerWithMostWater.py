"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""

from typing import List


def max_area(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    best = 0
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        area = h * w
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1], 0),
        ([0, 0], 0),
    ]

    for i, (arr, expected) in enumerate(test_cases, 1):
        result = max_area(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: input={arr}")
        print(f"  Expected: {expected}, Got: {result} -> {status}\n")