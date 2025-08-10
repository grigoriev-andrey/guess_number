from random import randint

number_1 = randint(1, 100)


def main():
    while True:
        guess = int(input("Your number: "))
        if number_1 > guess:
            print("your number is smaller than guess")

        elif number_1 < guess:
            print("your number is bigger than guess")
        elif guess == number_1:
            break


main()


print("Good game, men")
print("Good game, women")
