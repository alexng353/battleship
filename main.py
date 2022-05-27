import random
import string
# grid will be represented as a 2 deep list
# ships will be represented as occupied spaces in the list
WIDTH = 10
HEIGHT = 10

L2N = {list(string.ascii_uppercase[:10])[i]:i for i in range(10)}

def parse_input(input_c1):
    return ({
        "x":"".join([i for i in input_c1 if i.isalpha()]),
        "y":"".join([i for i in input_c1 if not i.isalpha()])
    })

def check_adjacency(c1, c2, p1, p2):
    
    pass

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


def main():
    p1 = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]
    p2 = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]

    board(p1, p2)

    print()

if __name__ == "__main__":
    main()
