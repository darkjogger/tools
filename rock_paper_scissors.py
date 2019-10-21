#!/usr/bin/env python3

"""你将通过完成这段程序来实现“石头剪刀布”的游戏。这个游戏涉及 2 个玩家，
并且在每轮结束后统计 2 个玩家的得分情况。
"""

import random

moves = ['rock', 'paper', 'scissors']

class Player:
    """这个 Player 的类是所有 Player 类别的父类。你将编写多个与 Player 有关的类。
    """
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        while True:
            p1_move = input("pls input 'rock' or 'paper' or 'scissors' or 'quit'.").lower()
            if p1_move in ['rock', 'paper', 'scissors', 'quit']:
                return p1_move
            else:
                print("Error input, try again.")


class ReflectPlayer(Player):

    def __init__(self):
        self.my_move = random.choice(moves)

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = their_move


class CyclePlayer(Player):

    def __init__(self):
        self.my_move = random.choice(moves)

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        self.my_move = moves[(moves.index(my_move)+1)%3]

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if move1 != 'quit' and move2 != 'quit':
            print(f"\tPlayer 1: {move1}  Player 2: {move2}")
            if beats(move1,move2):
                self.record(1)
                print(f"\tPlayer 1 won.", end=" ")
            elif beats(move2, move1):
                self.record(2)
                print(f"\tPlayer 2 won.", end=" ")
            else:
                self.record(0)
                print(f"\tIt's a tie.", end=" ")
            print(f"Player1 : Player2 = {self.score1} : {self.score2}")
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)
            return True
        else:
            return False

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            if self.play_round():
                continue
            else:
                break

        # end of the game
        print("Final result:")
        if self.score1 > self.score2:
            print(f"\t*** Player1 : Player2 = {self.score1} : {self.score2}  Player1 triumph! ***")
        elif self.score1 < self.score2:
            print(f"\t*** Player1 : Player2 = {self.score1} : {self.score2}  Player2 triumph! ***")
        else :
            print(f"\t*** Player1 : Player2 = {self.score1} : {self.score2}. Ended in a draw ***")
        print("Game over!")

    def record(self, who_win):
        if who_win == 1:
            self.score1 += 1
        elif who_win == 2:
            self.score2 += 1
        else:
            pass


""" 总共4种玩家，人类：HumanPlayer(). 随机电脑：RandomPlayer().  记忆电脑：ReflectPlayer().  循环电脑：CyclePlayer().
    默认为一人类玩家、一随机电脑玩家，3局两胜制。
"""
if __name__ == '__main__':
    game = Game(RandomPlayer(), RandomPlayer())
    game.play_game()
