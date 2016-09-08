#Word Class Stemmer: returns the stem of a given word

import sys
sys.path.insert(0, './endings')
import regularEndings
import wordClassGuesser
import endings

wcg=wordClassGuesser.guessWordClassFromLemma
retainEndings=endings.retainEndings


#recursive function to keep stemming a word
def stemRecursive(word,ends):
    for end in ends:
        if (word.endswith(end)):
            index = word.rindex(end)
            return stemRecursive(word[0:index],ends)
    return word


#final algorithm to stem a given word
#returns the stemmed word
def stemOne(word,out=[]):
    out=[]
    wordClasses=(wcg(word))
    if (len(wordClasses) == 0):
        out.append(stemRecursive(word,"all"))
        return out
    for pos in wordClasses:
        endings=retainEndings(pos)
        if len(endings)==0:
            endings=retainEndings("all")
        out1=set()
        out1.add(stemRecursive(word,endings))
    out=list(out1)
    return out
    
#final algorithm to stem a sentence
#returns the stemmed sentence
def stem(sentence):
    inp=sentence.split()
    out=''
    for i in range(len(inp)):
        out+=stemOne(inp[i])[0]+' '
    return out.strip()

