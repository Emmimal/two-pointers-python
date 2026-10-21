"""Practice problems that use the same pointer patterns."""


def is_subsequence(short: str, long: str) -> bool:
    """Check whether short appears in long in order, possibly with gaps."""
    i = 0
    for char in long:
        if i < len(short) and char == short[i]:
            i += 1
    return i == len(short)


def sorted_squares(sorted_nums: list[int]) -> list[int]:
    """Square every number in a sorted list and return the squares sorted."""
    n = len(sorted_nums)
    result = [0] * n
    left, right = 0, n - 1

    # The biggest square is at one of the two ends, so fill from the back.
    for pos in range(n - 1, -1, -1):
        if abs(sorted_nums[left]) > abs(sorted_nums[right]):
            result[pos] = sorted_nums[left] ** 2
            left += 1
        else:
            result[pos] = sorted_nums[right] ** 2
            right -= 1

    return result


def max_area(heights: list[int]) -> int:
    """Return the most water that two vertical lines can hold."""
    left, right = 0, len(heights) - 1
    best = 0

    while left < right:
        height = min(heights[left], heights[right])
        best = max(best, height * (right - left))

        # The width only shrinks from here, so only a taller line can help.
        # The shorter line limits the height, so it is the one to drop.
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return best
