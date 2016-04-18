#endings of words
import sys
sys.path.insert(0, './endings')
import xml.etree.ElementTree as ET

#extractive required data from xml files
def extractTextFromElement(elementName, stringofxml,out=[]):
    tree = ET.fromstring(stringofxml)
    for child in tree.iter():
        if child.tag == elementName:
            if (child.text.strip() in out):
                pass
            else:
                out.append(child.text.strip())
    return out

#returns a list of possible word endings 
def listAllEndings():
    f=open("fullGrammar4.xml","r")
    xml01=f.read()
    endings=extractTextFromElement("ending",xml01)
    f.close()
    endings.sort(key=len,reverse=True)
    return endings
def listAllEndings1(): #repitition: to be checked later
    f=open("fullGrammar5.xml","r")
    xml02=f.read()
    endings=extractTextFromElement("ending",xml02)
    f.close()
    return endings

#returns the endings of words a particular word class only
#the input is the word class
def retainEndings(elementName,out=[]):
    if elementName in ["all"]:
        return listAllEndings()
    element="{'type': '"+str(elementName)+"'}"
    out=[]
    root=ET.parse("fullGrammar4.xml")
    tree = root.getroot()
    for child in tree:
        if str(child.attrib) in [element]:
            for child01 in child.iter():
                if child01.tag == "ending":
                    if (child01.text.strip() in out):
                        pass
                    else:
                        out.append(child01.text.strip())
    out.sort(key=len,reverse=True)
    return out



