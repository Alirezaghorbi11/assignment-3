from random import randint
Random_List_Number= []
len = int(input('Please enter size  array :  \n'))
while len(Random_List_Number) < len:
    Randon_number = randint (0,len)
    if Randon_number not in Random_List_Number :
        Random_List_Number.append(Randon_number)


print('Array :\n\t ', Random_List_Number)








