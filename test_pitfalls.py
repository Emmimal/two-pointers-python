import pytest

from pitfalls import pair_sum_less_equal, pair_sum_stuck
from two_pointers import pair_with_target_sum


def test_less_equal_pairs_an_item_with_itself() -> None:
    # Only one 4 exists, so 4 + 4 = 8 is not a real answer.
    assert pair_sum_less_equal([4], 8) == [0, 0]
    assert pair_with_target_sum([4], 8) == []


def test_stuck_version_never_finishes_when_a_pair_exists() -> None:
    with pytest.raises(RuntimeError, match="stopped moving"):
        pair_sum_stuck([1, 3, 5, 8, 11], 13)


def test_stuck_version_looks_fine_when_there_is_no_pair() -> None:
    # The bug hides until the first time the total equals the target.
    assert pair_sum_stuck([1, 3, 5, 8, 11], 100) == []
