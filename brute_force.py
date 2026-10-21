"""Slow but obviously correct solutions, used as a baseline and as a test oracle."""


def pair_sum_brute(nums: list[int], target: int) -> list[int]:
    """Return positions of two numbers that add up to target, or []."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def three_sum_brute(nums: list[int]) -> list[list[int]]:
    """Return all unique triplets that add up to zero, each sorted."""
    n = len(nums)
    found: set[tuple[int, int, int]] = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    smallest, middle, largest = sorted((nums[i], nums[j], nums[k]))
                    found.add((smallest, middle, largest))
    return [list(triplet) for triplet in sorted(found)]
