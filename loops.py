import random
ans = input("enter a number :")

while  not ans.isdigit():
    ans = input("enter a number :")

ranNum = random.randint(0,100)

user_guess = int(input("write a number: "))

while user_guess != ranNum:
    if (user_guess > ranNum):
        print("too high")
    elif (user_guess < ranNum):
        print("Too low")
  
    user_guess = int(input("write a number: "))

print("you win")

