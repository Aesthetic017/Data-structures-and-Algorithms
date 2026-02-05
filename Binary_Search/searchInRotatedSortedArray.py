"""
Problem: Given a sorted array that has been rotated at an unknown pivot, search for a target value. The array was originally sorted in ascending order, then rotated (e.g., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
Example:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""

def search_rotated(arr,target):
    left = 0
    right = len(arr)-1
    
    while left<=right:
        mid = (left+right)//2
        
        if arr[mid] == target:
            return mid
        
        
        if arr[left]<=arr[mid]:
            if arr[left]<=target<arr[mid]:
                right = mid-1
            else: 
                left = mid +1
                
        else:
            if arr[mid]< target <=arr[right]:
                left = mid+1
            else:
                right = mid-1    
    
    return -1

if __name__ == '__main__':
    arr=[4,5,6,7,0,1,2,3]
    target = 0
    
    result = search_rotated(arr,target)
    
    print (result)                 
            