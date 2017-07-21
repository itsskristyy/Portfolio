import random
from random import randint

answerNumb = str(randint(1,36))
color = ["red", "black"]
answerColor = random.choice(color)
answerColor = str(answerColor)
money = int(input("How much money do wanna start with?"))
bet = int(input("How much money would you like to bet?"))
guessColor = input("What color will it be? red or black:")
guessNumb = input("What number will it be? 1-36: ")


if guessNumb == answerNumb and guessColor == answerColor:
        print (" You got the right color and number!")
        money += (bet*5)

else:
    if guessNumb == answerNumb:
        print("You have the right number")
        money += bet

    else:
        print ("You guessed the wrong number. The answer was " + (str(answerNumb)) + "!")
        money -= bet

if guessColor == answerColor:
        print("You guessed the right color")
        money += bet

else:
        print ("You guessed the wrong color. The answer was " + (str(answerColor)) + "!")
        money -= bet

if (int(guessNumb) % 2 == 0) and (int(answerNumb) % 2 == 0):
        print ("Your answer and guess were both even.")
        money += bet

elif (int(guessNumb) % 2 == 1) and (int(answerNumb) % 2 == 1):
        print("Your answer and guess were both odd.")
        money += bet

elif (int(guessNumb)% 2 == 0):
        print("Your guess was even but the answer was odd")
        money -= bet

else:
        print("Your guess was odd but the answer was even.")
        money -= bet

print ("You walk away with " + (str(money)) + " dollars !")
