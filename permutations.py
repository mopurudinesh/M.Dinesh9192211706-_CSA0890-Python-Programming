def get_permutations(arr):
    if len(arr) == 1:
        return [arr]

    permutations = []
    for i, num in enumerate(arr):
    
        remaining = arr[:i] + arr[i+1:]
        
        
        for perm in get_permutations(remaining):
            permutations.append([num] + perm)

    return permutations
arr = [1, 2 , 3 , 41 , 3 , 23]
permutations = get_permutations(arr)
for perm in permutations:
    print(perm)