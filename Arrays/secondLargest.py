def second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None


if __name__ == "__main__":
    arr = [12, 35, 1, 10, 3, 1]
    result = second_largest(arr)
    print("Array:", arr)
    print("Second Largest:", result)