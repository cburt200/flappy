from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

RED = (0, 255, 0)
BLUE = (0, 0, 0)
YELLOW = (255,215,0)


x = 0
y = 0

matrix = [[BLUE for column in range(8)] for row in range(8)]

game_over = False

while game_over==False:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    sense.set_pixels(sum(matrix,[]))

def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened


def gen_pipes(matrix):
    for row in matrix:
        row[-1] = RED
    gap = randint(1, 6)
    matrix[gap][-1] = BLUE
    matrix[gap - 1][-1] = BLUE
    matrix[gap + 1][-1] = BLUE
    return matrix


def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i + 1]
        row[-1] = BLUE
    return matrix


def draw_astronaut(pitch, roll, x,y):
    new_x = x
    new_y = y
    
    sense.set_pixel(x, y, BLUE)
    if 1<pitch<179:
        new_x -=1
    sense.set_pixel(x, y, YELLOW)
    if matrix[y][x]==RED:
        game_over = True

    
def check_collision(matrix):
    if matrix[y][x] == RED:
        return True
    else:
        return False




while not game_over:
    matrix = gen_pipes(matrix)
    if check_collision(matrix):
        break
    for i in range(3):
        matrix = move_pipes(matrix)
        sense.set_pixels(flatten(matrix))
        sense.set_pixel(x, y, YELLOW)   
        if check_collision(matrix):
            game_over = True
        sleep(1)

sense.show_message('You lose!')