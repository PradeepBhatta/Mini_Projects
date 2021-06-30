def getdate():
    import datetime
    return datetime.datetime.now()

def diet(clients):
    if clients in client_list:
        print("What did",clients,"eat ? ", end="")
        food = input("")
        print("Sucessfully written !!!")
        f = open(filename,"a")
        f.write("At "+str(getdate())+" "+clients + " ate "+food)
        f.close()
    else:
        print("Please input name correctly")   

def exercise(clients):
    if clients in client_list:
        print("What did",clients,"did? ", end="")
        exer = input("")
        print("Sucessfully written !!!")
        f = open(filename,"a")
        f.write("At "+str(getdate())+" "+clients + " did "+exer)
        f.close()
    else :
         print("Please input name correctly")

def retr():
    if clients in client_list:
        op = open(filename)
        print(op.readlines())
        op.close()

client_list = ["Pro" , "Noob" , "Bot"]
print("***** Health Management System ****")
print("Hello Wlcome to our health management system")
print('''Select your client
    Pro
    Noob
    Bot\n''')
clients = input("Enter your client's name = ")
log = input("Do you want to log or retrive\nPress 1 for log\nPress 2 for retrive\n")

if log == "1":
    print("Press 1 for Exercise\nPress 2 for Diet")
    ch = input("Enter your choice = ")

    if ch == "1":
        extension = ("_exe.txt")
        filename =(clients + extension)
        exercise(clients)
        
    elif ch == "2":
        extension = ("diet_.txt")
        filename =(clients + extension)
        diet(clients)
    else:
        print("Wrong Input!!!")

elif log == "2":

    print("Press 1 for Exercise\nPress 2 for Diet")
    ch = input("Enter your choice = ")

    if ch == "1":
        extension = ("_exe.txt")
        filename =(clients + extension)
        retr()

    elif ch == "2":
        extension = ("diet_.txt")
        filename =(clients + extension)
        retr()

    else:
        print("Wrong Input!!!")

else :
    print("Please input name correctly")
