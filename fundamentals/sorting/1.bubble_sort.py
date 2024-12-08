import random
import time


def bubbleSort(alist):
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    start_time = time.time()
    for passnum in range(
        len(alist) - 1, 0, -1
    ):  # Each pass places the next largest element in its correct position
        for i in range(passnum):  # Left to right
            if alist[i] > alist[i + 1]:
                # swap
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    return alist


if __name__ == "__main__":
    alist = random.sample(range(1, int(1e6)), int(1e4))

    assert bubbleSort(alist) == sorted(alist, reverse=False), "Bubble sort is not correct"

# Time taken: 3.4777 seconds
