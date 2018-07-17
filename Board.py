import Pieces


class Board:
    def __init__(self, grid, screen):
        # White
        grid[0][0] = Pieces.Rook("White", 0, 0, screen)
        grid[0][7] = Pieces.Rook("White", 0, 7, screen)

        grid[0][1] = Pieces.Knight("White", 0, 1, screen)
        grid[0][6] = Pieces.Knight("White", 0, 6, screen)

        grid[0][2] = Pieces.Bishop("White", 0, 2, screen)
        grid[0][5] = Pieces.Bishop("White", 0, 5, screen)

        grid[0][4] = Pieces.Queen("White", 0, 4, screen)
        grid[0][3] = Pieces.King("White", 0, 3, screen)
        for x in range(8):
            grid[1][x] = Pieces.Pawn("White", 1, x, screen)

        # Black changes in some comments
        grid[7][0] = Pieces.Rook("Black", 7, 0, screen)
        grid[7][7] = Pieces.Rook("Black", 7, 7, screen)

        grid[7][1] = Pieces.Knight("Black", 7, 1, screen)
        grid[7][6] = Pieces.Knight("Black", 7, 6, screen)

        grid[7][2] = Pieces.Bishop("Black", 7, 2, screen)
        grid[7][5] = Pieces.Bishop("Black", 7, 5, screen)

        grid[7][4] = Pieces.Queen("Black", 7, 4, screen)
        grid[7][3] = Pieces.King("Black", 7, 3, screen)
        for y in range(8):
            grid[6][y] = Pieces.Pawn("Black", 6, y, screen)
        self.grid = grid
        return

    def get_grid(self):
        return self.grid

    def get_piece(self, x, y):
        return self.grid[x][y]

    def piece_at(self, x, y):
        return self.grid[x][y] != 0
