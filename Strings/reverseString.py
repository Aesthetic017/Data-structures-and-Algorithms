"""Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
    """
    
def reverseString(s: list) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

if __name__ == "__main__":
    s1 = ["h","e","l","l","o"]
    print(f"Before: {s1}")
    reverseString(s1)
    print(f"After:  {s1}")

    s2 = ["H","a","n","n","a","h"]
    print(f"Before: {s2}")
    reverseString(s2)
    print(f"After:  {s2}")