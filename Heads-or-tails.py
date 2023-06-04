import random

print("Heads Or Tails")
print("Created By Verticous")

def flip():
    result = random.randint(0, 1)
    return result

while True:
    flip_result = flip()
    if flip_result == 0:
        print("Heads")
    else:
        print("Tails")

    Inputchoice = input("Play again? (y/n): ")
    if Inputchoice.lower() != "y":
        break
