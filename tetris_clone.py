#! python3
# tetris_clone.py - Tetris game clone
# This program was created according to a YouTube video tutorial on the channel freeCodeCamp.org
# The tutorial can be found at: https://www.youtube.com/watch?v=zfvxp7PgQ6c
#
# Usage: python.exe tetris_clone.py
#        then follow instructions on display
# 19-02-2020 elective skill
#

import pygame
import random


"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()  # initilizing pygame fonts

# GLOBALS VARS
# window width and height
s_width = 800
s_height = 700
# play field width and height
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
# length of one block in both dimensions (30x30px)
block_size = 30

top_left_x = (s_width - play_width) // 2  # calculating top right x-position of play field
top_left_y = s_height - play_height  # calculating top right y-position of play field


# SHAPE FORMATS
# different rotational appearances are given for each piece in a list

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

# list including all 7 different pieces
shapes = [S, Z, I, O, J, L, T]
# list that includes different colors for each piece
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0),
                (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape (7 in total)


# class for pieces
class Piece(object):
    # function for assigning values to a created object of this class
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape  # S, Z, I, O, J, L, or T
        # gets the position in the list 'shapes' for current shape and then picks color accordingly
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # default rotation; obviously start in first rotation


# this function is for creating the games grid; default grid has no locked positions
def create_grid(locked_positions={}):
    # defines the size and default color (black) of the grid, here: 20rows x 10 columns
    grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]
    # The (0,0,0) are the default color in every field; here: black

    for i in range(len(grid)):  # looping over rows of grid
        for j in range(len(grid[i])):  # looping over columns of grid
            if (j, i) in locked_positions:  # check if current position in grid is in dictionary locked_positions
                c = locked_positions[(j, i)]  # save the locked_positions color into a variable
                grid[i][j] = c  # overwrite the black from above with the locked_positions color
    return grid  # return whole grid with current colors


# function for rotating current piece
def convert_shape_format(shape):
    positions = []  # create empty list for positions to return
    # get rotation number by using modulo operation on rotation position and save in variable
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


# check if piece is in a valid space
def valid_space(shape, grid):
    # create accepted positions by checking whether position is black or not by looping over grid
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0, 0, 0)] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


# check if game is lost
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False


# function for creating a new piece from class Piece
def get_shape():
    # arguments: x-position, y-position, and what shape (in this case picking a random one from list shapes)
    return Piece(5, 0, random.choice(shapes))


# function for drawing some text in the middle of the window
def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)  # specify font
    label = font.render(text, 1, color)  # render font

    # blit rendered font onto middle of surface
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2),
                         top_left_y + play_height / 2 - label.get_height() / 2))


# function for drawing the play fields grid in grey
def draw_grid(surface, grid):
    sx = top_left_x  # taking global variables defined at the top
    sy = top_left_y

    for i in range(len(grid)):  # loop over grids rows
        # draw horizontal lines from left side of play field to right side
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * block_size),
                         (sx + play_width, sy + i * block_size))
    for j in range(len(grid[i])):  # loop over grids columns
        # draw vertical lines from top of play field to bottom
        pygame.draw.line(surface, (128, 128, 128), (sx + j * block_size, sy),
                         (sx + j * block_size, sy + play_height))


# function for clearing complete rows and moving the rest down
def clear_rows(grid, locked):

    inc = 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except ValueError:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

    return inc  # return count of cleared rows


# function for drawing the next coming piece on right side of play field
# takes pieces shape and the surface to draw it onto as arguments
def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)  # choosing font and size
    # render color and content of headline next shape
    label = font.render('Next Shape', 1, (255, 255, 255))

    sx = top_left_x + play_width + 50  # calculating x-position on right of playfield
    sy = top_left_y + play_height / 2 - 100  # calculating y-position
    format = shape.shape[shape.rotation % len(shape.shape)]  # ?

    for i, line in enumerate(format):  # loop over format
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':  # see above in shapes where '0' comes from
                # draw rectangle in pieces color onto surface in specified position; filled out
                pygame.draw.rect(surface, shape.color, (sx + j * block_size,
                                                        sy + i * block_size, block_size, block_size), 0)

    surface.blit(label, (sx + 10, sy - 30))  # blit label onto surface


# function for updating high score in all time high score txt-file
def update_score(nscore):
    score = max_score()  # retrieve current saved high score

    # open file in write-mode
    with open('scores.txt', 'w') as f:
        if int(score) > nscore:  # if saved high score higher than current one write old one again into file
            f.write(str(score))
        else:  # if current high score higher than saved one write current one into file
            f.write(str(nscore))


# function for retrieving max score from txt-file
def max_score():
    # open file in read-mode
    with open('scores.txt', 'r') as f:
        lines = f.readlines()  # read whole content
        score = lines[0].strip()  # save high score in variable

    return score  # return all time high score


