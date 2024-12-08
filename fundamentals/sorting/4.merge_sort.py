import random
import time


def merge(leftList, rightList):
    result = []
    i, j = 0, 0  # Initialize pointers for leftList and rightList
    while i < len(leftList) and j < len(rightList):  # Iterate while both lists have elements
        if leftList[i] <= rightList[j]:
            result.append(leftList[i])  # Append the smaller element from the left list
            i += 1  # Move the pointer in leftList
        else:
            result.append(rightList[j])  # Append the smaller element from the right list
            j += 1  # Move the pointer in rightList
    result.extend(leftList[i:])  # Add remaining elements from leftList if any
    result.extend(rightList[j:])  # Add remaining elements from rightList if any
    return result


def merge_sort(alist):
    # Time complexity: O(n log n)
    # Space complexity: O(n)
    # Depth of recursion: log n

    if len(alist) <= 1:  # Base case: If the list has only one element, it is already sorted
        return alist
    mid = len(alist) // 2  # Split the list into two halves
    leftList = alist[:mid]  # Left half
    rightList = alist[mid:]  # Right half
    leftList = merge_sort(leftList)  # Recursively sort the left half
    rightList = merge_sort(rightList)  # Recursively sort the right half
    result = merge(leftList, rightList)  # Merge the two sorted halves

    return result


if __name__ == "__main__":
    alist = random.sample(range(1, int(1e6)), int(1e4))
    start_time = time.time()
    assert merge_sort(alist) == sorted(
        alist, reverse=False
    ), f"Merge sort is not correct: {merge_sort(alist)}"
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")

# Time taken: 0.0178 seconds
