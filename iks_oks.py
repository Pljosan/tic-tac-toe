#3x3

#function for printing current state
def print_state(m):
    for i in range(0, 3):
        for j in range (0, 3):
            print m[i][j],
            if j != 2:
                print "|",
        print ""
        if i != 2:
            print "-----------"

#m[i][j].strip() == 'X' or m[i][j].strip == 'O'
#i is the current player so i == 'X' or i == 'O'
def check_if_player_won(m, i):
    if m[0][0].strip() == i and m[0][1].strip() == i and m[0][2].strip() == i:
        return 0
    elif m[1][0].strip() == i and m[1][1].strip() == i and m[1][2].strip() == i:
        return 0
    elif m[2][0].strip() == i and m[2][1].strip() == i and m[2][2].strip() == i:
        return 0
    elif m[0][0].strip() == i and m[1][0].strip() == i and m[2][0].strip() == i:
        return 0
    elif m[0][1].strip() == i and m[1][1].strip() == i and m[2][1].strip() == i:
        return 0
    elif m[0][2].strip() == i and m[1][2].strip() == i and m[2][2].strip() == i:
        return 0
    elif m[0][0].strip() == i and m[1][1].strip() == i and m[2][2].strip() == i:
        return 0
    elif m[0][2].strip() == i and m[1][1].strip() == i and m[2][0].strip() == i:
        return 0
    else:
        return 1

matrix = [["  ", " ", " "], ["  ", " ", " "], ["  ", " ", " "]]
current_player = 'X'

print_state(matrix)

while True:
    turn = "It's " + current_player + "'s turn to play"
    print turn

    first_coordinate = 7 #needs to be greater than 2 so while loop starts
    second_coordinate = 7 #needs to be greater than 2 so while loop starts
    first_coordinate_indicator = 0
    second_coordinate_indicator = 0

    while (first_coordinate > 2) or (first_coordinate < 0):
        if first_coordinate_indicator == 1:
            print "Failed to insert the first coordinate, choose a number in [0, 2]"
        first_coordinate = int(raw_input("Insert the first coordinate: "))
        first_coordinate_indicator = 1

    while (second_coordinate > 2) or (second_coordinate < 0):
        if second_coordinate_indicator == 1:
            print "Failed to insert the second coordinate, choose a number in [0, 2]"
        second_coordinate = int(raw_input("Insert the second coordinate: "))
        second_coordinate_indicator = 1

    if (matrix[first_coordinate][second_coordinate] != " ") and (matrix[first_coordinate][second_coordinate] != "  "):
        print "That field is already filled"
        continue

    if current_player == 'X':
        if second_coordinate == 0:
            matrix[first_coordinate][second_coordinate] = ' X'
        else:
            matrix[first_coordinate][second_coordinate] = 'X'
    else:
        if second_coordinate == 0:
            matrix[first_coordinate][second_coordinate] = ' O'
        else:
            matrix[first_coordinate][second_coordinate] = 'O'

    victory_indicator = check_if_player_won(matrix, current_player)

    print_state(matrix)

    if victory_indicator == 0:
        print "Player", current_player, "won!"
        break

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

    indicator = 0
    for i in range(0, 3):
        for j in range (0, 3):
            #if you find one free slot, set the indicator to 1, telling us
            #the game is still on
            if (matrix[i][j] == '  ') or (matrix[i][j] == ' '):
                indicator = 1
    if indicator == 0:
        print "It's a tie!"
        break
