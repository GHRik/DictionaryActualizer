import FileUtils
import CurlReader
import SjpWrapper
import sys

def splitDictionariesBySimilaryAndDifference( pfsPath , sjpPath ):
    parsedPFS = FileUtils.getParsePFSDictionaryFile(pfsPath)
    sjpDictionary = FileUtils.getSJPDictionary(sjpPath)
    return FileUtils.getSimilaryAndUnique(parsedPFS,sjpDictionary)

def modifyDictionaryPlace( myDict ):
    newDict = dict()
    newDict["name"] = myDict["name"]
    newDict["count"] = myDict["count"]
    for index in range(0,newDict["count"]):
        newDict["variant["+str(index)+"]"] = myDict["variant["+str(index)+"]"]
        newDict["mean[" + str(index) + "]"] = myDict["mean[" + str(index) + "]"]
    return newDict


def fillDictionary( dictionaryName ):
    a_file = open("Input/"+dictionaryName,"r", encoding="utf8")
    lines = a_file.readlines()
    webiste = "https://www.sjp.pl/"
    FileUtils.truncJsonFile(dictionaryName)
    for line in lines:
        word = line
        word = word.rstrip('\n')
        https = webiste+word
        payload = CurlReader.readCurl(https)
        payload = payload.replace("\n"," ")
        myJson = SjpWrapper.wrapCurl(payload)
        myJson["name"] = word
        myJson = modifyDictionaryPlace(myJson)
        FileUtils.printJSONToFile(myJson,dictionaryName)


if __name__ == '__main__':

    if CurlReader.testSjpSite() == False:
        print("Problem with sjp site, check connection to sjp.pl")
    else:
        if len(sys.argv[1:]) == 2:
            pfsPath = str(sys.argv[1:][0])
            sjpPath = str(sys.argv[1:][1])
            [same,pfsUnique,sjpUnique] = splitDictionariesBySimilaryAndDifference(pfsPath,sjpPath)
            FileUtils.printToFile(same,"same.txt")
            FileUtils.printToFile(pfsUnique,"pfsUnique.txt")
            FileUtils.printToFile(sjpUnique,"sjpUnique.txt")
            fillDictionary("pfsUnique.txt")
            fillDictionary("same.txt")
            fillDictionary("sjpUnique.txt")
        if len(sys.argv[1:]) == 1:
            dictPath = str(sys.argv[1:][0])
            fillDictionary(dictPath)





