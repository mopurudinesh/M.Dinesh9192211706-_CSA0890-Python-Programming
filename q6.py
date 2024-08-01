def remove_duplicates(arr):
    from collections import Counter
    counter = Counter(arr)
    return sorted([num for num in arr if counter[num] == 1])

array = [15, 14, 25, 14, 32, 14, 31]
print("Sorted Array with duplicates removed:", remove_duplicates(array))
