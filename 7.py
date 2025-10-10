import time
import random

def generate_data(size=1000):
    return [random.randint(1, 1000) for _ in range(size)]

def insertion_sort(arr):
    comparisons = 0
    start = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key
    return round(time.time() - start, 5), comparisons

def merge_sort(arr):
    comparisons = 0
    start = time.time()
    
    def recursive_merge_sort(a):
        nonlocal comparisons
        if len(a) > 1:
            mid = len(a) // 2
            L, R = a[:mid], a[mid:]
            recursive_merge_sort(L)
            recursive_merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                comparisons += 1
                if L[i] < R[j]:
                    a[k] = L[i]; i += 1
                else:
                    a[k] = R[j]; j += 1
                k += 1
            while i < len(L): a[k] = L[i]; i += 1; k += 1
            while j < len(R): a[k] = R[j]; j += 1; k += 1

    recursive_merge_sort(arr)
    return round(time.time() - start, 5), comparisons

data = generate_data()

insertion_time, insertion_comparisons = insertion_sort(data.copy())
merge_time, merge_comparisons = merge_sort(data.copy())

print("\nEmpirical Comparison: Insertion vs Merge Sort")
print(f"Insertion Sort - Time: {insertion_time}s | Comparisons: {insertion_comparisons}")
print(f"Merge Sort     - Time: {merge_time}s | Comparisons: {merge_comparisons}")
