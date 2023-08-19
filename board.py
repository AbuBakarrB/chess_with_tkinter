# importing dependencies
import tkinter as tk

# creating root window
root = tk.Tk()
root.title("Chess")

# board class
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
                self.color = "#807c7c"
            else:
                self.color = "white"

            for col in range(8):
                if self.color == "white":
                    self.color = "#807c7c"
                else:
                    self.color = "white"
              
                self.gameboard[row][col] = tk.Button(root,
                                                        width = 9,
                                                        height = 4,
                                                     background = self.color,
                                                     borderwidth = 0,
                                                     compound = "left"
                                                     )

                self.gameboard[row][col].grid(row = row, column = col)
                
    def pieces(self):
        
        global wpawn, wrook, wknight, wbishop, wking, wqueen
        
        wpawn = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/pawn-w.png").subsample(6, 6)
        for i in self.gameboard[6]:
            i.configure(height = 0, width = 0, image = wpawn)
        
        # adding rooks
        wrook = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/rook-w.png").subsample(6, 6)
        self.gameboard[7][0].configure(height = 0, width = 0, image = wrook)
        self.gameboard[7][7].configure(height = 0, width = 0, image = wrook)
        
        # adding knights
        wknight = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/knight-w.png").subsample(6, 6)
        self.gameboard[7][6].configure(height = 0, width = 0, image = wknight)
        self.gameboard[7][1].configure(height = 0, width = 0, image = wknight)
        
        # adding bishops
        wbishop = tk.PhotoImage(master = root, file = r"/homeuser/chess/pieces/bishop-w.png").subsample(6, 6)
        self.gameboard[7][2].configure(height = 0, width = 0, image = wbishop)
        self.gameboard[7][5].configure(height = 0, width = 0, image = wbishop)
        
        # adding king and queen
        wking = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/king-w.png").subsample(6, 6)
        wqueen = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/queen-w.png").subsample(6, 6)
        self.gameboard[7][3].configure(height = 0, width = 0, image = wking)
        self.gameboard[7][4].configure(height = 0, width = 0, image = wqueen)
                
board = Board()
board.set_board()
board.pieces()
tk.mainloop()
    
