# Project2 - Bulls and Cows

# Define basic variables
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
Hello_user = '''
Hi there user!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number'''
import random

# Define main function
def main():
    print(Hello_user)
    rand_number = list(map(int, random.sample(nums, 4)))
    print(rand_number)
    user_guess = user_input(rand_number)
    bulls, cows = bulls_and_cows(user_guess, rand_number)
    print(f" {bulls} Bulls, {cows} Cows")



def user_input(rand_number):
    guess_list = []
    while True:
        guess_num = input(":")
        try:
            if len(str(guess_num)) == 4:
                for i in str(guess_num):
                    guess_list.append(int(i))
                return guess_list
            elif guess_num == "":
                print("prazdna hodnota")
            else:
                print("Cislo musi byt 4 mistne")
        except ValueError:
            print("Prosim zadejte pouze cislice")


def bulls_and_cows(guess_num, rand_num):
    bulls = 0
    cows = 0
    for i, x in enumerate((rand_num)):
        for j, y in enumerate((guess_num)):
            if i == j and x == y:
                bulls = bulls + 1
            elif x == y:
                cows = cows + 1
    return bulls, cows


main()
