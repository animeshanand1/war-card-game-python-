#!/usr/bin/env python
# coding: utf-8

# In[136]:


#for comparing rank of the cards dictionary is used
import random
suits=("Hearts","Diamonds","Clubs","Spades")
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7, "Eight":8, "Nine":9 , "Ten":10 ,"Jack":11, 
        "Queen":12 , "King":13 ,"Ace":14}
       


# In[137]:


class card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit


# In[138]:


class Deck:
    
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                created_card=card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()


# In[139]:


new_deck= Deck()


# In[140]:


new_deck.shuffle()


# In[141]:


mycard=new_deck.deal_one()


# In[142]:


print(mycard)


# In[143]:


class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        return self.all_cards.pop()
    def add_cards(self,new_cards):
        #will be checking for whether the new card being added is a list of cards or a single card
        if type(new_cards)==type([]):
            return self.all_cards.extend(new_cards)
        else:
            return self.all_cards.append(new_cards)
    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'


# In[144]:


new_player= Player ("Animesh")


# In[145]:


print(new_player)


# In[146]:


new_player.add_cards(mycard)


# In[147]:


print(new_player)


# In[148]:


print(new_player.all_cards[0])


# In[149]:


new_player.add_cards([mycard,mycard,mycard])


# In[150]:


print(new_player)


# In[151]:


new_player.remove_one()


# In[152]:


print(new_player)


# In[199]:


#Setting Up The Game:
player_one= Player ("One")
player_two = Player ("Two")

new_deck=Deck()
new_deck.shuffle()
#Distribution of cards among the 2 players:

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
    


# In[200]:


game_on=True


# In[201]:


#Game logic:
round_num=0
while game_on:
    round_num+=1
    print(f'round {round_num}')
    if len(player_one.all_cards)==0:
        print("player one has been defeated,player two won!!")
        game_on=False
        break
    if len(player_two.all_cards)==0:
        print("player two has been defeated,player one won!!")
        game_on=False
        break

#New Round Starts:
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())

    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())

    at_war=True
    while at_war:
        
        if player_one_cards[-1].value>player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            
            player_one.add_cards(player_two_cards)
            
            at_war=False
        
        elif player_one_cards[-1].value<player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            
            player_two.add_cards(player_two_cards)
            
            at_war=False
            
        else:
            print("WAR!")
            
            
            if len(player_one.all_cards)<7:
                print("Player one has insufficient cards to declare war")
                print("Player Two wins!!")
                game_on=False
                break
                
            
            elif len(player_two.all_cards)<7:
                print("Player two has insufficient cards to declare war")
                print("Player One wins!!")
                game_on=False
                break
                
                
            else:
                for num in range(7):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
           
            
        
        
    
    


# In[ ]:





# In[ ]:




