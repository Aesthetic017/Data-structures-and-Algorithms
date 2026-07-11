"""
Move Zeroes
Move all 0's in a list to the end while maintaining the relative
order of the non-zero elements. Done in-place.

Time:  O(n)
Space: O(1)
"""


def move_zeroes(nums):
    insert_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            # swap nums[i] and nums[insert_pos]
            nums[i], nums[insert_pos] = nums[insert_pos], nums[i]
            insert_pos += 1

    return nums


# ---- Test cases ----
if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))    # [1, 3, 12, 0, 0]
    print(move_zeroes([0, 0, 1]))           # [1, 0, 0]
    print(move_zeroes([1, 2, 3]))           # [1, 2, 3] (no zeroes)
    print(move_zeroes([0, 0, 0]))           # [0, 0, 0]
    print(move_zeroes([4, 0, 5, 0, 6, 0]))  # [4, 5, 6, 0, 0, 0]