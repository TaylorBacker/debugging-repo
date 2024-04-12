from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value ## issue here counting correctly
        return total

    @classmethod
    def run(cls):
        rounds = 1
        winCount = 0
        loseCount = 0
        while True:
            runner = cls()

            print("Round {}\n".format(rounds))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                winCount += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                loseCount += 1

            print("Wins: {} Loses {}".format(winCount, loseCount))
            runner.round += 1
            rounds += 1

            if winCount == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

## fixed here
            if prompt == 'y' or prompt == 'Y':
                continue
            elif prompt =='n' or prompt == 'N':
                exit()
