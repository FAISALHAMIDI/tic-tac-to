import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.player_turn = 'F'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_board()
        
    def create_board(self):
        """Create a 3x3 grid of buttons."""
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 40), width=5, height=2,
                                   command=lambda row=row, col=col: self.click_button(row, col))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
        
    def click_button(self, row, col):
        """Handle button click event."""
        button = self.buttons[row][col]
        if button['text'] == '' and self.check_winner() is False:
            button['text'] = self.player_turn
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player_turn} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.player_turn = 'T' if self.player_turn == 'F' else 'F'
                
    def check_winner(self):
        """Check if there is a winner."""
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != '':
                return True
        
        for col in range(3):
            if self.buttons[0][col]['text'] == self.buttons[1][col]['text'] == self.buttons[2][col]['text'] != '':
                return True
        
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            return True
        
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
            return True
        
        return False
    
    def check_draw(self):
        """Check if the game is a draw."""
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]['text'] == '':
                    return False
        return True
    
    def reset_board(self):
        """Reset the game board for a new game."""
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]['text'] = ''
        self.player_turn = 'F'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
