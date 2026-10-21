# Two Pointers in Python: Build and Test a Problem-Solving Toolkit

Companion code for the tutorial **Two Pointers in Python: Build and Test a
Problem-Solving Toolkit** on [EmiTechLogic](https://emitechlogic.com/two-pointers-in-python/).

Two pointers turns many O(n²) nested-loop problems into O(n) by moving two
index variables through the data by a fixed rule. In this project you build a
small toolkit of two-pointers functions, check each one against a slow
brute-force version on thousands of random inputs, and measure how much faster
they are.

## What is inside

| File | What it does |
| --- | --- |
| `two_pointers.py` | The toolkit: pair sum on a sorted list, reverse in place, palindrome check, remove duplicates, merge two sorted lists, and three sum. |
| `brute_force.py` | Slow, obviously correct versions. They serve as a speed baseline and as a test oracle that the fast code must agree with. |
| `linked_list.py` | Fast and slow pointers: find the middle node of a singly linked list. |
| `practice.py` | Three practice problems: is subsequence, squares of a sorted array, and container with most water. |
| `pitfalls.py` | Two buggy pair sums (`<=` instead of `<`, and a missing pointer move), kept so tests can show how they fail. |
| `benchmark.py` | Times the nested-loop pair sum against the two pointers version. |
| `test_two_pointers.py` | 41 tests for the toolkit, including random cross-checks against brute force. |
| `test_linked_list.py` | 7 tests for the linked-list middle. |
| `test_practice.py` | 21 tests for the practice problems. |
| `test_pitfalls.py` | 3 tests that show the two bugs. |
| `requirements.txt` | The one dependency: `pytest`. |

## Requirements

- Python 3.9 or newer (tested on Python 3.13)
- `git`, to clone the project
- `pytest`, installed in the steps below

The code uses only the standard library, apart from `pytest` for the tests.

## Quick start

### 1. Clone the repository

```console
$ git clone https://github.com/Emmimal/two-pointers-python.git
$ cd two-pointers-python
```

### 2. Create and activate a virtual environment

On macOS and Linux:

```console
$ python3 -m venv venv
$ source venv/bin/activate
```

On Windows (Command Prompt):

```console
> python -m venv venv
> venv\Scripts\activate
```

On Windows (PowerShell):

```console
> python -m venv venv
> venv\Scripts\Activate.ps1
```

When the environment is active, your prompt starts with `(venv)`.

### 3. Install the dependency

```console
(venv) $ python -m pip install -r requirements.txt
```

### 4. Run the tests

```console
(venv) $ python -m pytest
```

You should see all 72 tests pass:

```text
........................................................................ [100%]
72 passed in 0.12s
```

### 5. Run the benchmark

```console
(venv) $ python benchmark.py
```

Here is one run on Python 3.13:

```text
      n   nested loops   two pointers
  1,000        0.0278s      0.000096s
  2,000        0.1266s      0.000184s
  4,000        0.4222s      0.000355s
  8,000        2.1651s      0.000729s
```

Your times will differ, and individual runs are noisy, but the shape should
hold. Each time `n` doubles, the nested loops take roughly four times as long,
which is the signature of O(n²). The two pointers time roughly doubles, which is
O(n).

## Try it yourself

Use the toolkit directly in a Python session:

```pycon
>>> from two_pointers import pair_with_target_sum, three_sum, is_palindrome
>>> pair_with_target_sum([1, 3, 5, 8, 11], 13)
[2, 3]
>>> three_sum([-1, 0, 1, 2, -1, -4])
[[-1, -1, 2], [-1, 0, 1]]
>>> is_palindrome("A man, a plan, a canal: Panama")
True
```

Find the middle of a linked list with fast and slow pointers:

```pycon
>>> from linked_list import find_middle, from_values
>>> find_middle(from_values([1, 2, 3, 4, 5])).val
3
```

Run a single test file, or a single test:

```console
(venv) $ python -m pytest test_two_pointers.py
(venv) $ python -m pytest test_two_pointers.py -k three_sum
```

## The three pointer patterns

| Pattern | Where the pointers start | How they move | Functions in this project |
| --- | --- | --- | --- |
| Opposite direction | Both ends | Move toward each other | `pair_with_target_sum`, `reverse_in_place`, `is_palindrome`, `three_sum`, `sorted_squares`, `max_area` |
| Same direction | Near the start | Both move forward, one faster than the other | `remove_duplicates`, `merge_sorted`, `is_subsequence` |
| Fast and slow | The same place | One moves 1 step, the other moves 2 | `find_middle` |

## Two things to remember

- **Pair sum needs sorted input.** On an unsorted list, the "too small, move
  left" rule is no longer true, and the function can miss a pair that exists.
  `test_pair_sum_gives_wrong_answers_on_unsorted_input` shows an example.
- **Every branch must move a pointer or return.** Otherwise the loop never ends.
  `pitfalls.py` and `test_pitfalls.py` show this bug and the `<=` bug safely.

## Project layout

```text
two-pointers-python/
├── README.md
├── requirements.txt
├── two_pointers.py
├── brute_force.py
├── linked_list.py
├── practice.py
├── pitfalls.py
├── benchmark.py
├── test_two_pointers.py
├── test_linked_list.py
├── test_practice.py
└── test_pitfalls.py
```

All modules sit in one folder, so every import is a plain module name. Run all
commands from the project folder.

## Troubleshooting

**`ModuleNotFoundError: No module named 'two_pointers'`**
You are running a command from the wrong folder. Run `cd two-pointers-python`
first, then run the command again.

**`No module named pytest`**
The virtual environment is not active, or the dependency is not installed.
Activate the environment (step 2), then run
`python -m pip install -r requirements.txt`.

**`python: command not found`**
On some systems the command is `python3`. Use `python3` in place of `python`
for the commands above.

**PowerShell refuses to run `Activate.ps1`**
Allow scripts for this session with
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`, or use
Command Prompt instead.

**The benchmark times differ from the README**
That is expected. Timings depend on your machine and change from run to run.
Look at the trend as `n` doubles, not the exact numbers.

## Read the full tutorial

The step-by-step explanation behind this code, including the trace of the pair
sum, the decision flow for when two pointers does not work, and the practice
problems, is in the tutorial on EmiTechLogic:

[Two Pointers in Python: A Complete Problem-Solving Guide
](https://emitechlogic.com/two-pointers-in-python/)

## Author

Written by Emmimal P. Alexander at [EmiTechLogic](https://emitechlogic.com/).
