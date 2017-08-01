def palindromePermutation(string):
    char_counts, odd = counts_chars(string), False
    for key, value in char_counts.items():
        if (value % 2 != 0) and odd:
            return False
        elif (value % 2 != 0) and not odd:
            odd = True
    return True

def counts_chars(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
