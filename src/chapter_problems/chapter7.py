import copy
import sys

STARTING_PIECES = {"a8": "bR", "b8": "bN", "c8": "bB", "d8": "bQ",
"e8": "bK", "f8": "bB", "g8": "bN", "h8": "bR", "a7": "bP", "b7": "bP",
"c7": "bP", "d7": "bP", "e7": "bP", "f7": "bP", "g7": "bP", "h7": "bP",
"a1": "wR", "b1": "wN", "c1": "wB", "d1": "wQ", "e1": "wK", "f1": "wB",
"g1": "wN", "h1": "wR", "a2": "wP", "b2": "wP", "c2": "wP", "d2": "wP",
"e2": "wP", "f2": "wP", "g2": "wP", "h2": "wP"}

MAX_PIECES = {"bR": 2, "bN": 2, "bB": 2, "bQ": 1, "bK": 1, "bP": 8, "wR": 2, "wN": 2, "wB": 2, "wQ": 1, "wK": 1, "wP": 8}

rows = ["1", "2", "3", "4", "5", "6", "7", "8"]
columns = ["a", "b", "c", "d", "e", "f", "g", "h"]

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""

WHITE_SQUARE = "||"
BLACK_SQUARE = "  "

def print_chessboard(board):
    squares = []
    is_white_square = True
    for y in "87654321":
        for x in "abcdefgh":
            #print(x, y, is_white_square)  # DEBUG: Show coordinates  # noqa: ERA001
            if x + y in board:
                squares.append(board[x + y])
            elif is_white_square:
                squares.append(WHITE_SQUARE)
            else:
                squares.append(BLACK_SQUARE)
            is_white_square = not is_white_square
        is_white_square = not is_white_square

    print(BOARD_TEMPLATE.format(*squares))



def main():  # noqa: C901
    main_board = copy.copy(STARTING_PIECES)

    while True:
        print_chessboard(main_board)
        response = input([">"])

        if response[0] == "move":
            main_board[response[2]] = main_board[response[1]]
            del main_board[response[1]]
        elif response[0] == "remove":
            del main_board[response[1]]
        elif response[0] == "set":
            main_board[response[1]] = response[2]
        elif response[0] == "reset":
            main_board = copy.copy(STARTING_PIECES)
        elif response[0] == "clear":
            main_board = {}
        elif response[0] == "fill":
            for y in "87654321":
                for x in "abcdefgh":
                    main_board[x + y] = response[1]
        elif response[0] == "quit":
            sys.exit()


def chess_checker(board):
    def _raise_invalid(msg):
        raise ValueError(msg)

    try:
        piece_counts = MAX_PIECES.copy()
        for key, val in board.items():
            if val not in piece_counts:
                msg = "Invalid piece"+val
                _raise_invalid(msg)
            piece_counts[val] -= 1
            if piece_counts[val] < 0:
                msg = f"Too many {val}"
                _raise_invalid(msg)
            if len(key) != 2 or key[0] not in rows or key[1] not in columns:  # noqa: PLR2004
                msg = "invalid row/column"
                _raise_invalid(msg)
    except ValueError as exc:
        print(exc)

def print_inventory(inventory_dict):
    piece_counts = 0
    print("Inventory:")
    for key, value in inventory_dict.items():
        print(f"{value} {key}")
        piece_counts+=value
    print(f"Total number of items: {piece_counts}")

def add_inventory(original_inventory, added_item_list):
    for item in added_item_list:
        original_inventory[item] = original_inventory.get(item,0) + 1
    return original_inventory

if __name__ == "__main__":
    """[summary]"""
    main()
    inventory = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    print_inventory(inventory)
    print_inventory(add_inventory(inventory, loot))


""" Chapter Questions
1.What does the code for an empty dictionary look like?
di = {}
2.What does a dictionary value with a key "foo" and a value 42 look like?
{"foo":42}
3.What is the main difference between a dictionary and a list?
A dictionary uses many data types to serve as index, while a list is only integer.
4.What happens if you try to access spam["foo"] if spam is {"bar": 100}?
keyerror
5.If a dictionary is stored in spam, what is the difference between the expressions "cat" in spam and "cat" in spam.keys()?
Nothing
6.If a dictionary is stored in spam, what is the difference between the expressions "cat" in spam and "cat" in spam.values()?
"cat" in spam checks for "cat" in the keys of the dictionary. "cat" in spam.values() checks all the values of the dictionary for "cat"
7.What is a shortcut for the following code?
        if "color" not in spam:
            spam["color"] = "black"
spam.setdefault("black")
8.What module and function can be used to “pretty-print” dictionary values?
pprint.pprint(dict)
"""
