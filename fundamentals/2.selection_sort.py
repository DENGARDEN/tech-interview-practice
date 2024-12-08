import random
import time


# Ascending order
# For descending order, just change the condition in the if statement
def selectionSort(alist):
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    start_time = time.time()
    for fillslot in range(
        len(alist) - 1, 0, -1
    ):  # Right to left : The rightmost element is the largest
        positionOfMax = 0
        for location in range(1, fillslot + 1):  # Left to right
            # Find the maximum value in the unsorted part of the list
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        # Swap the maximum value with the last element of the unsorted part
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    return alist


if __name__ == "__main__":
    alist = random.sample(range(1, int(1e6)), int(1e4))
    assert selectionSort(alist) == sorted(
        alist, reverse=False
    ), f"Selection sort is not correct {selectionSort(alist)}"

# Time taken: 1.4633 seconds
