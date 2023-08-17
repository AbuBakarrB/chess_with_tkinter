import tkinter as tk

root = tk.Tk()
root.title("Chess")

class Board(tk.Button):
    
    gameboard = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    
    def __init__(self):
        pass
    
    
    def set_board(self):
        self.color = "#808080"
        for row in range(8):
            
            if self.color == "white":
                self.color = "#808080"
            else:
                self.color = "white"

            for col in range(8):
                if self.color == "white":
                    self.color = "#808080"
                else:
                    self.color = "white"
              
                self.gameboard[row][col] = tk.Button(
                                                     width = 8,
                                                     height = 3,
                                                     background = self.color
                                                     )

                self.gameboard[row][col].grid(row = row, column = col)
board = Board()
board.set_board()
tk.mainloop()
    
