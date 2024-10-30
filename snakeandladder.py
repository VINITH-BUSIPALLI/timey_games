import pygame
import random
import sys

#VALUE DEFINING
WIDTH, HEIGHT=750,750
BOARD_SIZE=10
LINE_WIDTH=2
SPACE_SIZE = WIDTH // BOARD_SIZE
FONT_SIZE=32

#COLOUR DEFINING
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("||SNAKE AND LADDER||")
