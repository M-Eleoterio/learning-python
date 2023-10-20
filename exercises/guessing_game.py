import os
import random

while True:

    print("HELLO!!! Wellcome to the Guessing Game!")
    print("Here are the rules:")
    print("1. A number between 1 and 20 will be generated. Your objective is to guess what number is that.")
    print("2. You have 5 lives. Everytime you give a wrong answer, you lose a life.")
    print("3. When you give a wrong answer, the game will tell you if your number is corret, lower or higher than the correct one.")
    print("This is all, have fun!!!")
    print("Made by Rvsso み")
    print("_______________________________________")
    # definindo as variaveis
    corr_number = random.randint(1, 20)
    lives = 5
    while lives >0:
        print("lives left:", lives)
        answer = int(input("Type your guess: "))
        if answer == corr_number:
            print("Congratulations! You guessed the number with", lives, "lives left!")
            break
        elif answer > corr_number:
            print("Wrong! The number is lower..")
            lives -= 1

        elif answer < corr_number:
            print("Wrong! The number is higher...")
            lives -= 1
    print("Sorry, the correct number was", corr_number) 
    print("Good luck next time!")
    break