# Max heap implementation using array
import random
import time


def max_heapify(unsorted, index, heap_size):
    largest = index  # Initialize the largest element as the current index
    left_child = 2 * index + 1  # Left child index
    right_child = 2 * index + 2  # Right child index

    # If the left child is larger than the current largest, update the largest
    if left_child < heap_size and unsorted[left_child] > unsorted[largest]:
        largest = left_child

    # If the right child is larger than the current largest, update the largest
    if right_child < heap_size and unsorted[right_child] > unsorted[largest]:
        largest = right_child

    # If the largest element is not the current index, swap them and recursively call max_heapify on the largest element
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        max_heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        # Build the max heap from the bottom up
        max_heapify(unsorted, i, n)

    temp = unsorted.copy()
    for i in range(n - 1, 0, -1):  # Heap size decreases by 1 each iteration
        # Extract the maximum element from the heap and swap it with the last element
        temp[0], temp[i] = temp[i], temp[0]
        max_heapify(temp, 0, i)  # Restore the max heap property
    return temp  # Return the sorted array


if __name__ == "__main__":
    alist = random.sample(range(1, int(1e6)), int(1e4))
    start_time = time.time()
    assert heap_sort(alist) == sorted(alist, reverse=False), "Heap sort is not correct"
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")

# Time taken: 0.0273 seconds
