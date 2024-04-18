class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol



class ConnectFour:
    def __init__(self, row, col, win, players):
        self.row = row
        self.col = col
        self.win = win
        self.players = players
        self.board = [[' ' for _ in range(col)] for _ in range(row)]
        self.current_player = 0
        self.empty_cols = [0] * col



    def print_board(self):
        for row in self.board:
            print('|',' | '.join(row), '|')
            print('-' * (4 * self.col + 1))
        
        # Print column numbers
        print()
        for i in range(self.col):
            print(f"| {i} ", end="")
        print("|")
        print()
        print()




    def is_valid_move(self, col):
        return 0 <= col < self.col and self.empty_cols[col] < self.row

    def make_move(self, col):
        if self.is_valid_move(col):
            row = self.row - self.empty_cols[col] - 1
            self.board[row][col] = self.players[self.current_player].symbol
            self.empty_cols[col] += 1


    def check_winner(self, row, column):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            for i in range(1, self.win):
                r = row + dr * i
                c = column + dc * i
                if 0 <= r < self.row and 0 <= c < self.col and self.board[r][c] == self.players[self.current_player].symbol:
                    count += 1
                else:
                    break
            for i in range(1, self.win):
                r = row - dr * i
                c = column - dc * i
                if 0 <= r < self.row and 0 <= c < self.col and self.board[r][c] == self.players[self.current_player].symbol:
                    count += 1
                else:
                    break
            if count >= self.win:
                return True
        return False

    def switch_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)


    def play_game(self):
        while True:
            print()
            print()
            self.print_board()
            col = int(input(f"{self.players[self.current_player].name}, enter column: "))
            if self.is_valid_move(col):
                self.make_move(col)
                if self.check_winner(self.row - self.empty_cols[col], col):
                    print()
                    print()
                    print('*' *  (4 * self.col + 1))
                    print()
                    print()
                    self.print_board()
                    print(f"{self.players[self.current_player].name} wins!")
                    break
                self.switch_player()
            else:
                print()
                print("***   Invalid move. Try again   ***")
            print()
            print()
            print('*' *  (4 * self.col + 1))



game = ConnectFour(row = 6, col = 7, win = 4, players = [Player("John", "X"), Player("Anna", "O")])
game.play_game()