def draw_window(surface, grid, score=0, last_score=0):
    surface.fill((0, 0, 0))  # fill window black

    pygame.font.init()  # initialize pygame fonts
    # Tetris label
    font = pygame.font.SysFont('comicsans', 60)  # choose font and size
    # define text and color for label (2nd argument is boolean smooth edges)
    label = font.render('Tetris', 1, (255, 255, 255))

    # draw lable on top of window
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    # current score
    font = pygame.font.SysFont('comicsans', 30)  # choose font and size
    # define text and color for current score (2nd argument is boolean smooth edges)
    label = font.render('Score: ' + str(score), 1, (255, 255, 255))

    sx = top_left_x + play_width + 50  # calculate x-position of current score
    sy = top_left_y + play_height / 2 - 100  # calculate y-position of current score

    surface.blit(label, (sx + 20, sy + 160))  # draw current score on top of window

    # high score
    # define text and color for current score (2nd argument is boolean smooth edges)
    label = font.render('High Score: ' + last_score, 1, (255, 255, 255))

    sx = top_left_x - 200  # calculate x-position of high score
    sy = top_left_y + 200  # calculate y-position of high score

    surface.blit(label, (sx + 20, sy + 160))  # draw high score on top of window

    # draw blocks onto window in defined colors
    for i in range(len(grid)):  # loop over rows
        for j in range(len(grid[i])):  # loop over columns
            # draw rectangle; arguments: surface, color, position + size, outline thickness (0 is filled)
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * block_size,
                                                   top_left_y + i * block_size, block_size, block_size), 0)

    # draw outer grid of playfield onto surface in red
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 4)

    # call function to draw white grid onto blocks so they dont touch each other
    draw_grid(surface, grid)
    # pygame.display.update()


def main(win):
    last_score = max_score()  # retrieves all time max score
    locked_positions = {}  # create dictionary for position of already fallen pieces
    # grid = create_grid(locked_positions)

    change_piece = False  # boolean for changing piece
    run = True  # boolean variable for keeping the program running
    current_piece = get_shape()  # get random current tetris piece
    next_piece = get_shape()  # get random next tetris piece
    clock = pygame.time.Clock()  # create object of pygame clock
    fall_time = 0  #
    fall_speed = 0.27  # basis fall speed of pieces
    level_time = 0  # just initilize time in current level (unused)
    score = 0  # initial score, every game starts with 0

    while run:
        # creating the grid for the pieces (20x10); argument are the already fallen pieces (initially none; see above)
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()  # save running time of game
        level_time += clock.get_rawtime()  # save running time of game (unused)
        clock.tick()  # update clock

        if level_time / 1000 > 5:  # not implemented
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005

        if fall_time / 1000 > fall_speed:  # check if according to this rule the piece should move down
            fall_time = 0  # set back fall_time
            current_piece.y += 1  # move current piece one down
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:  # check if piece went through bottom
                current_piece.y -= 1  # move it one up again
                change_piece = True  # change to the next piece

        for event in pygame.event.get():
            # case for stopping the program and closing the window
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            # case for pressing a key
            if event.type == pygame.KEYDOWN:
                # case for pressing left arrow
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1  # move current piece one to left
                    if not(valid_space(current_piece, grid)):  # reverse moving if moving leads to unvalid position
                        current_piece.x += 1
                # case for pressing right arrow
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1  # move current piece one to right
                    if not(valid_space(current_piece, grid)):  # reverse moving if moving leads to unvalid position
                        current_piece.x -= 1
                # case for pressing down arrow
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1  # move current piece one to bottom
                    if not(valid_space(current_piece, grid)):  # reverse moving if moving leads to unvalid position
                        current_piece.y -= 1
                # case for pressing up arrow
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1  # rotate current piece by 90 degree clockwise
                    if not(valid_space(current_piece, grid)):  # reverse rotation if rotation leads to unvalid position
                        current_piece.rotation -= 1
                # case for pressing escape key
                if event.key == pygame.K_ESCAPE:
                    run = False  # ending game loop

        shape_pos = convert_shape_format(current_piece)  #

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:  # if true change to next piece
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece  # take the next_piece and use it as current piece
            next_piece = get_shape()  # initilize next piece
            change_piece = False  # change boolean back
            # assign points to score after clearing rows
            score += clear_rows(grid, locked_positions) * 10

        draw_window(win, grid, score, last_score)  # call function for drawing window
        draw_next_shape(next_piece, win)  # call function for drawing next piece on the right
        pygame.display.update()  # update display

        # calls function to check whether a game is lost; this will return boolean if lost
        if check_lost(locked_positions):
            draw_text_middle(win, "YOU LOST!", 80, (255, 255, 255))  # display YOU LOST onto window
            pygame.display.update()  # update display
            pygame.time.delay(1500)  # display message for some time
            run = False  # stop main loop from executing
            update_score(score)  # check if new score bigger than high score


#  function for displaying the game's menu; first function that gets called when running program
def main_menu(win):
    run = True  # obviously this boolean needs to be True to keep main loop running
    while run:
        win.fill((0, 0, 0))  # fill the window in black
        draw_text_middle(win, 'Press Any Key To Play', 60, (255, 255, 255))  # draw text onto window
        pygame.display.update()  # actually display the changes to the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close window if window close button is clicked
                run = False
            if event.type == pygame.KEYDOWN:  # start main/game function if ANY key is pressed
                main(win)  # call main game function and give current window as argument

    pygame.display.quit()  # quit window and end program


win = pygame.display.set_mode((s_width, s_height))  # initialize a window for display
pygame.display.set_caption('Tetris Clone')  # set caption of initialized window
main_menu(win)  # start game
