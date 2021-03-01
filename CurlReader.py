from pip._vendor import requests


def readCurl( https ):
    url = https
    res = requests.get(url)

    if validate(res.status_code):
        return res.content.decode("utf-8")
    else:
        return "BAD_STATUS_CODE"


def validate( status ):
    if status == 200:
        return True
    else:
        return False


def testSjpSite():
    url = "https://www.sjp.pl/"
    res = requests.get(url)

    return validate(res.status_code)
