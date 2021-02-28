import collections

def printToFile( myList, fileName ):
    with open(fileName, 'w') as f:
        for item in myList:
            f.write("%s\n" % item)

def getParsePFSDictionaryFile(filePath):
    a_file = open(filePath, encoding="utf8")
    lines = a_file.readlines()
    returnLines = list()
    for line in lines:
        returnLines.append(line.split("\t")[0].strip().lower())
    while '' in returnLines:
        returnLines.remove('')
    return returnLines


def getSJPDictionary(filePath):
    a_file = open(filePath, encoding="utf8")
    lines = a_file.readlines()
    returnLines = list()
    for line in lines:
        returnLines.append(line.strip().lower())
    while '' in returnLines:
        returnLines.remove('')
    return returnLines

def getSimilaryAndUnique( str1, str2 ):
    all = str1 + str2
    all = ([item for item, count in collections.Counter(all).items() if count > 1])
    str1 = [item for item in str1 if item not in all]
    str2 = [item for item in str2 if item not in all]
    return all,str1,str2
