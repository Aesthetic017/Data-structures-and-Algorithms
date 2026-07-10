from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    print("Before:", nums)
    sol.rotate(nums, k)
    print("After:", nums)