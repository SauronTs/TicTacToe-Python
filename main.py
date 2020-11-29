#!/usr/bin/env python3

from TicTacToe import TicTacToe
import random

def main():
    game = TicTacToe()
    currentInput = ' '

    if random.randint(0, 1) == 0:
        game.nextAIMove()

    game.printField()

    while(currentInput != 'q' and game.gameIsRunning):
        currentInput = input()
        game.performMoves(currentInput)
        game.printField()

    print()

if __name__ == "__main__":
    main()