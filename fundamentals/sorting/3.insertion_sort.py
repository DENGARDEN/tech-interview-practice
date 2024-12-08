import random
import time


def insertion_sort(collection):
    # Time complexity: O(n^2), best case: O(n)
    # Space complexity: O(1)
    start_time = time.time()
    for index in range(
        1, len(collection)
    ):  # Start from the second element: The first element is already sorted
        while 0 < index and collection[index] < collection[index - 1]:
            # Swap the current element with the previous element
            # Cascade the swap until the correct position is found
            collection[index], collection[index - 1] = collection[index - 1], collection[index]
            index -= 1
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    return collection


if __name__ == "__main__":
    alist = random.sample(range(1, int(1e6)), int(1e4))
    assert insertion_sort(alist) == sorted(alist, reverse=False), "Insertion sort is not correct"

# Time taken: 2.7055 seconds
