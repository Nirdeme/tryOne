
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the target is at the middle
        if arr[mid] == target:
            return mid

        # If the target is smaller, ignore the right half
        elif arr[mid] > target:
            right = mid - 1

        # If the target is larger, ignore the left half
        else:
            left = mid + 1

    # Target not found in the list
    return -1


sorted_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_value = 97
result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")


