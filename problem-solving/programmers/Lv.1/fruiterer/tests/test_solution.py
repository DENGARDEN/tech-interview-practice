import pytest

from src.best_solution import solution as best_solution
from src.solution import solution as solution


@pytest.mark.parametrize("solution", [solution, best_solution])
@pytest.mark.parametrize(
    "k, m, score, expected",
    [
        (3, 4, [1, 2, 3, 1, 2, 3, 1], 8),  # Test case 1
        (4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2], 33),  # Test case 2
    ],
)
def test_solution(solution, k, m, score, expected):
    assert solution(k, m, score) == expected, f"Failed for input (k={k}, m={m}, score={score})"
