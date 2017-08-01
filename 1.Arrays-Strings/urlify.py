def urlify(string):
    result, url = "", "%20"
    for char in string:
        if char == " ":
            result = result + url
        else:
            result = result + char
    return result
