import random
#snake water and gun game

def gamewin(computer, you):
    #if two  values are equals decalare a tie
    if computer == you:
        return None
#check for all possibilities when computer choose s
    elif computer == 's':
        if you == 'w':
            return False
    elif you == 'g':
            return True

#check for all possibilities when computer choose w
    elif computer == 'w':
       if you == 'g':
           return False
    elif you == 's':
           return True

#check for all possibilities when computer choose g
    elif computer == 'g':
        if you == 's':
           return False
    elif you == 'w':
            return True

print("computer turn: snake(s) water(s) or gun(g)?")
randNo = random.randint(1,3)
if randNo  == 1:
    computer = 's'
elif randNo == 2:
    computer = 'w'
elif randNo == 3:
    computer ='g'

you = input("your turn: snnake(s) water(w) or gun(g)?")

a = gamewin(computer,you)

print(f"computer chose {computer}")
print(f"you chose {you}")

if a == None:
    print("the game is a tie!")
elif a:
    print("you win")
else:
    print("you lose :)")


