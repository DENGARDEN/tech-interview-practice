import pytest


@pytest.mark.parametrize(
    "kwargs",
    [
        pytest.param({"flo": 1.42, "result": 1}, id="test_case_1"),
        pytest.param({"flo": 69.32, "result": 69}, id="test_case_2"),
    ],
)
def test_solution(kwargs):
    # from src.best_solution import solution as best_solution
    from src.solution import solution  # Import the solution function here

    result = kwargs.pop("result")
    assert solution(**kwargs) == result, f"Failed for input (kwargs={kwargs})"
