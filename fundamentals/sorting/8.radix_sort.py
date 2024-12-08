import random
import time
from math import log


def get_digit(number, d, base):
    return (number // base**d) % base


def counting_sort_with_digit(A, d, base):
    k = base - 1  # max digit value
    B = [-1] * len(A)  # Sorted array for counting sort of this digit
    C = [0] * (k + 1)  # Cumulative count array

    # Count the occurrences of each digit
    for a in A:
        C[get_digit(a, d, base)] += 1

    # Update C to contain the cumulative counts
    for i in range(1, k + 1):
        C[i] += C[i - 1]

    # Build the output array B in a stable manner
    for j in range(len(A) - 1, -1, -1):  # Iterate from the end to ensure stability
        digit_value = get_digit(A[j], d, base)
        B[C[digit_value] - 1] = A[j]  # Place the number in the correct position
        C[digit_value] -= 1  # Decrement the count

    return B


def radix_sort(list, base=10):
    digit = int(log(max(list), base) + 1)
    for d in range(digit):  # Sort from LSD to MSD: (100, 1000, 10000)
        list = counting_sort_with_digit(list, d, base)
    return list


if __name__ == "__main__":
    alist = random.sample(range(1, int(1e6)), int(1e4))
    start_time = time.time()
    assert radix_sort(alist) == sorted(alist)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")

# Time taken: 0.0403 seconds
