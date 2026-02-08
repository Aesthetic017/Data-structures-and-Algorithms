"""
Problem: Given a sorted array with possible duplicates, find the starting 
and ending position of target value. If not found return [-1, -1]

Input: arr = [5,7,7,8,8,10]
Output: [3,4]  (indices where 8 appears)
"""

def findPositions(arr, target):
    
    def find_bound(is_first):
        left = 0
        right = len(arr) - 1
        boundary = -1  
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                boundary = mid  
                
                if is_first:
                    right = mid - 1  
                else:
                    left = mid + 1   # Search right for last occurrence
                    
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return boundary
    
    first = find_bound(True)
    if first == -1:
        return [-1, -1]  
    
    last = find_bound(False)
    return [first, last]


if __name__ == '__main__':  
    arr = [5, 7, 7, 8, 8, 10]
    target = 8
    result = findPositions(arr, target)
    print(result)  
    
'''
arr = [5,7,7,8,8,10]
target = 8
o/p = [3,4]

find bound is a function which returns boundary depending what is  is_first  

first = find_bound(True) means is_first=True for first occurence

left = 0 right = 5 mid = 2
mid =2 i.e 7 is not equal to target and its < target 

so it runs elif arr[mid]<target condition
and now left becomes mid+1 which is 3+1

now left = 3 right 5 so mid is 4
mid =4 i.e. 8 which = target so it runs arr [mid] ==target conditon and sets boundary =4 
as is_first is true it takes right -1 = mid

now boundary is 4 left = 3 right=4
so mid is 3+4//2 = 3

mid = target yes
so boundary is updated to 3 

like this the first = find_bound(True) runs and when the left > right , it stops 

now searching for last, is_first gonna be false

and like first occurence the function will find the last element in array and it returns 

-----------------------------------------------------------------------------------------------------------
arr = [5, 7, 7, 8, 8, 10]
Index:  0  1  2  3  4  5

Finding FIRST (is_first = True):
Step 1: mid=2, arr[2]=7, 7<8, go RIGHT
Step 2: mid=4, arr[4]=8, FOUND! boundary=4, search LEFT
Step 3: mid=3, arr[3]=8, FOUND! boundary=3 (UPDATE), search LEFT
Step 4: left>right, STOP
Result: first = 3

Finding LAST (is_first = False):
Step 1: mid=2, arr[2]=7, 7<8, go RIGHT
Step 2: mid=4, arr[4]=8, FOUND! boundary=4, search RIGHT
Step 3: mid=5, arr[5]=10, 10>8, go LEFT
Step 4: left>right, STOP
Result: last = 4

Final Answer: [3, 4]
'''    