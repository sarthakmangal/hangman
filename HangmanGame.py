# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 01:26:08 2021

@author: Sarthak Mangal
"""






import HangmanWordList
import random
import display_hangman
word = random.choice(HangmanWordList.hangman_words)


gusses = 6
blank = ""
count = 0
lst = []
for _ in range(len(word)):
    blank += "_ "
   
while gusses != 0 and ((len(word))-count) != 0:
    
    n = input("enter your gusses ")
    if n in word:
        if n not in lst:
            lst.append(n)
            for i in range(len(word)):
                if n == word[i]:
                    blank = blank[:2*i]+n+blank[((2*i)+1):]
                    count += 1 
                    
        
        print(display_hangman.display_hangman(gusses))
        print(blank)
    else:
        gusses -= 1        
        print(display_hangman.display_hangman(gusses))
        print(blank)
        print("gusses left = " + str(gusses))
        
if gusses == 0:
    print("You loose!!!")
    print("word :",word)
    
else:
    print("You win!!!")
    print("You save the innocent men!!!")
    