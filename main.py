import argparse
import random


def intify(a):
    if a.isdigit():

        return int(a)
    else:
        raise ValueError(f"Error! {a} is not valid")


parser = argparse.ArgumentParser(description='dice roller that can simulate the rolls of various configurations of dice')

parser.add_argument('dice', type=str, help='selection of dice. Syntax xdy. x = number of dice / y number of side')
parser.add_argument('-l', '--log', type=str, default='rolls_log.txt', help='file where to a log of the rolls')
parser.add_argument('-r', '--repeat', type=int, default=1, help='number of times to roll')

args = parser.parse_args()

if 'd' in args.dice.lower().strip():
    dices, sides = [intify(number) for number in args.dice.lower().strip().split('d')]
else:
    print(f"Syntax Error: {args.dice} doesn't respect the selection's syntax")

for _ in range(args.repeat):
    rolls = [random.randint(1, sides) for _ in range(dices)]
    total = sum(rolls)
    average = total/len(rolls)

    text = f"Rolls: {', '.join(map(str,rolls))}\nTotal: {total}\nAverage: {average:.2f}\n"

    print(text)

    with open(args.log, mode= 'a') as file:
        file.write(text)
        file.write("-" * 30 + "\n")
