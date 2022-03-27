import random


def gamewin(pc, you):
    if pc == you:  # two values are equal probability
        return None
    elif pc == 's':
        if pc == 'w':
            return False
        elif pc == 'g':
            return True
    elif pc == 'w':  # all possibilities when comp choose w
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif pc == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("pc turn : Snake (s) water (w) gun (g)")
randno = random.randint(1, 3)


if randno == 1:
    pc = 's'
elif randno == 2:
    pc = 'w'
elif randno == 3:
    pc = 'g'

you = input(("your turn : snake(s) water(w) gun(g)"))

a = gamewin(pc, you)
print(f"computer choose {pc}")
print(f"you choose {you}")

if a == None:
    print("the game is tie !")

elif a:
    print("you win !")
else:
    print("you loose !!")
