#Higher Lower game
logo="""
                                                              
        ,--,                                                  
      ,--.'|                     ,---,                        
   ,--,  | :  ,--,             ,--.' |                        
,---.'|  : ',--.'|             |  |  :                __  ,-. 
|   | : _' ||  |,     ,----._,.:  :  :              ,' ,'/ /| 
:   : |.'  |`--'_    /   /  ' /:  |  |,--.   ,---.  '  | |' | 
|   ' '  ; :,' ,'|  |   :     ||  :  '   |  /     \ |  |   ,' 
'   |  .'. |'  | |  |   | .\  .|  |   /' : /    /  |'  :  /   
|   | :  | '|  | :  .   ; ';  |'  :  | | |.    ' / ||  | '    
'   : |  : ;'  : |__'   .   . ||  |  ' | :'   ;   /|;  : |    
|   | '  ,/ |  | '.'|`---`-'| ||  :  :_:,''   |  / ||  , ;    
;   : ;--'  ;  :    ;.'__/\_: ||  | ,'    |   :    | ---'     
|   ,/      |  ,   / |   :    :`--''       \   \  /           
'---'        ---`-'   \   \  /              `----'            
   ,--,                `--`-'                                 
,---.'|                                                       
|   | :                                                       
:   : |                                                       
|   ' :      ,---.           .---.            __  ,-.         
;   ; '     '   ,'\         /. ./|          ,' ,'/ /|         
'   | |__  /   /   |     .-'-. ' |   ,---.  '  | |' |         
|   | :.'|.   ; ,. :    /___/ \: |  /     \ |  |   ,'         
'   :    ;'   | |: : .-'.. '   ' . /    /  |'  :  /           
|   |  ./ '   | .; :/___/ \:     '.    ' / ||  | '            
;   : ;   |   :    |.   \  ' .\   '   ;   /|;  : |            
|   ,/     \   \  /  \   \   ' \ |'   |  / ||  , ;            
'---'       `----'    \   \  |--" |   :    | ---'             
                       \   \ |     \   \  /                   
                        '---"       `----'                                                     """              


vssign="""
                             
                             
              .--.--.        
       ,---. /  /    '.      
      /__./||  :  /`. /      
 ,---.;  ; |;  |  |--`       
/___/ \  | ||  :  ;_         
\   ;  \ ' | \  \    `.      
 \   \  \: |  `----.   \     
  ;   \  ' .  __ \  \  |     
   \   \   ' /  /`--'  /     
    \   `  ;'--'.     /___   
     :   \ |  `--'---'/  .\  
      '---"           \  ; | 
                       `--"  
"""  

print(logo)
print("Welcome to higher or lower! I will give you two cebrities and you will guess who hads the most amount of instagram followers")
import random 
from replit import clear 
from Celbrities import celebfollows


def game():
  score=0
  continue_game=True
  a=random.choice(list(celebfollows))
  b=random.choice(list(celebfollows))
  while continue_game==True:
    
    if a==b:
      b=random.choice(list(celebfollows))
      
    print(f"Your current score is: {score}")
    print(f"Compare A: {a}")
    print(vssign)
    print(f"Against B: {b}")
    playerchoice=input("Who has more Instagram followers? Type 'A' or 'B': ")
    
    if playerchoice== "A" and celebfollows[a]>celebfollows[b]:
      score+=1
      a=b
      b=random.choice(list(celebfollows))
      if a==b:
        b=random.choice(list(celebfollows))
      clear()
      
    elif playerchoice=="A" and celebfollows[a]<celebfollows[b]:
      clear()
      print("Sorry, that was wrong")
      print(f"Your final score is: {score}")
      continue_game=False
        
    elif playerchoice=="B" and celebfollows[b]>celebfollows[a]:
      score+=1
      a=b
      b=random.choice(list(celebfollows))
      if a==b:
        b=random.choice(list(celebfollows))
      clear()
        
    elif playerchoice=="B" and celebfollows[b]<celebfollows[a]:
      clear()
      print("Sorry, that was wrong")
      print(f"Your final score is: {score}")
      continue_game=False
      
game()  
