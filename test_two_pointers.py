import random

import pytest

from brute_force import pair_sum_brute, three_sum_brute
from two_pointers import (
    is_palindrome,
    merge_sorted,
    pair_with_target_sum,
    remove_duplicates,
    reverse_in_place,
    three_sum,
)


# --- pair sum -------------------------------------------------------------


def test_pair_sum_finds_the_pair() -> None:
    assert pair_with_target_sum([1, 3, 5, 8, 11], 13) == [2, 3]


def test_pair_sum_returns_empty_list_when_there_is_no_pair() -> None:
    assert pair_with_target_sum([1, 3, 5, 8, 11], 100) == []


@pytest.mark.parametrize("nums", [[], [7]])
def test_pair_sum_handles_fewer_than_two_items(nums: list[int]) -> None:
    assert pair_with_target_sum(nums, 7) == []


def test_pair_sum_does_not_pair_an_item_with_itself() -> None:
    assert pair_with_target_sum([4], 8) == []


def test_pair_sum_works_with_negative_numbers() -> None:
    assert pair_with_target_sum([-4, -1, 0, 3, 10], 9) == [1, 4]


def test_pair_sum_agrees_with_brute_force_on_random_sorted_lists() -> None:
    rng = random.Random(42)
    for _ in range(2_000):
        nums = sorted(rng.randint(-20, 20) for _ in range(rng.randint(0, 12)))
        target = rng.randint(-30, 30)
        fast = pair_with_target_sum(nums, target)
        slow = pair_sum_brute(nums, target)
        # The two may pick different pairs, but they must agree on whether
        # a pair exists, and any pair they return must really add up.
        assert bool(fast) == bool(slow)
        if fast:
            i, j = fast
            assert i < j
            assert nums[i] + nums[j] == target


def test_pair_sum_gives_wrong_answers_on_unsorted_input() -> None:
    # 1 + 3 = 4 exists, but the "too small, move left" rule needs sorted data.
    assert pair_with_target_sum([1, 3, 2], 4) == []
    assert pair_sum_brute([1, 3, 2], 4) == [0, 1]


# --- reverse ----------------------------------------------------------------


@pytest.mark.parametrize(
    "items",
    [[], [1], [1, 2], [1, 2, 3, 4, 5], [1, 1, 1]],
)
def test_reverse_in_place_matches_slicing(items: list[int]) -> None:
    expected = items[::-1]
    reverse_in_place(items)
    assert items == expected


def test_reverse_in_place_returns_nothing_and_changes_the_same_list() -> None:
    items = [1, 2, 3]
    same_list = items
    assert reverse_in_place(items) is None
    assert same_list == [3, 2, 1]


# --- palindrome -------------------------------------------------------------


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("a", True),
        (".,", True),
        ("0P", False),
    ],
)
def test_is_palindrome(text: str, expected: bool) -> None:
    assert is_palindrome(text) is expected


# --- remove duplicates ------------------------------------------------------


def test_remove_duplicates_keeps_each_value_once() -> None:
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = remove_duplicates(nums)
    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]


@pytest.mark.parametrize(
    ("nums", "expected"),
    [([], []), ([5], [5]), ([2, 2, 2], [2]), ([1, 2, 3], [1, 2, 3])],
)
def test_remove_duplicates_edge_cases(nums: list[int], expected: list[int]) -> None:
    k = remove_duplicates(nums)
    assert nums[:k] == expected


def test_remove_duplicates_agrees_with_sorted_set_on_random_input() -> None:
    rng = random.Random(7)
    for _ in range(1_000):
        nums = sorted(rng.randint(0, 6) for _ in range(rng.randint(0, 15)))
        expected = sorted(set(nums))
        k = remove_duplicates(nums)
        assert nums[:k] == expected


# --- merge ------------------------------------------------------------------


def test_merge_sorted_interleaves_two_lists() -> None:
    assert merge_sorted([1, 4, 7], [2, 3, 9]) == [1, 2, 3, 4, 7, 9]


@pytest.mark.parametrize(
    ("first", "second"),
    [([], [5, 6]), ([5, 6], []), ([], []), ([1, 1], [1, 1])],
)
def test_merge_sorted_edge_cases(first: list[int], second: list[int]) -> None:
    assert merge_sorted(first, second) == sorted(first + second)


def test_merge_sorted_does_not_change_its_inputs() -> None:
    first, second = [1, 4], [2, 3]
    merge_sorted(first, second)
    assert first == [1, 4]
    assert second == [2, 3]


# --- three sum --------------------------------------------------------------


def test_three_sum_finds_unique_triplets() -> None:
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


@pytest.mark.parametrize(
    ("nums", "expected"),
    [([], []), ([0], []), ([0, 0], []), ([0, 0, 0], [[0, 0, 0]]), ([1, 2, 3], [])],
)
def test_three_sum_edge_cases(nums: list[int], expected: list[list[int]]) -> None:
    assert three_sum(nums) == expected


def test_three_sum_all_zeros_returns_one_triplet() -> None:
    assert three_sum([0] * 10) == [[0, 0, 0]]


def test_three_sum_does_not_change_its_input() -> None:
    nums = [3, -1, 2, -2, 0]
    three_sum(nums)
    assert nums == [3, -1, 2, -2, 0]


def test_three_sum_agrees_with_brute_force_on_random_input() -> None:
    rng = random.Random(2026)
    for _ in range(500):
        nums = [rng.randint(-6, 6) for _ in range(rng.randint(0, 10))]
        assert three_sum(nums) == three_sum_brute(nums)
