def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

list1 = [1, 2, 4]
list2 = [1, 3, 4]
print("Merged Sorted List:", merge_sorted_lists(list1, list2))
