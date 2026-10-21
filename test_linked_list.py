import pytest

from linked_list import find_middle, from_values


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 3),
        ([1, 2, 3, 4, 5], 3),
    ],
)
def test_find_middle_returns_the_second_middle_for_even_lengths(
    values: list[int], expected: int
) -> None:
    middle = find_middle(from_values(values))
    assert middle is not None
    assert middle.val == expected


def test_find_middle_of_an_empty_list_is_none() -> None:
    assert find_middle(None) is None


def test_find_middle_agrees_with_indexing_on_every_length() -> None:
    for length in range(1, 50):
        values = list(range(length))
        middle = find_middle(from_values(values))
        assert middle is not None
        assert middle.val == values[length // 2]
