def oneAway(string, result):
    return insert(string, result) or remove(string, result) or replace(string, result)

def insert(string1, string2):
    first, second, change = 0, 0, False
    while second < len(string2):
        if string1[first] != string2[second]:
            if not change:
                change  = True
                first += 1
            else:
                return False
        else:
            first += 1
            second += 1
    return True

def remove(string1, string2):
    if len(string1) - len(string2) != 1:
        return False
    first, second = 0, 0
    while second < len(string2):
        if string1[first] != string2[second]:
            return False
        else:
            first += 1
            second += 1
    return True

def replace(string1, string2):
    if len(string1) != len(string2):
        return False
    diff_chars = 0
    for index in range(len(string1)):
        if string1[index] != string2[index]:
            diff_chars += 1
    return diff_chars == 1
