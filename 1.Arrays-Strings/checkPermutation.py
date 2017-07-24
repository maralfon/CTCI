def checkPermutation(string1, string2):
    sorted1, sorted2 = sorted(string1), sorted(string2)
    for index in range(len(sorted1)):
        if not sorted1[index] == sorted2[index]:
            return False
    return True

def checkPermutationAlt(string1, string2):
    counts1, counts2 = generate_dict(string1), generate_dict(string2)
    for key, values in counts1.copy().items():
        if (key in counts1) and (key in counts2) and (counts1[key] == counts2[key]):
            del counts1[key]
            del counts2[key]
        else:
            return False
    return counts1 == counts2

def generate_dict(string):
    counts = {}
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
