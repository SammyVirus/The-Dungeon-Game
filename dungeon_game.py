import random
import os


print("\n\n\n              ***Welcome To the dungeon game!!***   \n")
n = int(input("       Please Enter the size of the grid you want to play in :>>  "))
CELLS = []
for a in range(n):
    for b in range(n):
        pair = (b, a)
        CELLS.append(pair)

def get_locations():
    return random.sample(CELLS, 3)
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')    
             
def move_player(player, move):
    x, y = player
    if move == "LEFT":
        x = x-1
    if move == "RIGHT":
        x = x+1
    if move == "UP":
        y = y-1
    if move == "DOWN":
        y = y+1
    return x, y
    
def move_monster(monster, valid_moves):
    x, y = monster
    move = random.choice(valid_moves)
    if move == "LEFT":
        x = x-1
    elif move == "RIGHT":
        x = x+1
    elif move == "UP":
        y = y-1
    elif move == "DOWN":
        y = y+1
    elif move == "DOWNLEFT":
        y = y+1
        x = x-1
    elif move == "DOWNRIGHT":
        y = y+1
        x = x+1
    elif move == "UPLEFT":
        y = y-1
        x = x-1
    elif move == "UPRIGHT":
        y = y+1
        x = x+1
    return x, y
        

def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if y == 0:
        moves.remove("UP")
    if y == n-1:
        moves.remove("DOWN")
    if x == 0:
        moves.remove("LEFT")
    if x == n-1:
        moves.remove("RIGHT")
    return moves
    
def valid_monster_moves(monster, door):
    moves = ["NOMOVE", "LEFT", "RIGHT", "UP", "DOWN", "DOWNLEFT", "DOWNRIGHT", "UPLEFT", "UPRIGHT"]
    xm, ym = monster
    xd, yd = door
    if((ym == 0) or ((xm==xd) and (ym-yd == 1))):
        moves.remove("UP")
    if((ym == n-1) or ((xm==xd) and (ym-yd == -1))):
        moves.remove("DOWN")
    if((xm == 0) or ((ym==yd) and (xm-xd == 1))):
        moves.remove("LEFT")
    if((xm == n-1) or ((ym==yd) and (xm-xd == -1))):
        moves.remove("RIGHT")
    if((xm == 0) or (ym == 0) or ((xm-xd == 1) and (ym-yd == 1))):
        moves.remove("UPLEFT")
    if((xm == n-1) or (ym == 0) or ((xm-xd == -1) and (ym-yd == 1))):
        moves.remove("UPRIGHT")
    if((xm == 0) or (ym == n-1) or ((xm-xd == 1) and (ym-yd == -1))):
        moves.remove("DOWNLEFT")
    if((xm == n-1) or (ym == n-1) or ((xm-xd == -1) and (ym-yd == -1))):
        moves.remove("DOWNRIGHT")
    return moves

def draw_map(player, monster, door):
        print(" _"*n)
        tile = "|{}"

        if ((player != monster) and (player != door)):
            for cell in CELLS:
                x,y = cell
                if x<n-1:
                    line_end = ""
                    if cell == player:
                        output = tile.format("X")
                    elif cell == monster:
                        output = tile.format("€")
                    else:
                        output = tile.format("_")
                else:
                    line_end = "\n"
                    if cell == player:
                        output = tile.format("X|")
                    elif cell == monster:
                        output = tile.format("€|")
                    else:
                        output = tile.format("_|")
                print(output, end=line_end)
        elif((player == monster) or (player == door)):
            for cell in CELLS:
                x,y = cell
                if x<n-1:
                    line_end = ""
                    if cell == monster:
                        output = tile.format("€")
                    elif cell == door:
                        output = tile.format("+")
                    else:
                        output = tile.format("_")
                else:
                    line_end = "\n"
                    if cell == monster:
                        output = tile.format("€|")
                    elif cell == door:
                        output = tile.format("+|")
                    else:
                        output = tile.format("_|")
                print(output, end=line_end)
            
def game_loop():
    
    monster, door, player = get_locations()
    while True:
        
        valid_moves = get_moves(player)
        monster_valid_moves = valid_monster_moves(monster, door)
        print("You're currently in room ({}, {})".format(player[1]+1, player[0]+1))
        print("Monster is currently in room ({}, {})".format(monster[1]+1, monster[0]+1))
        print("You can move {}".format(", ".join(valid_moves)))
        print("Enter QUIT to quit")
        draw_map(player, monster, door)
        
        if player == monster:
            response = input("\n ** OH NOOO!! The monster got you. **\n Do you Want To Play Again? (Y/N) : ")
            response = response.upper()
            if response == "Y":
                clear_screen()
                monster, door, player = get_locations()
                continue
            if response == "N":
                break
        if player == door:
            response = input("\n ** CONGO!!! You Escaped **\n Do You Want To Play Again? (Y/N) : ")
            response = response.upper()
            if response == "Y":
                clear_screen()
                monster, door, player = get_locations()
                continue
            if response == "N":
                break
        	
        move  = input("> ")
        move = move.upper()
		
        if move == "QUIT":
	        break
        if move in valid_moves:
                player = move_player(player, move)
                monster = move_monster(monster, monster_valid_moves)
        else:
                print("\n ** Walls are hard! Don't run into them! **")
                input(" ** Press Enter to try another move **")
        clear_screen()


if(n>1):
    clear_screen()
    print("Welcome to the dungeon!")
    input("Press return to start!")
    clear_screen()
    game_loop()
else:
    print("         Please Pick a grid of size larger than 1 !! ")
    
            
        
        
        
