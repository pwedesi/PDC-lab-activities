from multiprocessing import Pool


def _merge(left, right):
    """merge two sorted lists into one sorted list."""
    merged: list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(items):
    n = len(items)
    if n <= 1:
        return list(items)
    mid = n // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return _merge(left, right)


def parallel_merge_sort(data):
    """Sort a list of numbers using a 4-way parallel merge sort strategy."""
    if len(data) <= 1:
        return list(data)

    chunk_size = len(data) // 4
    if chunk_size == 0:
        chunk_size = 1

    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with Pool(processes=4) as pool:
        sorted_chunks = pool.map(merge_sort, chunks)

    while len(sorted_chunks) > 1:
        merged_chunks = []

        for i in range(0, len(sorted_chunks), 2):
            if i + 1 < len(sorted_chunks):
                merged_chunks.append(_merge(sorted_chunks[i], sorted_chunks[i + 1]))
            else:
                merged_chunks.append(sorted_chunks[i])

        sorted_chunks = merged_chunks

    return sorted_chunks[0]
