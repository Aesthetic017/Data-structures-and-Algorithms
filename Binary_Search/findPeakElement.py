"""
    Problem: A peak element is an element that is strictly greater than its neighbors. Given an array, find any peak elements index. 
    input nums=[1,2,3,1]
    Output =2 // index of peak element
"""

def peakElement(nums):
                                                
    left = 0
    right = len(nums)-1
    
    while left < right :
        mid = (left+right)//2
        
        if nums[mid]<nums[mid+1]:
           left = mid+1
        else:
            right=mid
            
    return left       

if __name__=='__main__': 
    
    nums = [1,2,3,1]   
    result = peakElement(nums)
    print(result)
    
#Explaination :   
"""
[1,2,3,1]
left = 0 right=3
mid = 0+3 //2 = 1
// 3 is greater than 2 ( which is num[mid]<nums[mid+1]) sp left = mid+1

now,
left = 2 right = 3
mid = 2+3 // 2 = 2

// 1 is not greater than 3 which is at i=2 so right = mid

now, 

left = 2 right = 2

it started with left<right so the loop won't run and it returns left 
so the value of left is index 2 which is 3

so the output is 2, with value 3
"""    