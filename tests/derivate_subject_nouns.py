#!/usr/bin/python 
# -*- coding=utf-8 -*-
#---------------------------------------------------------------------
# Name:        tashkeel 
# Purpose:     Arabic automatic vocalization. # 
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com) 
# Created:     31-10-2011 
#  Copyright:   (c) Taha Zerrouki 2011 # Licence:     GPL 
#---------------------------------------------------------------------
"""
    Arabic Tashkeel Class
"""
import sys
sys.path.append('../support')
sys.path.append('../')
import pyarabic.araby as araby
#~ import libqutrub.classverb as classverb
import libqutrub.classnoun as classnoun
import libqutrub.verb_const as verb_const 
import libqutrub.verb_valid as valid_verb 
import libqutrub.triverbtable as triverbtable
import verbs
text = u""""""


def generate_subject(verb, transitive = True, future_type= araby.FATHA):
    """
    """
    conjugator = classnoun.NounClass(verb, transitive, future_type)
    conjugated = conjugator.derivate()
    infinitive = conjugator.conjugate_tense_for_pronoun(u"الماضي المعلوم",u"هو")
    return {"infinitive":infinitive, 
              "subject":conjugated.split('\t')[0],
              "object":conjugated.split('\t')[1],
            }
def get_future_type(word):
    word_nm = araby.strip_tashkeel(word)
    v = word
    if len(word_nm) != 3:
        return araby.FATHA
    elif word_nm[1] == araby.ALEF:
        v = word_nm[0]+araby.FATHA + araby.ALEF + word_nm[2] +araby.FATHA
    elif word_nm.startswith(araby.ALEF_MAKSURA):
        v = word_nm[0]+araby.FATHA + word_nm[1] + araby.FATHA +word_nm[2]

    for i in (1,2,3,4,5,6):
        v2 = v+str(i)
        if v2 in triverbtable.TriVerbTable:
            return triverbtable.TriVerbTable[v2]['haraka']
    return araby.FATHA
        

def mainly():
    """
    main test
    """
    mode = "fa3il"
    DATA_FILE = "samples/fa3il-5.csv"
    #~ DATA_FILE = "samples/maf3oul.csv"
    #~ mode = "maf3oul"
    with open(DATA_FILE) as f:
        line = f.readline().decode('utf8')
        while line :
            if not line.startswith("#"):
                liste = line.strip('\n').split("\t")
                if len(liste) >= 2 :
            
                    correct = liste[0]
                    word = liste[1].split(';')[0]
                    transitive = True
                    future_type = get_future_type(word)
                    if valid_verb.is_valid_infinitive_verb(word,True): # vocalized
                        result = generate_subject(word,  transitive, future_type)
                        fa3il = result.get("subject", u"")
                        maf3oul = result.get("object", u"")
                        inf_verb = result.get("infinitive", word)
                        debug = False
                        #~ debug = True
                        if mode == "maf3oul":
                            if debug or not correct == maf3oul:
                                print (u"\t".join([word,inf_verb,araby.name(future_type)+future_type,maf3oul, correct, str(correct==maf3oul)])).encode('utf8')
                        else:
                            if debug or not correct == fa3il:
                                print (u"\t".join([word,inf_verb,fa3il, correct, str(correct==fa3il)])).encode('utf8')

                    else:
                        print (u"\t".join([word,"","", correct, "Invalid_Verb"])).encode('utf8')                    
            line = line = f.readline().decode('utf8')

if __name__ == "__main__":
    mainly()
    #v= u'سَاكَ'
    #future_type = get_future_type(v)
    #print future_type.encode('utf8')
    #~ words= [u"شمَّس", 
        #~ u"استعمل",
        #~ u"ضرب",
#~ u"تفعّل",
        #~ u"وعد",
        #~ u"مشى",
        #~ u"تغاضى",
        #~ u"تعانق",
        #~ u"أسرع",
        #~ u"تعجّل",
        #~ u"انفعل",
        #~ u"اقتبس",
        #~ u"اخضرّ",
        #~ u"اغرورق",
        #~ u"استوفى",
    #~ ]
    #~ for word in words:
        #~ conjugated = generate_subject(word)
        #~ print (u"\t".join([word, conjugated])).encode('utf
