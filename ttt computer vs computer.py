import random
a = ['_' for i in range(0, 9)]
global z
global x
global y
def my_input():
    print("---------")
    print("|", a[0], a[1], a[2], "|")
    print("|", a[3], a[4], a[5], "|")
    print("|", a[6], a[7], a[8], "|")
    print("---------")
my_input()
def my_coord():
    b = [random.randint(1, 3), random.randint(1, 3)]
    x = b[0]
    y = b[1]
    '''if (b[0].isnumeric() == False) or (b[1].isnumeric() == False):
        print("You should enter numbers!")
        my_coord()'''
    if int(x) > 3 or int(x) < 1 or int(y) > 3 or int(y) < 1:
        print("Coordinates should be from 1 to 3!")
        my_coord()
    elif int(x) == 1 and int(y) == 1 and a[6] == '_':
        a[6] = z
        my_input()
    elif int(x) == 1 and int(y) == 2 and a[3] == '_':
        a[3] = z
        my_input()
    elif int(x) == 1 and int(y) == 3 and a[0] == '_':
        a[0] = z
        my_input()
    elif int(x) == 2 and int(y) == 1 and a[7] == '_':
        a[7] = z
        my_input()
    elif int(x) == 2 and int(y) == 2 and a[4] == '_':
        a[4] = z
        my_input()
    elif int(x) == 2 and int(y) == 3 and a[1] == '_':
        a[1] = z
        my_input()
    elif int(x) == 3 and int(y) == 1 and a[8] == '_':
        a[8] = z
        my_input()
    elif int(x) == 3 and int(y) == 2 and a[5] == '_':
        a[5] = z
        my_input()
    elif int(x) == 3 and int(y) == 3 and a[2] == '_':
        a[2] = z
        my_input()
    else:
        print("This cell is occupied! Choose another one!")
        my_coord()
while True:
    def my_cond():
        in_seq = list(a)
        win_seq = [[a[0], a[1], a[2]], [a[3], a[4], a[5]], [a[6], a[7], a[8]], [a[0], a[3], a[6]], [a[1], a[4], a[7]], [a[2], a[5], a[8]], [a[0], a[4], a[8]], [a[2], a[4], a[6]]]
        win_x = ['X', 'X', 'X']
        win_o = ['O', 'O', 'O']
        if win_seq.__contains__(win_x) and not(win_seq.__contains__(win_x) and win_seq.__contains__(win_o)) and not(in_seq.count('X') >= in_seq.count('O') + 2):
            print('X wins')
            quit()
        elif win_seq.__contains__(win_o) and not(win_seq.__contains__(win_x) and win_seq.__contains__(win_o)) and not(in_seq.count('X') >= in_seq.count('O') + 2):
            print('O wins')
            quit()
        elif (in_seq.count('X') >= in_seq.count('O') + 2) or (in_seq.count('O') >= in_seq.count('X') + 2) or (win_seq.__contains__(win_x) and win_seq.__contains__(win_o)):
            print('Impossible')
        elif len(in_seq) == 9 and not (win_seq.__contains__(win_o) or win_seq.__contains__(win_x)) and not in_seq.__contains__('_'):
            print('Draw')
            quit()
    for j in range(9):
        if j % 2 == 0:
            z = 'X'
            my_cond()
            my_coord()

        else:
            z = 'O'
            my_cond()
            my_coord()





