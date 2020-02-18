dictionary = {'x': [], 'o': []}
player = dictionary['x']
gameStatus = 0
board = ['_', '|', '_', '|', '_', '\n', '_', '|', '_', '|', '_', '\n', ' ', '|', ' ', '|', ' ']

def view():
        for d in dictionary['x']:
            board[d*2]= 'x'
        for d in dictionary['o']:
            board[d*2]= 'o'
        print(''.join(board))

view()

from wonlost import*

def isInputValid(conin, dictionary):
    if not conin.isdigit():
        return False
    v = int(conin)
    if v < 1 or  v > 9:
        return False
    c = v-1
    for m in dictionary:
        if c in dictionary[m]:
            return False
    return True

#print(isInputValid('1', {'x': [1]}))

def inputCorrectDigit():
    conin = input()
    while not isInputValid(conin, dictionary): 
        print("Please enter a digit from 1 to 9:")
        conin = input()
    return int(conin)-1
   
while wonlost(dictionary) == 0:
    v = inputCorrectDigit()
    player.append(v)
    gameStatus = wonlost(dictionary)
    if wonlost(dictionary) == 0:
        player = dictionary['o'] if player is dictionary['x'] else dictionary['x']
    view()

if wonlost(dictionary) == 1:
    print('Draw - Game over!')
elif wonlost(dictionary) == 2:
    print( 'Player X won! - Game over!' if player is dictionary['x'] else 'Player O won! - Game over!')
