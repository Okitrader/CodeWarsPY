def vaporcode(string):
    string = string.replace('', '  ')
    return string.upper()
print(vaporcode('hello world'))