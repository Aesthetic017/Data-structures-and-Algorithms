from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            print(f"Pushed {num} -> heap: {heap}")
            if len(heap) > k:
                popped = heapq.heappop(heap)
                print(f"  Size > k, popped smallest ({popped}) -> heap: {heap}")
        return heap[0]


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    print("Array:", nums)
    print("k:", k)
    print("-" * 40)

    result = sol.findKthLargest(nums, k)

    print("-" * 40)
    print(f"{k}th Largest Element:", result)