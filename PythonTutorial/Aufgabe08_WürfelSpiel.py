import random

rounds = 0
userSum = 0
computerSum = 0

while rounds <= 6:
    rounds += 1
    print("Click Enter to dice")
    input()
    computer = random.randint(1, 6)
    user = random.randint(1, 6)
    print("Round Nr " + str(rounds))
    print("computer has diced the number " + str(computer))
    print("user has diced the number " + str(user))
    computerSum += computer
    userSum += user

if (computerSum > userSum):
    print("Computer has Won")
else:
    print("User has won the Round!!!!!!!!!!!!")