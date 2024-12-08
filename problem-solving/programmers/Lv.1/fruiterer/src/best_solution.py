# https://school.programmers.co.kr/learn/courses/30/lessons/135808/solution_groups?language=python3&type=all


def solution(k, m, score):
    return sum(sorted(score)[len(score) % m :: m]) * m
