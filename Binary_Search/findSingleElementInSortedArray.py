'''
Problem: Given a sorted array where every element appears exactly twice except for one element which appears once, find that single element. Solve in O(log n) time.
Example:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
'''

def singleElement(nums):
    left = 0
    right = len(nums)-1
    
    while left <  right:
        mid = (left+right )//2
        
        if mid %2==1:
            mid -=1
        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid
    
    return nums[left]

if __name__== "__main__" :
    nums = [1,1,2,3,3,4,4,5,5,8,8] 
    result = singleElement(nums)
    print(result)
    
'''
Here nums = [1,1,2,3,3,4,4,5,5,8,8] target is find single element. 
     left = 0 right = 9 so mid = 9//2 = 4
     mid = 4 which is already even if its not make it even line 16 17
     
     so nums[mid]== nums[mid+1] ?
     3 == 4 ? No, so 
     right becomes new mid 
     
     now left = 0 right = 4 mid = 2
      so nums[mid]== nums[mid+1] ?
      2 ==3 ? no so ,
      right becomes new mid 
      
    now left = 0 right =2  mid =1 
       so nums[mid]== nums[mid+1] ?
      1 ==2 ? no so ,
      right becomes new mid
      
      now left = 0 right = 2  mid = 1 
        mid is odd → make it even → mid = 0

        so nums[mid] == nums[mid+1] ?
        1 == 1 ? Yes

            so left = mid + 2
        left = 2
        
        now left = right but the loop condition is left < right so it stops and returns left 
        so output is 2 

'''    
