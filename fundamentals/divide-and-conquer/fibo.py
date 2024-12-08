def fibb(n):
    if n <= 1:
        return 1
    return fibb(n - 1) + fibb(n - 2)


if __name__ == "__main__":
    print(fibb(9))  # 1 1 2 3 5 8 13 21 34 55
