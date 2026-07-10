from typing import List
import heapq
# Import List for type hinting, and heapq for min-heap operations


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Define the method that takes the array and k, and returns the kth largest value

        heap = []
        # Start with an empty heap (a plain list managed by heapq)

        for num in nums:
            # Go through every number in the array, one at a time

            heapq.heappush(heap, num)
            print(f"Pushed {num} -> heap: {heap}")
            # Add the number to the heap; heapq automatically keeps the smallest value at heap[0]
            # Print the heap's current contents so we can see it grow

            if len(heap) > k:
                popped = heapq.heappop(heap)
                print(f"  Size > k, popped smallest ({popped}) -> heap: {heap}")
                # If the heap now holds more than k elements, remove the smallest one
                # This keeps the heap limited to only the k largest values seen so far

        return heap[0]
        # Once all numbers are processed, the heap holds the k largest values
        # The smallest of those k (heap[0]) is exactly the kth largest overall


if __name__ == "__main__":
    # Only runs this block when the file is executed directly, not when imported elsewhere

    sol = Solution()
    # Create an object of the Solution class

    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    # Sample input: array to search, and which "kth largest" we want

    print("Array:", nums)
    print("k:", k)
    print("-" * 40)
    # Print the input details and a separator line for readability

    result = sol.findKthLargest(nums, k)
    # Call the method on the object, passing in nums and k, and store the returned answer

    print("-" * 40)
    print(f"{k}th Largest Element:", result)
    # Print a separator, then print the final result