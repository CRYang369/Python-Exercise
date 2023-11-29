# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:30:28 2023

@author: Yang Cairong
"""
import random
class PlayCard:        
    def __init__(self,play1,play2):
        self.cards=[i for i in range(1,53)]
        self.player1=play1
        self.player2=play2
        self.play1card=None
        self.play2card=None

    def play(self):
        random.shuffle(self.cards)
        self.play1score=0
        self.play2score=0
        self.play1card=self.cards[1:53:2]
        self.play2card=self.cards[2:53:2]    
        # [(p1card,p2card) for p1card in self.play1card for p2card in self.play2card]                        

        for p1card,p2card in zip(self.play1card,self.play2card):                         
            if p1card>p2card:
                self.play1score+=(p1card+p2card)
            else:
                self.play2score+=(p1card+p2card)
    def get_result(self):

         if self.play1score==self.play2score:
            self.play()
            
         elif self.play1score>self.play2score:
             return self.player1
         else:
             return self.player2
if __name__=="__main__":
    test=PlayCard('a', 'b')
    test.play()
    print(test.play1card,test.play1score)
    print(test.play2card,test.play2score)
    print(test.getresult())
                
                
                
        