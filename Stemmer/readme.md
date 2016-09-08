# Stemmer

The stemmer outputs the stemme version of an input pali sentence. The API is Pali-NLP-Stemmer-wordClassStemmer.stem()  

```shell
import wordClassStemmer

sentence='Eva.m me suta.m - eka.m samaya.m bhagavaa antaraa ca raajagaha.m antaraa ca naa.landa.m addhaanamaggappa.tipanno hoti mahataa bhikkhusa"nghena saddhi.m pa~ncamattehi bhikkhusatehi. Suppiyopi kho paribbaajako antaraa ca raajagaha.m antaraa ca naa.landa.m addhaanamaggappa.tipanno hoti saddhi.m antevaasinaa brahmadattena maa.navena.'

wordClassStemmer.stem(sentence)
Out[48]: 'Ev  sut -  samay bhagav antar c raajagah antar c naa.land addhaanamaggappa.tipann hot mahat bhikkhusa"ngh saddhi.m pa~ncamatt bhikkhusatehi. Suppiyop kh paribbaajak antar c raajagah antar c naa.land addhaanamaggappa.tipann hot saddhi.m antevaasin brahmadatt maa.navena.'

wordClassStemmer.stem('namo thassa bhagavato arahatho sammasambhuddhassa')
Out[49]: 'nam th bhagav arahath sammasambhuddh'
```


The process involves a few steps. 

The word class (noun, verb, adj....) of the input word is checked first.
The same word may belong to multiple word classes.
Hence a list of possibilities is returned. 

If no possibilities are identified, the ending of given word is compared with all 
available word endings and if matched, it is removed. This process is carried 
out recursively. 

If word class is identified, we consider each word class separately. 
Lists of endings for each word class are generated separately, and those endings
are compared with the word. If matching, the word is stemmed.
A list of possible stems is returned. Mostly, each separate case returns the same
stem. This method improves accuracy of stemming.  

