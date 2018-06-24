#Exercise files for dictionaries...

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
def howmany(aDict):

    result = 0
    values = aDict.values()
    for i in values:
        result += len(i)
    return result

def finder(aDict):
    values = aDict.values()
    result = []
    for i in values:
        result.append(i)
    return result

def bigegst(aDict):
    best = max(finder(aDict))
    big = []
    if len(aDict) > 0:
        for i in aDict:
            print("i is: " + i)
            if aDict[i] == best:
                print("adict(i) is: " + str(aDict[i]))
                big.append(i)

        return big[]
    else:
        return None
asd = {}
finder(asd)