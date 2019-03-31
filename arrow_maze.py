#   Directional Maze:
#   e se se sw  s
#   s nw nw  n  w
#   ne  s  h  e sw
#   se  n  w ne sw
#   ne nw nw  n  n

# Traversable directions: 'n ne e se s sw w nw'
from enum import Enum


class Compass(Enum):
    NORTH = ["NORTH", "N", "n"]
    NORTH_EAST = ["NORTH_EAST", "NE", "ne"]
    NORTH_WEST = ["NORTH_WEST", "NW", "nw"]
    EAST = ["EAST", "E", "e"]
    SOUTH = ["SOUTH", "S", "s"]
    SOUTH_EAST = ["SOUTH_EAST", "SE", "se"]
    SOUTH_WEST = ["SOUTH_WEST", "SW", "sw"]
    WEST = ["WEST", "W", "w"]


def compass_display():
    backslash = "\\"
    straight = "|"
    side = "—"
    forward_slash = "/"
    temp = "\n\nCompass Direction Points:\n"
    temp += " " * 5 + Compass.NORTH_EAST.value[1] + (" " * 3)
    temp += " " * 2 + Compass.NORTH.value[1] + (" " * 3)
    temp += " " * 2 + Compass.NORTH_EAST.value[1] + (" " * 3) + "\n"

    temp += " " * 6 + Compass.NORTH_WEST.value[2] + (" " * 3)
    temp += " " + Compass.NORTH.value[2] + (" " * 3)
    temp += " " + Compass.NORTH_EAST.value[2] + (" " * 3) + "\n"

    for x in range(4):
        temp += "\t\t"
        temp += ((" " * x) + backslash)
        temp += ((" " * (3 - x)) + straight)
        temp += ((" " * (3 - x)) + forward_slash)
        temp += "\n"

    temp += " " * 1
    temp += Compass.WEST.value[1] + (" " * 3)
    temp += Compass.WEST.value[2] + (" " * 1)

    for x in range(6):
        temp += side

    temp += " " * 1
    temp += Compass.EAST.value[2] + (" " * 3)
    temp += Compass.EAST.value[1]
    temp += "\n"

    for x in range(4):
        temp += "\t\t"
        temp += ((" " * (3 - x)) + forward_slash)
        temp += ((" " * x) + straight)
        temp += ((" " * x) + backslash)
        temp += "\n"

    temp += " " * 5 + Compass.SOUTH_WEST.value[1] + (" " * 3)
    temp += " " * 2 + Compass.SOUTH.value[1] + (" " * 3)
    temp += " " * 2 + Compass.SOUTH_EAST.value[1] + (" " * 3) + "\n"

    temp += " " * 6 + Compass.SOUTH_WEST.value[2] + (" " * 3)
    temp += " " + Compass.SOUTH.value[2] + (" " * 3)
    temp += " " + Compass.SOUTH_EAST.value[2] + (" " * 3) + "\n"
    print(temp)


MOVES = 0
X = 0
Y = 0
CO_ORDINATES = (X, Y)
DIRECTION = ''
CURRENT_DIRECTION = ''
NEXT_DIRECTION = ''
# ROW: 3, INDEX: 2
H_CO_ORDINATES = (3, 2)
DIRECTIONS_YOU_CAN_MOVE = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']

maze = {
    0: ['e', 'se', 'se', 'sw', 's'],
    1: ['s', 'nw', 'nw', 'n', 'w'],
    2: ['ne', 's', 'h', 'e', 'sw'],
    3: ['se', 'n', 'w', 'ne', 'sw'],
    4: ['ne', 'nw', 'nw', 'n', 'n']
}


def display_row(list_row):
    print("\n")
    for x in range(len(list_row)):
        print(str(list_row[x]) + " ", )


def display_maze():
    print("\nMaze:")
    temp_maze = []

    for key in maze:
        for item in maze.get(key):
            temp_maze.append(" " + item)

    for x in range(len(temp_maze)):
        if ((x % 5) == 0) and (x is not 0):
            print("\n")
        print(temp_maze[x], end=" ")
    print("\n")


