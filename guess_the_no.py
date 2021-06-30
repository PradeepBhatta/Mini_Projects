import random

a = random.randint(0,100)
b = 0
c = 100 
n = 8
while n > 0:
    print("Number of remaining guesses :-",n)
    num = input("Enter any number = ")
    num = int(num)

    if num > a:
        print("The number is between ",b,"and",num,"\n")
        c = num
        
    elif num < a:
        print("The number is between ",num,"and",c,"\n")
        b = num

    elif num == a:
        print("Congrats!!! YOU WIN")
        break
    
    else:
        print("Wrong Entry!!! Try again")

    n= n-1

    if n== 0:
        print("YOU LOSE :(")
        print("The number is =",a)


    
    

    




