def flatten(mylist):
    flatlist = []
    for element in mylist:
        if type(element) == list:
            flatlist += flatten(element)
        else:
            flatlist += element
    return flatlist

print(flatten(['a', ['b', ['c', ['d']], 'e'], 'f']))