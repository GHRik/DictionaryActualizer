import collections
import json

def printToFile( myList, fileName ):
    with open("Output/"+fileName, 'w',encoding="utf8") as f:
        for item in myList:
            f.write("%s\n" % item)
        f.close()

def truncJsonFile( myFile ):
    with open("Output/filled-"+myFile, 'w',encoding="utf8") as file:
        file.truncate(0)
        file.close()

def printJSONToFile( myJson, fileName ):
    with open("Output/filled-"+fileName, 'a',encoding="utf8") as file:
        file.write(json.dumps(myJson,ensure_ascii=False).encode('utf8').decode()+"\n")
        file.close()


def getParsePFSDictionaryFile(filePath):
    a_file = open("Input/"+filePath, 'r', encoding='utf-8')
    lines = a_file.readlines()
    returnLines = list()
    for line in lines:
        returnLines.append(line.split("\t")[0].strip().lower())
    while '' in returnLines:
        returnLines.remove('')
    a_file.close()
    return returnLines


def getSJPDictionary(filePath):
    a_file = open("Input/"+filePath, encoding="utf8")
    lines = a_file.readlines()
    returnLines = list()
    for line in lines:
        returnLines.append(line.strip().lower())
    while '' in returnLines:
        returnLines.remove('')
    a_file.close()
    return returnLines

def getSimilaryAndUnique( str1, str2 ):
    all = str1 + str2
    all = ([item for item, count in collections.Counter(all).items() if count > 1])
    str1 = [item for item in str1 if item not in all]
    str2 = [item for item in str2 if item not in all]
    return all,str1,str2
