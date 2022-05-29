import random
import string
# grid will be represented as a 2 deep list
# ships will be represented as occupied spaces in the list
WIDTH = 10
HEIGHT = 10

L2N = {list(string.ascii_uppercase[:10])[i]:i for i in range(HEIGHT)}

def adj(i1,i2):
    return abs(ord(i1[0])-ord(i2[0]))+abs(int(i1[1])-int(i2[1]))==1

def get_value(coord, p):
    return p[L2N[coord[0]]][int(coord[1])]

def set_value(coord, p, ship):
    p[L2N[coord[0]]][int(coord[1])] = ship

def key():
    print(r"""
    KEY FOR YOUR BOARD:
    0: No battleship
    1-5: battleship of n length
    8: hit
    9: sunk

    KEY FOR OPPONENTS BOARD:
    0: unknown
    8: hit
    9: sink
    """)

def board(p1, p2):
    letters = "  ".join(list(string.ascii_uppercase)[:10])
    print()
    print(f'    YOUR BOARD                      |    OPPONENT\'S BOARD')
    print(f'    {letters}    |    {letters}')
    for i in range(10):
        print(f" {i} {p1[i]}   | {i} {p2[i]}")

def game_start():
    while True:
        print("""
        Welcome to Battleship!
        Enter 'new' to start a new game.
        Enter 'quit' to quit.
        """)
        command = input("Command: ")
        if command == "new":
            game_loop()
        elif command == "quit":
            break
        else:
            print("Invalid command.")

def game_loop():
    # generates two new boards
    p1 = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]
    p2 = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]


    while True:
        # 1, 2, 3, 4, 5
        ships = {
            "carrier": 5,
            "battleship": 4,
            "cruiser": 3,
            "destroyer": 2,
            "dingy": 1
        }
        placed_ships = {}
        
        # place ships
        # fix this


        print("Choose a ship to place")
        for ship, length in ships.items():
            print(f"{ship}: {length}")
        print()

        ship = input("Ship: ")
        if ship not in ships:
            print("Invalid ship")
            continue

        length = ships[ship]
        print("Choose a starting coordinate")

        coord = input("Coordinate: ")
        # check length of ship, check if coord is valid
        # check if coord is in bounds
        # check if coord is empty

        # makes sure coord is valid
        if len(coord) != 2:
            print("Invalid coordinate")
            continue
        if coord[0] not in L2N or coord[1] not in range(WIDTH):
            print("Invalid coordinate")
            continue
        if get_value(coord, p1) != 0:
            print("Invalid coordinate")
            continue

        direction = input("Direction (l/r/u/d): ")
        if direction not in ["l", "r", "u", "d"]:
            print("Invalid direction")
            continue
        if direction == "l":
            for i in range(length):
                if get_value(coord, p1) != 0:
                    print("Invalid coordinate")
                    break
                coord = chr(ord(coord[0])-1) + coord[1]





        # for ship, length in ships.items():
        #     if ship in placed_ships:
        #         continue
        #     print(f"Place your {ship} ({length} spaces)")
        #     coord = input("Enter a coordinate: ")
        #     direction = input("Enter a direction: ")

        #     # check if ship is in bounds
        #     if direction == "horizontal":
        #         if int(coord[1])+length > WIDTH:
        #             print("Ship is out of bounds.")
        #             continue
        #     elif direction == "vertical":
        #         if L2N[coord[0]]+length > HEIGHT:
        #             print("Ship is out of bounds.")
        #             continue

    # while True:
    #     coord = input("Enter a coordinate: ")
    #     if coord == "quit":
    #         break
    #     if coord == "key":
    #         key()
    #         continue
    #     if coord == "board":
    #         board(p1, p2)
    #         continue
    #     if coord == "help":
    #         print("""
    #         Enter a coordinate to fire at.
    #         Enter 'quit' to quit the game.
    #         Enter 'key' to see the key for the board.
    #         Enter 'board' to see the board.
    #         """)
    #         continue
    #     if len(coord) != 2:
    #         print("Invalid coordinate.")
    #         continue
    #     if not coord[0].isalpha() or not coord[1].isdigit():
    #         print("Invalid coordinate.")
    #         continue
    #     if get_value(coord, p2) != 0:
    #         print("You already fired at that coordinate.")
    #         continue
    #     if get_value(coord, p1) == 0:
    #         print("You missed.")
    #         set_value(coord, p2, 8)
    #     else:
    #         print("You hit a battleship!")
    #         set_value(coord, p2, 9)
    #     board(p1, p2)
    main()


def main():





    print()


if __name__ == "__main__":
    main()
