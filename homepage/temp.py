# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
# import functions
# from config import max_letters, language_tags

def convert_dic_to_vector(dic, max_word_length):
    new_list = []
    for word in dic:
        vec = ''
        n = len(word)
        for i in range(n):
            current_letter = word[i]
            ind = ord(current_letter)-2688
            placeholder = (str(0)*ind) + str(1) + str(0)*(126-ind)
            vec = vec + placeholder
        if n < max_word_length:
            excess = max_word_length-n
            vec = vec +str(0)*127*excess
        new_list.append(vec)
    return new_list

max_letters = 8
language_tags = {

                'ahmedabadi':['કેમ', 'કર્યા', 'જશે', 'વિજય', 'આવા', 'દેખાય', 'જોઈ', 'કામ', 'રખાય','અહીંયા',
                  'જઈને', 'હિન્દી', 'ખુલ્લું', 'મને', 'થવાનો', 'કહીને', 'ઘણો', 'ના', 'દૂર', 'પરાણે', 'જોઈએ',
                  'રહ્યા', 'કરના', 'તેને', 'ચાલો', 'બાકી', 'ક્યારે', 'ચાલ', 'પેલી', 'કોઈની', 'દેખાતી', 'ક્યાંય', 'કંઈક',
                   'કેમનું', 'બધી', 'મળશે', 'એટલું', 'કરાય', 'જતાં', 'શોધવો', 'રાખવું', 'ફરી', 'જતો', 'ફોન', 'ચાલતાં', 'તૈયાર',
                       'હથેળીઓ', 'રહેતો', 'પાણીના', 'શોધતા', 'ખુલ્લુ', 'સાથે', 'હોય', 'કરે', 'શકે', 'ચાલ્યા', 'હતા', 'પાણીને',
                     'ગયો', 'થોડું', 'બીજો', 'કરશો', 'થઈ', 'ઘણું', 'ઘરે', 'ને','અત્યારે', 'આવવાના'],

                'charotari': ['રહેશે', 'જતા', 'કંઈ', 'કોઈ', 'કરીશું', 'નહી', 'ત્યાં', 'પાસે', 'જાઓ', 'તે', 'એટલે', 'મળ્યો', 'ના', 'જે', 'પાછા',
                 'ક્યાંક', 'આવવા', 'વિદ્યાર્થી', 'રહેજે', 'કઈ', 'તેની', 'પડશે', 'બહુ', 'પ્રચારો', 'આવ્યા', 'પેલી', 'અહીંથી', 'દેખાતું',
                  'જઈ', 'જાઉં', 'મારે', 'મળશે', 'શોધવો', 'ફૂલો', 'એને', 'લખવાનું', 'શકીશ', 'ક્યાં', 'રસ્તો', 'શોધ્યો', 'જતી','ચલ',
                   'આવે', 'સાથે', 'હોય', 'છોડતા', 'પાણી','ક્યારેય', 'મેં', 'ગયો', 'થોડું', 'બીજો', 'થઈ', 'દુર', 'લઈને', 'ઘરે', 'અત્યારે', 'અહીં'],

                'surati': ['કશે', 'કેવી', 'નીકળ્યો', 'પૂર્ણિમાએ','ગામની', 'કેટલું', 'તને', 'જવું', 'પાછા', 'ગયા', 'એવી', 'કઈ', 'પહેલી', 'એમણે',
                 'આવ્યા', 'ચાલ', 'પેલી', 'પહેલા', 'કરાવી', 'મારે', 'પાછળ', 'ધ્યાન', 'ગરમ', 'મળવા', 'જવાય', 'કરવુ', 'ચાલની',
                  'પરસ્પરની', 'ન', 'હતો', 'આવ્યો','ક્યાં', 'બોલાયેલા', 'બોલ', 'સાથે', 'બીજું','કરે', 'રાખો', 'પાણી', 'ચાલ્યા', 'નામાવલી', 'ગયો',
                   'કરીએ', 'મસ્તી', 'લઈને', 'ની', 'આયોજન'],

                'mahesani': ['છેડો', 'ચંપલ', 'તેના', 'કરાવે', 'કોઈને', 'કાઢવો', 'હેડો', 'પાછો', 'જતું', 'ત્યાં', 
                'પાસે', 'આવવું', 'તે', 'ચમચી', 'નક્કી', 'રેડિયો', 'રે', 'પહોંચી', 'હેડતા', 'મૂળ', 'પહોંચાય', 'અંધારું', 'કેટલું', 'ચવેલી', 
                'જીઓ', 'વીતી', 'તને', 'આપણો', 'પ્રથમ', 'એવું', 'કહીએ', 'જોઈતી', 'જે', 'ગીતા', 'રેલ્વે', 
                'કોલેજો', 'કાલ', 'કાર્બોહાઈડ્રેટ', 'કરો', 'એલચી', 'હોળી', 'થી', 'પોર્ન', 'કોમ', 'રહેજે', 'થકી', 'કઈ',
                 'થશે', 'જવાબદારીને', 'વહી', 'બહુ', 'જોડે', 'પેલી', 'અહીંથી', 'નંગા', 'ગઢડા',
                   'કીધા', 'ત્યારે', 'અથડાઈ', 'રહેવાનો', 'રંગ', 'મળતો', 'કન્યાવિદાય', 'ઊભો', 'રહે', 'મળશે', 'એટલું',
                   'હેડ', 'ફુવારા','અલ્યા', 'ખેડૂતોના', 'જોવું', 'રાખવું', 'માટે', 'તેનો', 'ચોક', 'કરવાનું', 'ફરી', 'કોમના', 'તમે', 'જતો',
                    'રહી', 'કેશ', 'સિંચાઈ', 'હતો', 'ફઈ', 'રહ્યો', 'પૂર્ણ', 'સારા', 'આપણાં', 'વળી', 'જતી', 'એના',
                     'આવે', 'વખતે', 'આવું', 'હોય', 'રાખો', 'અથવા', 'આગળ', 'ગામના', 'પીઠ','પાણી', 'શકીએ', 'ઘડવૈયો', 'કર્યું', 'દીધી',
                      'જાય', 'હતા', 'હોદ્દા', 'વત્તા', 'આપેલી', 'ખુશી', 'થોડું', 'બીજો', 'દુર', 'થયા', 'ઘણું', 'લઈને', 'ઘરે', 'વાતોને', 'ની',
                       'અત્યારે', 'રહો', 'આવવાના', 'અહીં','પરોલી'],

                'kathiyavadi': ['કરાવે', 'વખત', 'શક્ય', 'શોધવા', 'અરે', 'કંઈ', 'ભરેલા', 'ખૂબ', 'કેને', 'યે', 'ત્યાં',
                 'ભટકાઈ', 'જાઓ', 'જ્યાં', 'પિતા', 'ફંટાઇ','તંદુરસ્ત', 'આપણો', 'ના', 'જે', 'વયા', 'ગયા', 'આવવા', 'એટલો',
                  'કરો', 'અલી', 'હાલતાં', 'આવતી', 'કરાવ્યો', 'જાણે', 'કઈ', 'કાઢી', 'વહી', 'કેટલો', 'જાહે',
                    'આયા', 'આવ્યા', 'અહીંથી', 'નવો', 'શકાય', 'એજ', 'અલા', 'જઈ', 'તેમ', 'મેને',
                    'ગોતો', 'લઈ', 'નિકલ', 'છતાંયે', 'મળશે', 'એટલું', 'જોયા', 'બીજા', 'અલ્યા', 'જાવાની', 'રાખવું', 'નકલી',
                     'બધો', 'ધરા', 'આપણા', 'કરતાં', 'ગોતા', 'વાંચીએ', 'એવા', 'રહી', 'હારે', 'ખુલ્લી', 'પારસ', 'રખાયું',
                      'રજાઓમાં', 'હતો', 'આવતા', 'ગામ', 'સારા', 'હજારો', 'બોલ', 'તહેવાર', 'જાતા', 'જગ્યાએ', 'તારે', 
                      'આવે', 'કરવો', 'હોય','અગ્નિ', 'પાણી', 'શકીએ', 'હાલ', 'જાય', 'ઓલી', 'નહિતર', 'જડી', 'હતા', 'હાલો', 'ખરા', 'જાશે',
                       'જોતા','ગયો', 'થોડું', 'બીજો', 'થયો', 'કરશો', 'છેવટે', 'ઘણું', 'એમ', 'લઈને', 'ઘરે', 'ને', 'વયો', 'કામનો']

                 }


network = Sequential()
network.add(Dense(900, input_dim=127*max_letters, activation='sigmoid'))
network.add(Dense(600, activation='sigmoid'))
network.add(Dense(300, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dense(len(language_tags), activation='softmax'))
network.load_weights('weights.hdf5')
network.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])

def predict(text):
    lst = text.split()
    for i in lst:
        dic = []
        valid = False
        while not valid:
            # word = input('Enter word to predict:\n')
            word = i
            if len(word) <= max_letters:
                word = word.lower()
                valid = True
            else:
                print('Word must be less than ' + str(max_letters + 1) + ' letters long')
        dic.append(word)
        vct_str = convert_dic_to_vector(dic, max_letters)
        vct = np.zeros((1, 127 * max_letters))
        count = 0
        for digit in vct_str[0]:
            vct[0,count] = int(digit)
            count += 1
        prediction_vct = network.predict(vct)
        tmp = 0
        langs = list(language_tags.keys())
        for i in range(len(language_tags)):
            lang = langs[i]
            score = prediction_vct[0][i]
            if(tmp < score):
                tmp = score
        print(lang + ': ' + str(round(100*tmp, 2)) + '%')
        print('\n')