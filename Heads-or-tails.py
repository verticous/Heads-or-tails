import random

print("Heads Or Tails")
print("Created By Verticous")

while True:
    flip_result = random.randint(0, 1)
    if flip_result == 0:
        print("Heads")
    else:
        print("Tails")

    Inputchoice = input("Play again? (y/n): ")
    if Inputchoice.lower() not in {'yes','ye','y','yy'}:
        break
