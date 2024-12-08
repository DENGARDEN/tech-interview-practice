import time


def fibb(n):
    # O(n)
    table = [1] * (n + 1)  # Initialize the table with 1s
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


if __name__ == "__main__":
    start = time.time()
    fibb(int(1e6))  # 1 1 2 3 5 8 13 21 34 55
    end = time.time()
    print(f"Time taken: {end - start:.5f} seconds")

# Time taken: 30.16726 seconds