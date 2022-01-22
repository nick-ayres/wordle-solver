# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:00:54 2022

@author: Nick
"""

from english_words import english_words_lower_alpha_set

word_list = list(english_words_lower_alpha_set)

test_length = 5

filtered_word_list = list(filter(lambda w: len(w) == test_length, word_list))
#word_list[len(w) == test_length for w in word_list]

#words= list(filter(lambda w: "y" in w and "a" in w and "t" in w and "n" in w, filtered_word_list))

import random
import logging
import sys
logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
#fh = logging.FileHandler('my_log_info.log')
sh = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
#fh.setFormatter(formatter)
sh.setFormatter(formatter)
#logger.addHandler(fh)

class Puzzle:
    def __init__(self):
        self.word = ""
        
    def get_puzzle_n(self,n=0):
        self.word = filtered_word_list[n]
    
    def gen_rand_puzzle(self,length=5):
        self.word = random.choice(filtered_word_list)
        logging.info("word chosen is: " + self.word)
        #self.word = "x"*length
        return
    
    def test(self,test_word):
        assert len(test_word) == len(self.word)
        
        logging.info("test word: " + test_word)
        
        output = []
        
        for a in test_word:
            if a in self.word:
                output.append(1)
            else:
                output.append(0)
        
        #test if right position right word
        for i,(a,b) in enumerate(zip(test_word,self.word)):
            if a == b:
                output[i] = 2

        logging.info(output)
            
        
        return output
 
def filter_allowed_words(start_word_list,last_guess,last_result):
    for i,w in enumerate(start_word_list):
        for j,(l,r) in enumerate(zip(last_guess,last_result)):
            #remove wrong letter
            #maybe can replace with XOR logic but this is easier to read
            if r>0 and l not in w:
                #r > 0 means the letter in the guess was right
                start_word_list.pop(i)
                break
            if r == 0 and l in w:
                start_word_list.pop(i)
                break
            
            if r==2 and w[j] == l:
                #
                
                
            
    return 
 
def solve_puzzle(p):
    allowed_words = filtered_word_list
    
 
    
if __name__=="__main__":
    sadf = Puzzle()
    sadf.gen_rand_puzzle()
    logging.info(sadf.test(random.choice(filtered_word_list)))
    
    