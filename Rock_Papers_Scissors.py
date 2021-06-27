import random

u_score = 0
c_score = 0
print("Number of rounds you wanna play?")
x = int(input())



for i in range (0,x):

    print("\nRock[r], Paper[p] or Scissors[s]?")
    u = input()

    choices = ["r", "p", "s"]
    c = random.choice(choices)

    if u == 'r'  and c == 'r':
        print(c)
        print("\nDRAW!")
        print(f"Computer score is {c_score} and User score is {u_score}")

    elif u == 'r' and c == 'p':
        print(c)
        print("\nComputer won!")
        c_score += 1
        print(f"Computer score is {c_score} and User score is {u_score}")

    elif u == 'r' and c == 's':
        print(c)
        print("\nYou won!")
        u_score += 1
        print(f"Computer score is {c_score} and User score is {u_score}")


    elif u == 'p' and c == 'p':
        print(c)
        print("\nDraw!!")
        print(f"Computer score is {c_score} and User score is {u_score}")

    elif u == 'p' and c == 's':
        print(c)
        print("\nComputer won!!")
        c_score += 1
        print(f"Computer score is {c_score} and User score is {u_score}")

    elif u == 'p'  and c == 'r' :
        print(c)
        print("\nYou won!!")
        u_score += 1
        print(f"Computer score is {c_score} and User score is {u_score}")




    elif u == 's'  and c == 's' :
        print(c)
        print("\nDraw!!")
        print(f"Computer score is {c_score} and User score is {u_score}")

    elif u == 's' and c == 'r' :
        print(c)
        print("\nComputer won!!")
        c_score += 1
        print(f"Computer score is {c_score} and User score is {u_score}")

    elif u == 's'  and c == 'p' :
        print(c)
        print("\nYou won!!")
        u_score += 1
        print(f"Computer score is {c_score} and User score is {u_score}")

    else:
        print("Use 'r' for ROCK, 'p' for 'PAPER' and 's' for SCISSORS")

def winner(u_score, c_score):
    if c_score > u_score:
        print("\nGAME OVER!")
        print("Computer won the game!")

    elif u_score == c_score:
        print("\nGAME OVER!")
        print("Its a Draw")

    else:
        print("\nGAME OVER!")
        print('Congrats you won the game!')

winner(u_score, c_score)