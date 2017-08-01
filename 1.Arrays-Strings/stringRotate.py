def stringRotate(string, rotated):
    return isSubstring(rotated * 2, string)

def isSubstring(string, sub):
    return sub in string

x = 'waterbottle'
y = 'erbottlewat'
