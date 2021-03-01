import re
import html
from urllib.parse import unquote

def wrapCurl( curl ):
    return getFromRegex(curl)



def getFromRegex( curl ):
    regex = r"<h1[^>]*>.+?<\/h1>.<p[^>]*>.+?<.+?(?=.*)href=\"\/(.+?)\".+?znaczenie.+?<p[^>]*>(.+?)<\/p>"

    matches = re.finditer(regex, curl, re.MULTILINE)
    myJsonDict = dict()

    count = 0
    for matchNum, match in enumerate(matches, start=1):
        count += 1
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            if groupNum == 1:
                myJsonDict["variant["+str(matchNum-1)+"]"] = wrapVariantToUtf8(match.group(groupNum))
            if groupNum == 2:
                myJsonDict["mean["+str(matchNum-1)+"]"] = wrapMeanHtmlToUtf8(match.group(groupNum))
    myJsonDict["count"] = count
    return myJsonDict

def wrapVariantToUtf8(strVariant):
    strVariant = html.unescape(strVariant)
    strVariant = unquote(strVariant)
    strVariant = strVariant.replace('+', ' ')
    return strVariant


def wrapMeanHtmlToUtf8( strMean ):
    strMean = html.unescape(strMean)
    strMean = strMean.replace(u'\xa0', u' ')
    strMean = strMean.replace("<br />","\n")
    strMean = checkMeanInGoodFormat( strMean )
    return strMean

def checkMeanInGoodFormat( strMean ):
    if strMean == "KOMENTARZE:" or strMean == "POWIĄZANE HASŁA:" or hasGotSpecyficHTMLTags( strMean ) == True:
        return "BAD FORMAT"
    else:
        return strMean



def hasGotSpecyficHTMLTags( strMean ):
    regex = r"<a[^>]*>.+?<\/a>|<span[^>]*.+?<\/span>|<p[^>]*.+?<\/p>"
    matches = len(re.findall(regex, strMean))
    if matches > 0:
        return True
    else:
        return False
