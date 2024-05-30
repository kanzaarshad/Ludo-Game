# -*- coding: utf-8 -*-
"""Python ludo game

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UJ6yV1JxspST40V_ryEQokxn6xKSTXcp
"""

import random

class LudoGame:
    def __init__(self):
        self.board = {
            "red": [None] * 4,
            "blue": [None] * 4,
            "green": [None] * 4,
            "yellow": [None] * 4
        }
        self.home = {
            "red": [(0, 0), (0, 1), (1, 0), (1, 1)],
            "blue": [(0, 12), (0, 13), (1, 12), (1, 13)],
            "green": [(12, 0), (12, 1), (13, 0), (13, 1)],
            "yellow": [(12, 12), (12, 13), (13, 12), (13, 13)]
        }
        self.safe = [(1, 6), (6, 1), (8, 1), (13, 6), (1, 8), (6, 13), (8, 13), (13, 8)]
        self.current_turn = "red"
        self.dice = None

    def roll_dice(self):
        self.dice = random.randint(1, 6)

    def move_piece(self, color, piece_index):
        if self.dice == 6 and self.board[color][piece_index] is None:
            self.board[color][piece_index] = 0
        elif self.board[color][piece_index] is not None:
            current_position = self.board[color][piece_index]
            new_position = current_position + self.dice
            if new_position > 51:
                return False  # Piece cannot move beyond 51
            if new_position in self.safe:
                self.board[color][piece_index] = new_position
            elif new_position % 13 == 0 or new_position % 13 == 8 or new_position % 13 == 6:
                self.board[color][piece_index] = new_position
            else:
                return False  # Piece cannot move to unsafe position
        return True

    def switch_turn(self):
        colors = list(self.board.keys())
        current_index = colors.index(self.current_turn)
        self.current_turn = colors[(current_index + 1) % len(colors)]

    def play(self):
        while True:
            print(f"It's {self.current_turn}'s turn.")
            input("Press Enter to roll the dice...")
            self.roll_dice()
            print(f"You rolled {self.dice}.")

            pieces = self.board[self.current_turn]
            print("Your pieces:", pieces)
            piece_index = int(input("Choose piece to move (0-3): "))

            if not self.move_piece(self.current_turn, piece_index):
                print("Invalid move! Try again.")
                continue

            print("Piece moved successfully.")

            self.switch_turn()


game = LudoGame()
game.play()