import random as rn
#Winning Rules of Stone-Paper-Scissor
print("Winning Rules of the Stone-Paper-Scissor game are stated as follows: \n"
                                +"Stone vs Paper : Paper WINS \n"
                                + "Stone vs Scissor : Stone WINS \n"
                                +"Paper vs Scissor : Scissor WINS \n") 
ans=-1
print("Choices\n1.Stone\n2.Paper\n3.Scissor\n0.Exit\n")
while ans!=0:
    ans=int(input("Enter your choice\n"))
    while ans<0 or ans>3:
        print("Oh no! Invalid choice.Try again :) \n1.Stone\n2.Paper\n3.Scissor\n0.Exit\n")
        ans=int(input())

    if ans==1:
        print("You choose Stone")
    elif ans==2:
        print("You choose Paper")
    elif ans==3:
        print("You choose Scissor")
    else:
        continue

    x=rn.randint(1,3)
    if x==1:
        print("Computer chooses Stone")
    elif x==2:
        print("Computer chooses Paper")
    else:
        print("Computer chooses Scissor")

    if((ans == 1 and x == 2) or (ans == 2 and x ==1 )):                 
        print("Paper wraps the stone")                                              
        temp = 2                                                
    elif((ans == 1 and x == 3) or (ans == 3 and x == 1)): 
        print("Stone breaks the scissor") 
        temp = 1
    elif(ans==x):
        print("Draw")
        continue
    else: 
        print("Scissor cuts the paper") 
        temp = 3
 
    if temp == ans: 
        print("Yay! You win.\n") 
    else: 
        print("Aww! You lose. Computer wins.\n")

print("Thank you for playing. Have a nice day :)")
