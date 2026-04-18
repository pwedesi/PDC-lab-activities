"""Lab 6 evaluation pipeline: dataset generation and timing for sort/search tasks."""

from __future__ import annotations

import random
import time
from typing import Callable

from search import linear_search, parallel_linear_search
from sort import merge_sort, parallel_merge_sort

DATASET_SIZES = (1_000, 100_000, 1_000_000)
SIZE_LABELS = {1_000: "small", 100_000: "medium", 1_000_000: "large"}
RANDOM_RANGE = (1, 1_000_000)


def random_integers(n: int) -> list[int]:
    lo, hi = RANDOM_RANGE
    return [random.randint(lo, hi) for _ in range(n)]


def reverse_sorted_integers(n: int) -> list[int]:
    # special case
    return sorted(random_integers(n), reverse=True)


def _time_call_value(fn: Callable[[], object]) -> tuple[float, object]:
    start = time.perf_counter()
    value = fn()
    elapsed = time.perf_counter() - start
    return elapsed, value


def _is_sorted(nums: list[int]) -> bool:
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))


def run_sort_benchmark(label: str, data: list[int]) -> None:
    n = len(data)
    print(f"\n--- Sorting — {label} ---")

    t_seq, seq_out = _time_call_value(lambda: merge_sort(data))
    print(f"  merge_sort (sequential):     {t_seq:.6f} s")

    t_par, par_out = _time_call_value(lambda: parallel_merge_sort(data))
    print(f"  parallel_merge_sort:         {t_par:.6f} s")

    if n <= 10_000:
        print(f"  correctness (seq sorted):    {_is_sorted(seq_out)}")
        print(f"  correctness (par sorted):    {_is_sorted(par_out)}")
        print(f"  seq vs par same output:      {seq_out == par_out}")


def run_search_benchmark(label: str, data: list[int]) -> None:
    n = len(data)
    target = data[n // 2] if n else 0
    print(f"\n--- Searching — {label} (target = index n//2) ---")

    t_seq, i_seq = _time_call_value(lambda: linear_search(data, target))
    print(f"  linear_search (sequential):     {t_seq:.6f} s")

    t_par, i_par = _time_call_value(lambda: parallel_linear_search(data, target))
    print(f"  parallel_linear_search:        {t_par:.6f} s")

    print(f"  same index (seq vs par):     {i_seq == i_par} (seq={i_seq}, par={i_par})")


def run_full_suite_for_data(label: str, data: list[int]) -> None:
    run_sort_benchmark(label, data)
    run_search_benchmark(label, data)


def main() -> None:
    random.seed(42)

    print("Lab 6 — Sorting & searching evaluation")
    print(f"Random integer range: {RANDOM_RANGE[0]}..{RANDOM_RANGE[1]}")

    for n in DATASET_SIZES:
        data = random_integers(n)
        label = f"random — {SIZE_LABELS[n]} (n={n:,})"
        run_full_suite_for_data(label, data)

    special_n = 100_000
    special = reverse_sorted_integers(special_n)
    run_full_suite_for_data(
        f"special case — reverse-sorted random integers (n={special_n})",
        special,
    )


if __name__ == "__main__":
    main()
