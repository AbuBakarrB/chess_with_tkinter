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
        self.color = "#807c7c"
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
        
        global wpawn, bpawn, wrook, brook, wknight, bknight, wbishop, bbishop,wking, bking, wqueen, bqueen
        
        # adding pawns
        wpawn = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/pawn-w.png").subsample(6, 6)
        bpawn = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/pawn-b.png").subsample(6, 6)
        for i in self.gameboard[6]:
            i.configure(height = 0, width = 0, image = wpawn)
        for j in self.gameboard[1]:
            j.configure(height = 0, width = 0, image = bpawn)
        
        # adding rooks
        brook = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/rook-b.png").subsample(6, 6)
        wrook = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/rook-w.png").subsample(6, 6)
        self.gameboard[7][0].configure(height = 0, width = 0, image = wrook)
        self.gameboard[7][7].configure(height = 0, width = 0, image = wrook)
        self.gameboard[0][0].configure(height = 0, width = 0, image = brook)
        self.gameboard[0][7].configure(height = 0, width = 0, image = brook)
        
        # # adding knights
        bknight = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/knight-b.png").subsample(6, 6)
        wknight = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/knight-w.png").subsample(6, 6)
        self.gameboard[7][6].configure(height = 0, width = 0, image = wknight)
        self.gameboard[7][1].configure(height = 0, width = 0, image = wknight)
        self.gameboard[0][1].configure(height = 0, width = 0, image = bknight)
        self.gameboard[0][6].configure(height = 0, width = 0, image = bknight)
        
        # # adding bishops
        bbishop = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/bishop-b.png").subsample(6, 6)
        wbishop = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/bishop-w.png").subsample(6, 6)
        self.gameboard[7][2].configure(height = 0, width = 0, image = wbishop)
        self.gameboard[7][5].configure(height = 0, width = 0, image = wbishop)
        self.gameboard[0][2].configure(height = 0, width = 0, image = bbishop)
        self.gameboard[0][5].configure(height = 0, width = 0, image = bbishop)
        
        # # adding king and queen
        bking = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/king-b.png").subsample(6, 6)
        bqueen = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/queen-b.png").subsample(6, 6)
        wking = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/king-w.png").subsample(6, 6)
        wqueen = tk.PhotoImage(master = root, file = r"/home/user/chess/pieces/queen-w.png").subsample(6, 6)
        self.gameboard[7][3].configure(height = 0, width = 0, image = wking)
        self.gameboard[7][4].configure(height = 0, width = 0, image = wqueen)
        self.gameboard[0][3].configure(height = 0, width = 0, image = bking)
        self.gameboard[0][4].configure(height = 0, width = 0, image = bqueen)
                
board = Board()
board.set_board()
board.pieces()
tk.mainloop()
    
