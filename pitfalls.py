"""Buggy versions of the pair sum, kept so tests can show how they fail."""


def pair_sum_less_equal(sorted_nums: list[int], target: int) -> list[int]:
    """Bug: the loop uses <= so an item can be paired with itself."""
    left, right = 0, len(sorted_nums) - 1

    while left <= right:
        total = sorted_nums[left] + sorted_nums[right]

        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1

    return []


def pair_sum_stuck(
    sorted_nums: list[int], target: int, max_steps: int = 1_000
) -> list[int]:
    """Bug: when the total equals the target, no pointer moves.

    A real version of this bug loops forever. This one raises an error
    after max_steps rounds so a test can catch it instead of hanging.
    """
    left, right = 0, len(sorted_nums) - 1
    steps = 0

    while left < right:
        steps += 1
        if steps > max_steps:
            raise RuntimeError("pointers stopped moving")

        total = sorted_nums[left] + sorted_nums[right]

        if total < target:
            left += 1
        elif total > target:
            right -= 1
        # Missing: the equal case. Nothing moves, so the loop repeats.

    return []
