import random
x = 10
user = 0
computer = 0
tie = 0
print("Hello welcome to Snake Water and Gun game")

while x > 0 :
    lst =["Snake","Water","Gun"]
    choice = random.choice(lst)
    print("Press s for Snake\nPress w for Water\nPress g for gun\n")
    inp = input("Enter your choice :- ")

    if inp == "s" and choice == lst[1]:
        print("You got a point")
        user = user + 1

    elif inp == "w" and choice == lst[2]:
        print("You got a point")
        user = user + 1

    elif inp == "g" and choice == lst[0]:
        print("You got a point")
        user = user + 1

    elif inp == "s" and choice == lst[0]:
        print("Tie")
        tie = tie + 1

    elif inp == "w" and choice == lst[1]:
        print("Tie")
        tie = tie + 1

    elif inp == "g" and choice == lst[2]:
        print("Tie")
        tie = tie + 1

    else:
        print("Computer got a point")
        computer = computer + 1 
    x = x - 1

print("Your Points =",user)
print("Computer Points =",computer)
print("Ties =",tie)

if user > computer:
    print("You Win!!!")
elif user <  computer:
    print("You Lose!!!")
else:
    print("tie")
