import pygame
import Board

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 100
HEIGHT = 100

MARGIN = 1

grid = []

for row in range(8):
    grid.append([])
    for column in range(8):
        grid[row].append(0)


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


WINDOW_SIZE = [807, 807]
screen = pygame.display.set_mode(WINDOW_SIZE)
board = Board.Board(grid, screen)
pygame.init()
pygame.display.set_caption("Chess")

done = False

clock = pygame.time.Clock()

CURRENTLY_CLICKED = ()

color_grid = [[WHITE] * 8 for _ in range(8)]

largeText = pygame.font.Font('freesansbold.ttf', 115)
TextSurf, TextRect = text_objects("Hello World!", largeText)
TextRect.center = ((WINDOW_SIZE[0] / 2), (WINDOW_SIZE[1] / 2))
# gameDisplay.blit(TextSurf, TextRect)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif pygame.mouse.get_pressed()[2] == 1:  # RIGHT CLICK
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if board.piece_at(row, column):
                HOVER_OVER_MOVES = board.get_piece(row, column).get_moves()
                if (row, column) == CURRENTLY_CLICKED:
                    for item in HOVER_OVER_MOVES:
                        color_grid[item[0]][item[1]] = WHITE
                    CURRENTLY_CLICKED = ()
                else:
                    color_grid = [[WHITE] * 8 for _ in range(8)]
                    CURRENTLY_CLICKED = (row, column)
                    for item in HOVER_OVER_MOVES:
                        if not board.piece_at(item[0], item[1]):
                            color_grid[item[0]][item[1]] = RED
            pygame.display.flip()
    screen.fill(BLACK)
    for row in range(8):
        for column in range(8):
            pygame.draw.rect(screen,
                             color_grid[row][column],
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            screen.blit(TextSurf, TextRect)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