def set_starting_pos():
    enter_the_maze(X, Y)


def update_positioning():
    global DIRECTION
    global X, Y
    DIRECTION = maze.get(X)[Y]


def update_co_ordinates():
    global CO_ORDINATES
    global X, Y
    CO_ORDINATES = (X, Y)


def enter_the_maze(row, index):
    global X, Y
    if row > 0:
        X = row
    elif row <= 0:
        X = 0
    if index > 0:
        Y = index
    elif index <= 0:
        Y = 0
    update_co_ordinates()
    update_positioning()
    # testing_details()


def testing_details():
    print("\n\nTesting:")
    print("\t\tX: " + str(X))
    print("\t\tY: " + str(Y))
    print("\t\tDirection: " + str(DIRECTION))
    print("\t\tCo-Ordinates: " + str(CO_ORDINATES))


def home_details():
    print("\nHome (H): " + str(H_CO_ORDINATES))


def move_your_pos():
    global X, Y, MOVES
    # print("\nDirection: "+str(DIRECTION))
    # print("X: " + str(X))
    # print("Y: " + str(Y))

    if 'n' in DIRECTION:
        if X in [1, 2, 3, 4, 5]:
            X -= 1

    if 's' in DIRECTION:
        if X in [0, 1, 2, 3, 4]:
            X += 1

    if 'e' in DIRECTION:
        if Y in [0, 1, 2, 3]:
            Y += 1

    if 'w' in DIRECTION:
        if Y in [1, 2, 3, 4]:
            Y -= 1

    MOVES += 1
    # print("Attempted Moves: " + str(MOVES))

    set_current_direction()
    set_next_direction(X, Y)
    # print_testing_loop_details()
    if check_transverable() is True:
        enter_the_maze(X, Y)
    else:
        if NEXT_DIRECTION == 'h':
            print("\n\nHOME - END")
        else:
            print("\n\nINFINITE LOOP")


def print_testing_loop_details():
    print("\n\n" + "_" * 20)
    display_maze()
    print("\n\nCurrent Direction: " + CURRENT_DIRECTION)
    print("Next Direction: " + NEXT_DIRECTION)
    print("_" * 20)

def check_transverable():
    value = True
    directional_infinite_loop_opposites = {
                                Compass.SOUTH: Compass.NORTH,
                                Compass.EAST: Compass.WEST,
                                Compass.NORTH_EAST: Compass.SOUTH_WEST,
                                Compass.NORTH_WEST: Compass.SOUTH_EAST
                            }
    for key in directional_infinite_loop_opposites.keys():
        if (key.value[2] == CURRENT_DIRECTION) and (directional_infinite_loop_opposites.get(key).value[2] == NEXT_DIRECTION):
            value = False
            break
    return value


def loop(x, y):
    enter_the_maze(x, y)
    if DIRECTION == 'h':
        print("\nHome 'h' - Co-ordinate")
    else:
        while (check_transverable() is True): #or (DIRECTION != 'h'): #and (check_transverable() is True):
            move_your_pos()


def set_current_direction():
    global CURRENT_DIRECTION, DIRECTION
    CURRENT_DIRECTION = DIRECTION


def set_next_direction(x, y):
    global NEXT_DIRECTION
    NEXT_DIRECTION = maze.get(x)[y]


def check_solvable_by_co_ord():
    x = int(input('\n\nEnter Row: '))
    y = int(input('Enter Index: '))
    loop(x, y)


def check_xy_solvable():
    for keys in range(len(maze.keys())):
        for items in range(len(maze.get(keys))):
            print("\nStarting Co-Ordinates (X,Y): " + str(keys)+","+str(items))
            loop(keys, items)


if __name__ == "__main__":
    display_maze()
    # check_solvable_by_co_ord()

    check_xy_solvable()
