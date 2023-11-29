# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:30:28 2023

@author: Yang Cairong
"""
import random
from itertools import zip_longest
class Player:
    def __init__(self,playerName):
        self.playName=playerName
        self.playCard=None
        self.playScore=0


class PlayCard:        
    def __init__(self,names):
        self.players=[Player(name) for name in names]
        self.cards=[i for i in range(1,53)]


    def play(self):
      
        random.shuffle(self.cards)
        
        cardNum= len(self.cards)
        playerNum=len(self.players)
        div,mod=divmod(cardNum, playerNum)      

        
        for i, player in enumerate(self.players):            
            player.playScore=0
            player.playCard=self.cards[i:div*playerNum:playerNum]
            
        if mod >0:
            choicePlayers=random.sample(range(0,playerNum),mod)
            for i,playerindex in  enumerate(choicePlayers):
                self.players[playerindex].playCard.append(self.cards[-i-1])     
        for cards in zip_longest(*[player.playCard for player in self.players],fillvalue=0):     

            cards=list(cards)
            max_index=cards.index(max(cards))
            self.players[max_index].playScore+=sum(cards)
            
            
            # print(cards,max_index)

    def get_result(self):
        
        scores=[player.playScore for player in self.players]
        
        return scores,[index for index,item in enumerate(scores) if item==max(scores)]
        # maxscore_index=scores.index(max(scores))
        
        # print(scores,maxscore_index)
if __name__=="__main__":
    player=['a', 'b','c']
    test=PlayCard(player)
    test.play()
    while True:
        test.play()
        scores,winnerIndex=test.get_result()
        print(scores,winnerIndex)
        if (len(winnerIndex)==1):
            print("Final Result:",winnerIndex,scores)
            print('The winner is:',test.players[winnerIndex[-1]].playName)
            print('Winner\'s score is:',test.players[winnerIndex[-1]].playScore )
            # index=[range(len(player))].remove(winnerIndex)
            remain_index=[i for i in range(len(player))if i not in winnerIndex]
            print(remain_index)                
            print('The other paticipators\' name are',[test.players[i].playName for i in remain_index])
            print('The other paticipators\' score are',[scores[i] for i in remain_index ],'respectively')
            print('The winner\'s information is :')
            # print("PlayerID :  %d  Player :  %s     Score : %d",% winnerIndex[0],test.players[winnerIndex[0]],scores[winnerIndex[0]])
            print('The other paticipators respectively are:',)
            # # initializing list of players.
            # players =[test.players[i].playName for i in index]
             
            # # initializing their scores
            # scores =[scores[i] for i in index ]
             
            # printing players and scores.
            for idx,pl, sc in zip([remain_index[i] for i in remain_index],[test.players[i].playName for i in remain_index], [scores[i] for i in remain_index ]):
                print("PlayerID :  %d  Player :  %s     Score : %d" % (idx,pl, sc))
    
            # for idx,n,s in zip(index[i],test.players[i].playName,scores[i] for i in index):
            #     print(idx,n,s)
            break


                
                
                
        