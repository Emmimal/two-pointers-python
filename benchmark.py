"""Time the brute force pair sum against the two pointers version."""

from collections.abc import Callable
from time import perf_counter

from brute_force import pair_sum_brute
from two_pointers import pair_with_target_sum


def time_it(
    func: Callable[[list[int], int], list[int]], nums: list[int], target: int
) -> float:
    """Return how many seconds one call to func takes."""
    start = perf_counter()
    func(nums, target)
    return perf_counter() - start


def main() -> None:
    print(f"{'n':>7}  {'nested loops':>13}  {'two pointers':>13}")
    for n in (1_000, 2_000, 4_000, 8_000):
        # Even numbers only, and an odd target: no pair can ever match, so
        # both functions have to do all of their work.
        nums = list(range(0, 2 * n, 2))
        target = 1
        slow = time_it(pair_sum_brute, nums, target)
        fast = time_it(pair_with_target_sum, nums, target)
        print(f"{n:>7,}  {slow:>12.4f}s  {fast:>12.6f}s")


if __name__ == "__main__":
    main()
