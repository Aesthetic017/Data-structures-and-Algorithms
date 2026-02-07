"""
Problem: Given a sorted array that has been rotated at an unknown pivot, search for a target value. The array was originally sorted in ascending order, then rotated (e.g., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
Example:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""
def search_rotated(arr, target):
    left = 0                     # Left pointer at start of array
    right = len(arr) - 1         # Right pointer at end of array, We use len(arr) - 1 because Python arrays are 0-indexed, so the last element’s index is one less than the length.
    
    # Run binary search while valid range exists
    while left <= right:
        mid = (left + right) // 2   # Find middle index

        # If middle value matches target, return index
        if arr[mid] == target:
            return mid

        # Check if LEFT half is sorted
        if arr[left] <= arr[mid]:

            # If target lies inside sorted left half
            if arr[left] <= target < arr[mid]:
                right = mid - 1      # Move search to left side
            else:
                left = mid + 1       # Search in right half instead
        
        # Otherwise RIGHT half must be sorted
        else:
            # If target lies inside sorted right half
            if arr[mid] < target <= arr[right]:
                left = mid + 1       # Move search to right side
            else:
                right = mid - 1      # Search in left half instead

    # If target is not found, return -1
    return -1


# Driver code to test function
if __name__ == '__main__':
    arr = [4, 5, 6, 7, 0, 1, 2, 3]   # Rotated sorted array
    target = 0                      # Value to search
    
    result = search_rotated(arr, target)   # Call function
    print(result)                    # Print index of target



# time complexity : O(logn n) and Space Complexity : O(1)

"""
left = 0 (value 4), right = 7 (value 3)
mid = (0 + 7) // 2 = 3 (value 7)

arr[mid] == target? → 7 == 0? NO

arr[left] <= arr[mid]?  4 <= 7? YES
So LEFT half [4,5,6,7] is sorted

Is target in sorted left half?
arr[left] <= target < arr[mid]? → 4 <= 0 < 7? NO
(0 is not >= 4, so target is NOT in left half)

Search RIGHT half → left = mid + 1 = 4
now, 
left = 4 (value 0), right = 7 (value 3)
mid = (4 + 7) // 2 = 5 (value 1)

arr[mid] == target? → 1 == 0? NO

arr[left] <= arr[mid]? → 0 <= 1? YES
So LEFT half [0,1] is sorted

Is target in sorted left half?
arr[left] <= target < arr[mid]? → 0 <= 0 < 1? YES
(0 >= 0 AND 0 < 1, so target IS in left half)

Search LEFT half → right = mid - 1 = 4
now , 
left = 4 (value 0), right = 4 (value 0)
mid = (4 + 4) // 2 = 4 (value 0)

arr[mid] == target? → 0 == 0? YES ✓

return 4
"""