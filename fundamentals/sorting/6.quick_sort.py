import random
import time


def quick_sort(alist):

    quick_sort_helper(alist, 0, len(alist) - 1)  # Recursive function to sort the array
    return alist


def quick_sort_helper(alist, first, last):
    """Recursive function to sort the array

    Args:
        alist (list): The array to be sorted
        first (int): The leftmark index of the array
        last (int): The rightmark index of the array
    """
    # Base case: if the array has only one element, it is already sorted
    if first < last:
        # Partition the array and get the split point
        splitpoint = partition(alist, first, last)

        # Recursively sort the left and right halves of the array
        quick_sort_helper(alist, first, splitpoint - 1)
        quick_sort_helper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    """Partition the array and get the split point

    Args:
        alist (list): The array to be partitioned
        first (int): The leftmark index of the array
        last (int): The rightmark index of the array
    """
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False

    # Move unitil the leftmark is greater than the rightmark
    while not done:

        # Move the leftmark to the right until the value is greater than the pivot
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        # Move the rightmark to the left until the value is less than the pivot
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        # If the leftmark is greater than the rightmark, the partition is done
        if rightmark < leftmark:
            done = True
        else:
            # Swap the leftmark and rightmark values
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    # Swap the pivot with the rightmark value
    temp = alist[first]  # Store the pivot value
    alist[first] = alist[rightmark]  # Swap the pivot with the rightmark value
    alist[rightmark] = temp  # Swap the rightmark value with the pivot

    # Return the split point
    return rightmark


if __name__ == "__main__":
    alist = random.sample(range(1, int(1e6)), int(1e4))
    start_time = time.time()
    assert quick_sort(alist) == sorted(alist, reverse=False), "Quick sort is not correct"
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")

# Time taken: 0.0111 seconds
