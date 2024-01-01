import random
choice_list=["Rock","Paper","Scissors"]
name=input ("Enter your name:")
choice=input("Enter Rock/Paper/Scissors:")
while choice in choice_list:
 choice=input("Enter Rock/Paper/Scissors:")
 System_choice=random.choice(["Rock","Paper","Scissors"])
 if System_choice==choice:
   continue
 if System_choice=="Rock" and choice=="Paper":
   print(f"Congrats!!You won!!! {name}")
   break
 if System_choice=="Scissors" and choice=="Paper":
   continue
 if System_choice=="Paper":
   if choice=="Scissors":
     print("Congrats!!You won!! {}".format(name))
     break
   if choice=="Rock":
     continue
 if System_choice=="Scissors":
   if choice=="Paper":
     continue
   if choice=="Rock":
     print(f"Congrats!! You won{name}!!")
     break
    
