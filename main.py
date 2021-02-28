import FileUtils

def splitDictionariesBySimilaryAndDifference( pfsPath , sjpPath ):
    parsedPFS = FileUtils.getParsePFSDictionaryFile(pfsPath)
    sjpDictionary = FileUtils.getSJPDictionary(sjpPath)
    return FileUtils.getSimilaryAndUnique(parsedPFS,sjpDictionary)




if __name__ == '__main__':
    pfsPath = "testPFS.txt"
    sjpPath = "testSJP.txt"
    [same,pfsUnique,sjpUnique] = splitDictionariesBySimilaryAndDifference(pfsPath,sjpPath)
    FileUtils.printToFile(same,"same.txt")
    FileUtils.printToFile(pfsUnique,"pfsUnique.txt")
    FileUtils.printToFile(sjpUnique,"sjpUnique.txt")



