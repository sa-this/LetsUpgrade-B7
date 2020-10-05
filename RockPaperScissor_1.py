#!/usr/bin/env python
# coding: utf-8

# In[42]:


def toGetInputFromUser():
    player="blank"
    
    while not(player.lower()=="r" or player.lower()=="p" or player.lower()=="s"):
        player=input("enter your input out of R | P | S: ")
    return player


# In[51]:


import random
def toGetInputFromBot():
    lst=["r","p","s"]
    bot=random.choice(lst)
    return bot


# In[57]:


def toCheckWinner(player,bot):
    if(player=="r" and (bot=="p" or bot=="s")):
        if(bot=="p"):
            return "player"
        else:
            return "bot"
    elif(player=="p" and (bot=="r" or bot=="s")):
        if(bot=="p"):
            return "player"
        else:
            return "bot"
    elif(player=="s" and (bot=="p" or bot=="r")):
        if(bot=="p"):
            return "player"
        else:
            return "bot"
    elif(player==bot):
        return "draw"


# In[90]:


def rps():
    playerScore=0
    botScore=0
    quite="n"
    while(quite !="y"):
        player=toGetInputFromUser()

        print("\nThe player choose:",player)
        bot=toGetInputFromBot()
        print("\nThe bot choose : ",bot)
        winner=toCheckWinner(player,bot)
        print("\nthe winner is: ",winner,"\n\n")

        if(winner=="player"):
            playerScore+=2
        elif(winner=="bot"):
            botScore+=2
        else:
            playerScore+=1
            botScore+=1
            
        print("Score Board".rjust(20," "))
        print("_____________________________________________")
        print("\nPlayer's score--------->  \t",playerScore)
        print("\nBot's Score------------>\t",botScore)
        print("_____________________________________________")
        quite=input("\nIf you want quite press y otherwise press n\n")
        print("XXX".center(50,"_"))
rps()


# In[ ]:




