# DictionaryActualizer - Python Script
## Script to make offline version of dictionary from sjp.pl

### Before use!
This script is strict corelated with [SjpAPI](https://github.com/GHRik/SjpAPI/).
I could say: "It is the same", but there are a little difference, so go to repo above
and take info before you use this script :)!!
This version is very low performance. I dont test how many time is to get meaning from two dictionaries.
I will be probably very, very long, about 300mins.
A "for"s functions should be parareled.






Thsi script was created to easy get all meaning of word(from txt files) from (Słownik języka polskiego)(www.sjp.pl)

## Tables of contents:
1. [ Do i need this API? ](#need)
2. [ How it works? ](#how)
3. [ Features ](#fea)
4. [ Installation ](#instal)
5. [ Using ](#using)
6. [ Examples using ](#examples)
7. [ License ](#lic)


<a name="need">.</a>
## Do i need this API?

### When you need this API:
- Get "as fresh as tropical fruit"(***ONLINE***) meaning of any word in dictionary ["słownik języka polskiego"](https://www.sjp.pl)

### When you dont need this API:
- Only need check word is in dictionary or can be used in game like scrabble.
In this case you can check any link from [there](https://sjp.pl/slownik/po.phtml)
resolve your problem.


<a name="how">.</a>
## How it works
It is correlated with [SjpAPI](https://github.com/GHRik/SjpAPI/#how) but translated to python language

<a name="fea">.</a>
## Features

- Make from you dictionary txt file, a dictionary with meaning of word and you will know
from which word your word come from:

Example
```
"kościany" is from word: "kość"
```

<a name="using">.</a>
## Using
The most important paragraph. 

For the first you MUST to have:
Please check, a format of [sjp.txt](https://github.com/GHRik/DictionaryActualizer/blob/master/Input/sjp.txt) and [psf.txt](https://github.com/GHRik/DictionaryActualizer/blob/master/Input/pfs.txt).
1. Must be ***UTF-8***
2. Only first word from line will be processed
3. If one of the above step will be missed , probably script will fail

- If you want to fill only dictionary from SJP.PL:
1. Take your dictionary in txt file, ***make sure there is in UTF-8 format***
2. Insert this file in "Input folder"
3. Call script
```
python3> DictionaryActualizer.py {NAMEOfYourTextFile}.txt
```
4. A result will be in Output folder witch name: ""fill-{NAMEOfYourTextFile}.txt

- If you have a SJP.PL dictionary and OSPS dictonary:
1. Take your dictionaries in txt file, ***make sure there is in UTF-8 format***
2. Insert this files in "Input folder"
3. Call script
```
python3> DictionaryActualizer.py {NAMEOfYourSJPDict}.txt {NAMEOfYourOSPSDict}.txt
```
4. A result willbe in:
- filled-same.txt ( The same word which was in SJP and OSPS dictonaries )
- filled-{NAMEOfYourSJPDict}.txt (Word from SJP)
- filled-{NAMEOfYourOSPSDict}.txt (Word from OSPS)


<a name="instal">.</a>
## Installation

Just clone this repo and here you are ^^

<a name="examples">.</a>
## Examples:

[Input testowo.txt](https://github.com/GHRik/DictionaryActualizer/blob/master/Input/testowo.txt) and [Output](https://github.com/GHRik/DictionaryActualizer/blob/master/Output/filled-testowo.txt)

If you clone this repo you can run this command:
```
python3> DictionaryActualizer.py sjp.txt pfs.txt
```
And after all check Output folder.
You will see a examples :D

<a name="lic">.</a>
## License
Apache
