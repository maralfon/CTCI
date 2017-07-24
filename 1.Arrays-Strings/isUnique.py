# Additional Data Structures
def isUnique(string):
    chars = set()
    for char in string:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True

# No Additional Data Structures
def isUniqueNAD(string):
    sorted_string = sorted(string)
    length = len(sorted_string)
    for index in range(length):
        if index < length - 1:
            if string[index] == string[index + 1]:
                return False
    return True
