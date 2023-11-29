# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:30:28 2023

@author: Yang Cairong
"""
import random
# class player:        
#     def __init__(self,players):
#         for i in range(1,len(players)):
#             self.playname[i]=players[i]
#             self.playscore[i]=0
#             self.card[i]=self.cards[i:53:i]

            

class playcard:        
    def __init__(self,players):
        self.cards=[i for i in range(1,53)]
        random.shuffle(self.cards)
        
        self.playname=''
        self.playscore=0
        self.card=[]        

        for i in range(1,len(players)):
            self.playname[i]=players[i]
            self.playscore[i]=0
            self.card[i]=self.cards[i:53:i]
list1=['a','b']
test=playcard(list1)
            
            



#     def play(self):
#         # self.play1card=self.cards[1:53:2]
#         # self.play2card=self.cards[2:53:2]        
#         for i,j in zip(self.play1card,self.play2card):                         
#             if i>j:
#                 self.play1score+=(i+j)
#             else:
#                 self.play2score+=(i+j)
#     def getresult(self):

#           if self.play1score==self.play2score:
#             self.play()
#           elif self.play1score>self.play2score:
#               return self.player1
#           else:
#               return self.player2
# if __name__=="__main__":
#     players=['Przmek', 'Adelajda',"cairong"]
#     test=playcard(players)
#     test.play()
#     print(test.play1card,test.play1score)
#     print(test.play2card,test.play2score)
#     print(test.getresult())
                
                
                
        