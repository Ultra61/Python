def first_last(name):
    length = len(name)
    fchar = name[0]
    lchar = name[length - 1]
    return (fchar + lchar)
    
print(first_last('tests'))
    