import FileUtils
import CurlReader
import SjpWrapper
import sys
import time
import subprocess

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
    FileUtils.truncJsonFile(dictionaryName)
    a_file = open("Output/"+dictionaryName,"r", encoding="utf8")
    lines = a_file.readlines()
    webiste = "https://www.sjp.pl/"
    print("\nProcessing",dictionaryName," : ...")
    start = time.time()
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
    end = time.time()
    during = end - start
    print("Fill ",dictionaryName,"\ntakes time: ",during)

if __name__ == '__main__':

    if CurlReader.testSjpSite() == False:
        print("Problem with sjp site, check connection to sjp.pl")
    else:
        if len(sys.argv[1:]) == 2:
            sjpPath = str(sys.argv[1:][0])
            sjpLine = int(subprocess.check_output(["wc", "-l", "Input/"+sjpPath]).decode("utf8").split()[0])
            pfsPath = str(sys.argv[1:][1])
            pfsLine = int(subprocess.check_output(["wc", "-l", "Input/"+pfsPath]).decode("utf8").split()[0])
            print("Start to process lines: \nsjp:",sjpLine," lines\npfs:",pfsLine," lines")
            [same,pfsUnique,sjpUnique] = splitDictionariesBySimilaryAndDifference(pfsPath,sjpPath)
            FileUtils.printToFile(same,"same.txt")
            FileUtils.printToFile(pfsUnique,"pfsUnique.txt")
            FileUtils.printToFile(sjpUnique,"sjpUnique.txt")
            sameLinesCount = int(subprocess.check_output(["wc", "-l", "Output/same.txt"]).decode("utf8").split()[0])
            pfsUniqueCount = int(subprocess.check_output(["wc", "-l", "Output/pfsUnique.txt"]).decode("utf8").split()[0])
            sjpUniqueCount = int(subprocess.check_output(["wc", "-l", "Output/sjpUnique.txt"]).decode("utf8").split()[0])
            print("\nSplitted dictionaries on:\nSame in two dictionaries: ",sameLinesCount,"lines")
            print("Unique in sjp dict: ",sjpUniqueCount," lines")
            print("Unique in pfs dict: ",pfsUniqueCount," lines")
            fillDictionary("pfsUnique.txt")
            fillDictionary("same.txt")
            fillDictionary("sjpUnique.txt")
        if len(sys.argv[1:]) == 1:
            dictPath = str(sys.argv[1:][0])
            dictLine = int(subprocess.check_output(["wc", "-l", "Input/"+dictPath]).decode("utf8").split()[0])
            FileUtils.getSJPDictionary(dictPath)
            FileUtils.printToFile(FileUtils.getSJPDictionary(dictPath),dictPath)
            print("Start to process lines: ", dictLine)
            fillDictionary(dictPath)





