def merge_and_count_vowels(str1, str2):
    merged_string = ''.join(a + b for a, b in zip(str1, str2))
    merged_string += str1[len(str2):] + str2[len(str1):]

    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in merged_string if char in vowels)

    return merged_string, vowel_count
str1 = "welcome"
str2 = "homely"
merged_string, vowel_count = merge_and_count_vowels(str1, str2)
print("Merged String:", merged_string)
print("Number of vowels:", vowel_count)