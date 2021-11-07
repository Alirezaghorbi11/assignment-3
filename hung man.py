import os
from random import randint
from os import system
import random


word_bank = ['apple' , 'chelsea' , 'sowp' , 'bitcoin' , 'top' , 'printer' , 'sxp' , 'skirt' , 'cardano' , 'alireza'] 



array_choose = []
counter_win = 1
life = ['💕','💕','💕','💕','💕']


while True :
    os.system("clear")
    print('╒══════════════════════════════════════════════╕')
    print('│⟹  ➊ - New Game                               │')
    print('│⟹  ➋ - Exit                                   │')
    print('╘══════════════════════════════════════════════╛\n')
    menu_1 = input('\n\tPlease Choose one of them : ')
    os.system("clear")
    if menu_1 == '1' :
        user_true_char = []
        counter_win = 0
        life = ['💕','💕','💕','💕','💕']
        word = random.choice(word_bank)
        if word in array_choose :
            while word in array_choose :
                word = random.choice(word_bank)
        array_choose.append(word)

        while True:
            os.system("clear")
            print('\n╒════════════════════════════╕')
            print('│',end='')
            for i in range (len(life)) :
                print('  ' ,life[i],end='')
            print('   │                           ',end='')
            
            for i in range(len(word)):
                #print(' ')
                if word[i] in user_true_char :
                    print(word[i] , end='')
                elif word[i]==' ' :
                    print(' ' , end='')
                else:
                    print('-' , end='')
            
            print('\n╘════════════════════════════╛\n')
            if life != [] and counter_win < len(word)
 :
                user_char = input('\nPlz enter a char :  ')
                if user_char in word:
                    print('Yes')
                    user_true_char.append(user_char)
                    counter_win +=1
                else:
                    life.pop()
                    print ('No')

            if life == []:
                os.system("clear")
                print('\n╒════════════════════════════╕')
                print('│        Game Over         │')
                print('╘════════════════════════════╛\n')
                pause = input()
                array_choose = []
                break

            if counter_win >= len(word)
 :
                os.system("clear")
                print('\n╒════════════════════════════╕')
                print('│        You win              │')
                print('╘════════════════════════════╛\n')
                pause = input()
                break
    elif menu_1 == '2':
        exit(0)
