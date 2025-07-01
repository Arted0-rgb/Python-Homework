minimum_height=int(input("enter your height")) 
minimum_age=int(input("enter your age")) 
if height >= min_height and age >= min_age:
    print("You are able to to ride the roller coaster")
elif height < min_height:
    print("you are too short. You need to be taller.")
else:  
    print(" you are too young. You need to be older.")
    
