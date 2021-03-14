r = 8
chances = 5
guess=int(input("Guess the number"))

if(chances>0):
    if(guess == r):
        print("Congrats You Won!!!")
    else:
        chances=chances-1
        print("Try again.")
else:
    print("You lose!!!")