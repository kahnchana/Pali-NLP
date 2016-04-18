#Word Class Guesser
import sys
sys.path.insert(0, './irregular')
import irregular
from irregular import *


#guesses word class of a given lemma
#returns the guessed word class
def guessWordClassFromLemma(lemma,guesses=[]):
    guesses=[]
    
    if (isIrregularNoun(lemma)):
        return ("noun")
    elif(isIrregularNum(lemma)):
        return ("numeral")
    
    if (lemma.endswith("ti")):
        guesses.append("verb")
        
    if (lemma.endswith(("a", "aa", "i", "in", "ii", "u", "uu", "ar", "an", "ant", "as", "us", "o"))):
        guesses.append("noun")

    if (lemma.endswith(("a", "aa", "i", "ii", "u", "uu", "ant", "vaa", "maa", "at"))):
        guesses.append("adjective")

    if (lemma.endswith(( "a", "i", "a.m", "ma", "ya"))):
        guesses.append("numeral");
    
    if (lemma.endswith("u.m")):
        guesses.append("indeclinable")
        
    return guesses

    
#checks if a given lemma ends with a given ending
#returns True is so
def lemmaEndsWith(lemma,*ends):
    for e in ends:
        if (lemma.endswith(e)):
            return True

#guesses word class of a given word
#returns the guessed word class
def guessWordClassFromWord(word,guesses=[]):
    pass #to be used when lemmatizer is being built


    return False
