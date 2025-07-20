Age =int(input("What is your age?"))
Height =int(input("What is your height")) 
Permission =bool(input("do you have parent permision?(yes/no)"))

if Age<12:
    print("you are not allowed on this ride")
if Height<145:
    print("you are not allowed on this ride")
if Permission False:
    print("You are not allowed on this ride")
else:
    print("You are allowed.")