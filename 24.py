# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:32:39 2023

@author: prafu

"""

import re
sentence5="sharat twitted , Wittnessing 70th republic day India  from Rajpath, \new-Delhi , memorizing performance by Indian Army!"
re.sub(r'([^\s\w]|_)+',' ',sentence5).split()
# extracting n-grams
#n-gram can be extracted using three technique
#1 cluster defined function
#2 NLTK
#3 TextBlob

###################################
#extracting n-grams using custom defined function

import re
def n_gram_extractor(input_str,n):
    tokens =re.sub(r'([^\s\w]|_)+',' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
        

n_gram_extractor("The cute little boy is playing with kitten",2)
n_gram_extractor("The cute little boy is playing with kitten",3)

#----------------------------------------------------------------------------------------------------
import nltk
from nltk import ngrams
#extracting n-grams with nltk
list(ngrams("The cute little boy is playing with kitten",2))
list(ngrams("The cute little boy is playing with kitten",3))

#----------------------------------------------------------------------------------------------------

from textblob import TextBlob
blob=TextBlob("The cute little boy is playing with kitchen.")
blob.ngrams(n=2)
blob.ngrams(n=3)

#----------------------------------------------------------------------------------------------------


# tokenization using keras

sentence5
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence((sentence5))

#######################################################################


#tWEET TOKENIZER

from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer(sentence5)


########################################################################


# multi word expression

from nltk.tokenize import MWETokenizer
sentence5
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace(',', ' ').split())

###########################################################################

# Regular expression tokenizer
sentence5
from nltk.tokenize import RegexpTokenizer

tokenizer=RegexpTokenizer('\w+|\$[\d.]+|\s+')
tokenizer.tokenize(sentence5)

#######################################################################
# white space tokenizer

from nltk.tokenize import WhitespaceTokenizer
wh_tokenizer=WhitespaceTokenizer()
wh_tokenizer.tokenize(sentence5)


####################################################################

from nltk.tokenize import WordPunctTokenizer
wh_tokenizer=WordPunctTokenizer()
wh_tokenizer.tokenize(sentence5)

########################################################################


# stemmer

sentence6="I love playing cricket.Cricket players prictices hard in training "
from nltk.stem import RegexpStemmer
regex_stemmer=RegexpStemmer('ing$')
' '.join(regex_stemmer.stem(wd)for wd in sentence6.split())


############################################################################

sentence7="Before eating ,it would be nice to sanitize your hand"
from nltk.stem.porter import PorterStemmer
ps_stemmer=PorterStemmer()
words=sentence7.split()
" ".join([ps_stemmer.stem(wd) for wd in words])


###############################################################################

##Lematization

import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
nltk.download('wordnet')

lemmatizer=WordNetLemmatizer()
sentence8="The codes executed today are far better than what  executed"
words=word_tokenize(sentence8)
" ".join([lemmatizer.lemmatize(word) for word in words])


############################################################################

import nltk 

from textblob import TextBlob
sentence9=TextBlob("she sells sashells on the seashore")
words=sentence9.words


# we want to make words[2] i,e seashell in singular

sentence9



#################################################################

# custom stopword removal

from nltk import word_tokenize
sentence9="she sells seashells on seashore"
custom_stop_word_list=['She','On','the','am','is']
words=word_tokenize(sentence9)
" ".join([word for word in words if word.lower() not in custom_stop_word_list])




















