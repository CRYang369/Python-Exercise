'''
Random choose the number with 1~6

'''

import random
# set the maxmum and minimum
min_val=1
max_val=6

#Contiue?
roll_again='yes'
#Loop
while roll_again=='yes' or roll_again=='y':
    print("Start roll the dice")
    print("The number of the dice is : ")

    #The first try
    print(random.randint(min_val,max_val))
    #The second try
    print(random.randint(min_val,max_val))
    #Continue?
    roll_again=input("Do you want to continue rolling the dice?(if yes,imput the yes or y)")
   