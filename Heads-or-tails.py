import random

print("Heads Or Tails")
print("Created By Verticous")

def coin_flip():
    result = random.randint(0, 1)
    return result

while True:
    flip_result = coin_flip()
    if flip_result == 0:
        print("Heads")
    else:
        print("Tails")

    Inputchoice = input("Play again? (y/n): ")
    if Inputchoice.lower() != "y":
        break
