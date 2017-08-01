def stringCompress(string):
    count, last, result = 0, '', ''
    for char in string:
        if last == '' and count == 0 and result == '':
            last = char
            count += 1
        elif last == char:
            count += 1
        else:
            result = result + last + str(count)
            last = char
            count = 1
    result = result + last + str(count)
    if len(result) >= len(string):
        return string
    return result
