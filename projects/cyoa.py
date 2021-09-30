"""Guess Game!"""

__author__ = "730443412"

from random import randint

host: str = "Aaliyah"
player: str 
points: int 
SMILE: str = '\U0001F604'
SAD: str = '\U0001F614'
FROWN: str = '\U0001F615'


def main() -> None:
    """The program's entrypoint."""
    greet()
    # ask player for difficulty level using input function
    level: int = int(input("What level? 1 - Easy, 2 - Medium, 3 - Hard, 4 - Exit"))
    global points
    while level != 4:
        if level == 1:
            easy()
        elif level == 2:
            medium()
        elif level == 3:
            hard()
        else:
            print("Goodbye! You accumulated " + str(points) + "points")
        
        level = int(input("What level?" + SMILE))


def greet() -> None:
    """Greet function"""
    print(f"Welcome to Aaliyah's Very Simple Guessing Game. I will be your host, {host}! In this game, you will have to choose a number I am guessing. The hard the difficulty, the harder it will be to figure it out! Good luck!" + SMILE)
    global player 
    player = str(input("What is your name?"))
    print("Hello " + player + "!" + SMILE)


def easy() -> None:
    points: int = 0
    tries: int = 0
    max: int = 3
    answer = int(input("Pick a number between 1 and 2!: "))
    canswer = randint(1,2)
    while answer != canswer:
        while answer > canswer:
            print("Sorry, you guessed too high!" + SAD)
            tries += 1
            answer = int(input("Guess a number between 1 and 2: "))
        while answer < canswer:
            print("Sorry, you guessed too low!" + SAD)
            tries += 1
            answer = int(input("Guess a number between 1 and 2: "))
    print("Good job!")
    points + 1


def medium() -> None:
    points: int = 0
    tries: int = 0
    max: int = 3
    answer = int(input("Pick a number between 1 and 5!: "))
    canswer = randint(1,5)
    while answer != canswer:
        while answer > canswer:
            print("Sorry, you guessed too high!" + SAD)
            tries += 1
            answer = int(input("Guess a number between 1 and 5: "))
        while answer < canswer:
            print("Sorry, you guessed too low!" + SAD)
            tries += 1
            answer = int(input("Guess a number between 1 and 5: "))
    print("Good job!")
    points + 1


def hard() -> None:
    points: int = 0
    tries: int = 0
    max: int = 3
    answer = int(input("Pick a number between 1 and 10!: "))
    canswer = randint(1,10)
    while answer != canswer:
        while answer > canswer:
            print("Sorry, you guessed too high!" + SAD)
            tries += 1
            answer = int(input("Guess a number between 1 and 10: "))
        while answer < canswer:
            print("Sorry, you guessed too low!" + SAD)
            tries += 1
            answer = int(input("Guess a number between 1 and 10: "))
    print("Good job!")
    points + 1
            

if __name__ == "__main__":
    main()