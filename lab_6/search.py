from concurrent.futures import ThreadPoolExecutor
from math import ceil

def linear_search(nums, target):
  """search for an element sequentially in a list"""
  for i, num in enumerate(nums):
    if num == target:
      return i
  return -1

def parallel_linear_search(nums, target, workers=4):
  """search for an element in parallelized linear search"""
  workers = max(1, min(workers, len(nums)))
  if workers == 1:
    return linear_search(nums, target)

  def search_chunk(start, end):
    for i in range(start, end):
      if nums[i] == target:
        return i
    return -1

  chunk_size = ceil(len(nums) / workers)
  ranges = [
    (start, min(start + chunk_size, len(nums)))
    for start in range(0, len(nums), chunk_size)
  ]

  with ThreadPoolExecutor(max_workers=workers) as executor:
    results = [
      future.result()
      for future in [executor.submit(search_chunk, start, end) for start, end in ranges]
    ]

  matches = [index for index in results if index != -1]
  return min(matches) if matches else -1