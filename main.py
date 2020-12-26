import random
from random import randint
from PyDictionary import PyDictionary
from termcolor import colored

dictionary=PyDictionary()

lines = open('dictionary.txt').read().splitlines()
myline =random.choice(lines)
#print(myline)
# words = ['hello', 'hi', 'asdf', 'joe', 'ginger']
wordInDoc = str.lower(myline)
print(wordInDoc)
#print(len(wordInDoc))
word = []
displayWord = []

def split(word):
    return [char for char in word]

# for x in range(len(wordInDoc)):
#     print('_', end=' ')

#line break
# print('')

word = split(wordInDoc)


wordLen = 0
for x in range(len(wordInDoc)):
    displayWord.append('_ ')
    wordLen += 1



def userInput():
    guess = input('Letter? ')
    str.lower(guess)

displayWordComp = ''


print(displayWord)

#wordLen = 0
while True:
    displayWordComp = ''
    displayWordComp = displayWordComp.join(displayWord)


    if wordInDoc != displayWordComp:
        print('')
        guess = input('Letter? ')
        str.lower(guess)
        wordLen = 0
    #for x in range(len(wordInDoc)):
        #print(word[wordLen])
    
    #dispWordCompDube = displayWord
    
        for x in range(len(wordInDoc)):
            
            # print('')
            # print(guess)
            #print(wordLen)
            # print(word[wordLen])
            if guess in word[wordLen]:
                #print('it worked')
                
                #print(displayWord)
                    
                #print(wordLen)

                del displayWord[wordLen]

                displayWord.insert(wordLen, guess)

                
                displayWordlen = wordLen
                
                print(displayWord)
                #print(displayWord[displayWordlen], end=' ')
                wordLen += 1
                #line break
                #print('')        

            else:
                #print('nope')
                wordLen += 1

            #break
    else:
        print('')
        print(colored('Y', 'red',), colored('o', 'blue'), colored('u', 'green'), ' ', colored('W', 'cyan'), colored('o', 'magenta'), colored('n', 'yellow'), colored('!', 'white'))
        

        #Gives Definition of the word

        #wordInDocDef = dictionary.meaning(wordInDoc)
        #print(wordInDocDef)
        break
            
    




