import random
import time


def counting_sort(A, k):
    """Counting sort algorithm

    Args:
        A (list): The array to be sorted
        k (int): The maximum value in the array
    """
    B = [-1] * len(A)  # The sorted array
    C = [0] * (k + 1)  # The count array

    # Count the number of times each value appears in the array
    for a in A:
        C[a] += 1

    # Compute the cumulative count
    for i in range(k):
        C[i + 1] += C[i]

    # Place the elements in the sorted array
    for j in reversed(range(len(A))):
        B[C[A[j]] - 1] = A[j]  # C is cumulative count, so we need to subtract 1
        C[A[j]] -= 1  # Decrement the count
    return B


if __name__ == "__main__":
    alist = random.sample(range(1, int(1e6)), int(1e4))
    start_time = time.time()
    assert counting_sort(alist, int(1e6)) == sorted(
        alist, reverse=False
    ), "Counting sort is not correct"
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")

# Time taken: 0.0855 seconds
