import re
import irregularData
import xml.etree.ElementTree as ET

#tools for extractive endings from xml files
def extractTextFromElement(elementName, stringofxml,out=[]):
    tree = ET.fromstring(stringofxml)
    for child in tree.iter():
        if child.tag == elementName:
            if (child.text.strip() in out):
                pass
            else:
                out.append(child.text.strip())
    return out

def stripb(string):
    return re.sub("[\{\[].*?[\}\]]", "", string)

#provides a list of irregualar nouns
def listIrregularNouns():
    iNoun=irregularData.irregularNoun
    iNoun=stripb(iNoun)
    iNoun=iNoun.strip().split()
    iNoun=set(iNoun)
    iNoun=list(iNoun)
    iNoun.sort(key=len)
    return iNoun

#provides a list of irregualar numerals
def listIrregularNum():
    iNum=irregularData.irregularNumeral
    iNum=stripb(iNum)
    iNum=iNum.strip().split()
    iNum=set(iNum)
    iNum=list(iNum)
    iNum.sort(key=len)
    return iNum

#checks if input word is an irregular noun
#returns true if so
def isIrregularNoun(word):
    if word in listIrregularNouns():
        return True
    return False

#checks if input word is an irregular numeral
#returns true if so
def isIrregularNum(word):
    if word in listIrregularNum():
        return True
    return False

#provides a list of indeclinables (endings) - not finalized 
def listIndeclinables():
    f=open("indeclinables.xml","r")
    xml01=f.read()
    indeclinables=extractTextFromElement("entry",xml01)
    f.close()
    return indeclinables
