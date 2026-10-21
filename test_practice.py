import random

import pytest

from practice import is_subsequence, max_area, sorted_squares


@pytest.mark.parametrize(
    ("short", "long", "expected"),
    [
        ("ace", "abcde", True),
        ("aec", "abcde", False),
        ("", "abc", True),
        ("", "", True),
        ("a", "", False),
        ("abc", "abc", True),
        ("abcd", "abc", False),
    ],
)
def test_is_subsequence(short: str, long: str, expected: bool) -> None:
    assert is_subsequence(short, long) is expected


def test_sorted_squares_example() -> None:
    assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


@pytest.mark.parametrize("nums", [[], [0], [-3], [-2, -1], [1, 2, 3], [-5, -3, -1]])
def test_sorted_squares_matches_square_then_sort(nums: list[int]) -> None:
    assert sorted_squares(nums) == sorted(n * n for n in nums)


def test_sorted_squares_agrees_with_square_then_sort_on_random_input() -> None:
    rng = random.Random(11)
    for _ in range(500):
        nums = sorted(rng.randint(-10, 10) for _ in range(rng.randint(0, 12)))
        assert sorted_squares(nums) == sorted(n * n for n in nums)


def test_max_area_example() -> None:
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


@pytest.mark.parametrize(
    ("heights", "expected"),
    [([], 0), ([5], 0), ([1, 1], 1), ([4, 3, 2, 1, 4], 16)],
)
def test_max_area_edge_cases(heights: list[int], expected: int) -> None:
    assert max_area(heights) == expected


def test_max_area_agrees_with_brute_force_on_random_input() -> None:
    rng = random.Random(5)
    for _ in range(500):
        heights = [rng.randint(0, 9) for _ in range(rng.randint(0, 12))]
        expected = max(
            (
                min(heights[i], heights[j]) * (j - i)
                for i in range(len(heights))
                for j in range(i + 1, len(heights))
            ),
            default=0,
        )
        assert max_area(heights) == expected
