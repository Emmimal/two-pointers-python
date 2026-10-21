"""A small toolkit of two pointers solutions."""


def pair_with_target_sum(sorted_nums: list[int], target: int) -> list[int]:
    """Return positions of two numbers in a sorted list that add up to target.

    Returns an empty list when no such pair exists.
    """
    left, right = 0, len(sorted_nums) - 1

    while left < right:
        total = sorted_nums[left] + sorted_nums[right]

        if total == target:
            return [left, right]
        if total < target:
            # The list is sorted, so the left item is too small to pair with
            # anything still in play. Drop it for good.
            left += 1
        else:
            # The right item is too big to pair with anything still in play.
            right -= 1

    return []


def reverse_in_place(items: list[int]) -> None:
    """Reverse a list without creating a new one."""
    left, right = 0, len(items) - 1

    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1


def is_palindrome(text: str) -> bool:
    """Check a string, ignoring case, spaces and punctuation."""
    left, right = 0, len(text) - 1

    while left < right:
        if not text[left].isalnum():
            left += 1
            continue
        if not text[right].isalnum():
            right -= 1
            continue

        if text[left].lower() != text[right].lower():
            return False

        left += 1
        right -= 1

    return True


def remove_duplicates(sorted_nums: list[int]) -> int:
    """Remove duplicates from a sorted list in place.

    Returns how many unique items now sit at the front of the list. The
    items after that position are leftovers and should be ignored.
    """
    if not sorted_nums:
        return 0

    write = 1
    for read in range(1, len(sorted_nums)):
        # Equal values sit side by side in a sorted list, so a new value is
        # simply one that differs from the last value we kept.
        if sorted_nums[read] != sorted_nums[write - 1]:
            sorted_nums[write] = sorted_nums[read]
            write += 1

    return write


def merge_sorted(first: list[int], second: list[int]) -> list[int]:
    """Merge two sorted lists into one new sorted list."""
    i = j = 0
    merged: list[int] = []

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1

    # The loop stops when one list runs out, so at most one slice has items.
    merged.extend(first[i:])
    merged.extend(second[j:])
    return merged


def three_sum(nums: list[int]) -> list[list[int]]:
    """Return all unique triplets that add up to zero.

    The input list is not changed.
    """
    ordered = sorted(nums)
    triplets: list[list[int]] = []

    for i in range(len(ordered) - 2):
        # Skip a first number we have already used, or we repeat answers.
        if i > 0 and ordered[i] == ordered[i - 1]:
            continue

        left, right = i + 1, len(ordered) - 1
        while left < right:
            total = ordered[i] + ordered[left] + ordered[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([ordered[i], ordered[left], ordered[right]])
                left += 1
                right -= 1
                # After recording an answer, step past equal values.
                while left < right and ordered[left] == ordered[left - 1]:
                    left += 1
                while left < right and ordered[right] == ordered[right + 1]:
                    right -= 1

    return triplets
