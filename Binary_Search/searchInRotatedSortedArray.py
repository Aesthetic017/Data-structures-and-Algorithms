"""
Problem: Given a sorted array that has been rotated at an unknown pivot, search for a target value. The array was originally sorted in ascending order, then rotated (e.g., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
Example:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""
def search_rotated(arr, target):
    left = 0                     # Left pointer at start of array
    right = len(arr) - 1         # Right pointer at end of array

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