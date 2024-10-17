"""
Game Name: Tic-Tac-Toe
Description: Play against a bot in Tic-Tac-Toe
Author: Zachary Coe
Date: 2024-10-16
"""



import random



BOARD_SPOTS = 9
WINNING_COMBINATIONS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]



class Board:
    starting_appearance = f"""
                 1 | 2 | 3 
                ---+---+---
                 4 | 5 | 6 
                ---+---+---
                 7 | 8 | 9 """
    
    def __init__(self):
        self.spot_list = [" "] * BOARD_SPOTS    
        self.game_over = False

    def find_empty_spots(self):
        empty_spots = []
        for index in range(len(self.spot_list)):
            if self.spot_list[index] == " ":
                empty_spots.append(index + 1)
        return empty_spots
        
    def update_board(self, spot, symbol):
        self.spot_list[spot - 1] = symbol
        # Empty appearance from above, but adjusts with x's or o's
        self.appearance = f"""                 {self.spot_list[0]} | {self.spot_list[1]} | {self.spot_list[2]} 
                ---+---+---
                 {self.spot_list[3]} | {self.spot_list[4]} | {self.spot_list[5]} 
                ---+---+---
                 {self.spot_list[6]} | {self.spot_list[7]} | {self.spot_list[8]} """
        
        print(f"\n{self.appearance}")


    
class Player:
    def __init__(self):
        self.symbol = ""

    def take_turn(self, board: Board):
        empty_spots = board.find_empty_spots()
        while True:
            try:
                spot = input(f"\nChoose a spot {empty_spots}: ")
                spot = int(spot)
                if spot in empty_spots:
                    return spot
                else:
                    raise ValueError()
            except ValueError:
                print(f"Invalid input, please choose from {empty_spots}.")    
        

class Computer(Player):
    def __init__(self, hard):
        super().__init__()
        self.hard = hard        

    def take_turn(self, board: Board):
        empty_spots = board.find_empty_spots()
        print("\nComputer's turn...")
        pause()
        if self.hard:
            return
        else:
            return random.choice(empty_spots)


              
class Game:
    instructions = """\nTicTacToe! You'll be randomly assigned X's or O's.
You'll be asked for a location you'd like to play.
To do so, type the number that corresponds to the
     spot you'd like to play on. Have fun!"""
    
    def __init__(self):
        print(Game.instructions)
        print(Board.starting_appearance)
        self.player = Player()
        self.play_again = True
        self.player_goes_first = True
        self.round_count = 0
        self.ties = 0
        self.wins = 0
        self.losses = 0

    def get_difficulty(self):
        while True:
            try:
                options = ["easy", "e", "hard", "h"]
                difficulty = input("\nSelect the difficulty (Easy/Hard): ").lower()
                if difficulty in options[:2]:
                    return False
                elif difficulty in options[2:]:
                    return True
                else:
                    raise ValueError()
            except ValueError:
                print("Invalid input. Please type 'easy' or 'hard'.")

    def choose_x_or_o(self):
        options = ["X", "O"]
        random.shuffle(options)
        self.player.symbol = options[0]
        self.computer.symbol = options[1]

        # If player has X, they go first
        self.player_goes_first = self.player.symbol == "X"
        
        print(f"You will be playing as {self.player.symbol}'s")
        return

    def set_play_again(self):
        play_list = ["n", "y"]
        while True:     
            try:   
                play = input("Play again? (y/n) ").lower()
                if play in play_list:
                    if play == "y":
                        self.play_again = True
                        return
                    else:
                        self.play_again = False
                        return
                else:
                    raise ValueError()
            except ValueError:
                print("Please type either y or n.")

    def new_game(self):
        self.round_count = 0
        self.computer = Computer(self.get_difficulty())
        self.choose_x_or_o()
        self.board = Board()

    def check_for_winner(self, symbol):
        for list in WINNING_COMBINATIONS:
            checker = 0
            for index in list:
                if self.board.spot_list[index] == symbol:
                    checker += 1
            if checker == 3:
                return True
        return False

    def player_goes_first_rounds(self):
        # Player turn
        self.board.update_board(self.player.take_turn(self.board), self.player.symbol)
        if self.round_count >= 3:
            if self.check_for_winner(self.player.symbol):
                self.board.game_over = True
                self.wins += 1
                return
        # Computer turn
        self.board.update_board(self.computer.take_turn(self.board), self.computer.symbol)
        if self.round_count >= 3:
            if self.check_for_winner(self.computer.symbol):
                self.board.game_over = True
                self.wins += 1
                return
        self.round_count += 1

    def computer_goes_first_rounds(self):
        # Computer turn
        self.board.update_board(self.computer.take_turn(self.board), self.computer.symbol)
        if self.round_count >= 3:
            if self.check_for_winner(self.computer.symbol):
                self.board.game_over = True
                self.wins += 1
                return
        # Player turn
        self.board.update_board(self.player.take_turn(self.board), self.player.symbol)
        if self.round_count >= 3:
            if self.check_for_winner(self.player.symbol):
                self.board.game_over = True
                self.wins += 1
                return
        self.round_count += 1



def main():
    tictactoe = Game()
    while tictactoe.play_again:
        tictactoe.new_game()
        player_symbol = tictactoe.player.symbol
        while not tictactoe.board.game_over:
            # Player goes first if X
            if player_symbol == "X":
                tictactoe.player_goes_first_rounds()
            else:
                tictactoe.computer_goes_first_rounds()
        print(f"Wins: {tictactoe.wins}")
        print(f"Losses: {tictactoe.losses}")
        print(f"Ties: {tictactoe.ties}")



def pause():
    while True:
        input("Press ENTER to continue")
        break



if __name__ == "__main__":
    main()