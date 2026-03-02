'''
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
'''


def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    
    for i in range(len(s)):
        if s == goal:
            return True
        s = s[1:] + s[0]
    
    return False

if __name__ == "__main__":

    s1, goal1 = "abcde", "cdeab"
    print(f"Input: s={s1}, goal={goal1}")
    print(f"Output: {rotateString(s1, goal1)}")   # True
    
    print()
    
    s2, goal2 = "abcde", "abced"
    print(f"Input: s={s2}, goal={goal2}")
    print(f"Output: {rotateString(s2, goal2)}")   # False


        