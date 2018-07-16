import pygame


class Piece:
    def __init__(self, color, piece_type, x, y, screen):
        self.color = color
        self.piece_type = piece_type
        self.pos_x = x
        self.pos_y = y
        self.screen = screen

    def drawPiece():
        carImg = pygame.image.load('whitepawn.png')
        screen.blit(carImg, (self.pos_x, self.pos_y))

    def __str__(self):
        return "{} {}".format(self.color, self.piece_type)


class King(Piece):  # Inheritance
    def __init__(self, color, x, y, screen):
        self.moves_made = 0
        super().__init__(color, King, x, y, screen)

    def get_moves(self):
        return []


class Queen(Piece):  # Inheritance
    def __init__(self, color, x, y, screen):
        super().__init__(color, Queen, x, y, screen)

    def get_moves(self):
        return []


class Pawn(Piece):  # Inheritance
    def __init__(self, color, x, y, screen):
        self.moves_made = 0
        super().__init__(color, Pawn, x, y, screen)
        # carImg = pygame.image.load('whitepawn.png')
        # self.screen.blit(carImg, (self.pos_x, self.pos_y))

    def get_moves(self):
        if self.color == "White":
            if self.moves_made == 0:
                return [(self.pos_x + 1, self.pos_y), (self.pos_x + 2, self.pos_y)]
            return [(self.pos_x + 1, self.pos_y)]
        if self.moves_made == 0:
            return [(self.pos_x - 1, self.pos_y), (self.pos_x - 2, self.pos_y)]
        return [(self.pos_x - 1, self.pos_y)]


class Rook(Piece):  # Inheritance
    def __init__(self, color, x, y, screen):
        self.moves_made = 0
        super().__init__(color, Rook, x, y, screen)

    def get_moves(self):
        return []


class Knight(Piece):  # Inheritance
    def __init__(self, color, x, y, screen):
        super().__init__(color, Knight, x, y, screen)

    def get_moves(self):
        return []


class Bishop(Piece):  # Inheritance
    def __init__(self, color, x, y, screen):
        super().__init__(color, Bishop, x, y, screen)

    def get_moves(self):
        return []
