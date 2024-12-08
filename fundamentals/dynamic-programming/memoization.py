import time

# 전역 변수로 TABLE과 N이 미리 선언됨
N = int(1e5)
TABLE = [None] * (N + 1)


def fibb(n):

    if n <= 1:
        return 1
    if TABLE[n]:  # 이미 계산된 값이 있으면 바로 반환
        return TABLE[n]
    TABLE[n] = fibb(n - 1) + fibb(n - 2)  # 계산된 값을 저장
    return TABLE[n]  # 계산된 값 반환


if __name__ == "__main__":
    start = time.time()
    print(fibb(int(1e5)))  # 1 1 2 3 5 8 13 21 34 55
    end = time.time()
    print(f"Time taken: {end - start:.5f} seconds")

# Maximum recursion depth exceeded in comparison
