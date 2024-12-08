def solution(k, m, score):
    # k is not used
    score = sorted(score, reverse=True)

    answer = 0
    for i in range(0, len(score) - m + 1, m):
        answer += score[i + m - 1] * m

    return answer
