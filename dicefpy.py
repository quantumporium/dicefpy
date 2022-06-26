#! usr/bin/python3

"""
 name: dice for python (diceFpy in short)
 author: quantumporium (quatumporium@github.com)
 
"""
# import
from random import randint as randomNb
from sys import argv

# library of function : code start at line ->
def usage():
    """
    non-pure function, print the usage of the script

    """
    print("""
        name: diceFpy
        standar usage: ./diceFpy [option] [option] or python diceFpy [option]
        usage  option:
                        -h : give the help/usage text for the scrypt
                        -n [integer] : n allow multiple instace of dice

        example usage: ./diceFpy
                        >>  [2]

                        ./ diceFpy -3
                        >>  [3] 
                        >>  [10]
                        >>  [9]
    """)
    return

def fatal():
    print("[ ERROR ] an fatal error occur, the program will stop shortly ...")
    exit()
    return

def print_dice(parsed_arg):
    """
        non-pure function, print random dice with minimalist style

    """
    if parsed_arg[0] == "empty":
        ammout_dice = 0
    elif parsed_arg[0] == "number":
        amount_dice = parsed_arg[1]

    for option in len(int(ammount_dice)):
        print(f"[{randomNb(1, 12)}]") 
    
    return

def parse_arg(argv):
    """    
        pure function, parse the terminal command 
    """
    if argv[1:] == None:
        return [ "empty" ] 

    if "-h" in argv:
        return [ "help" ] 

    if "-n" in argv:
        return [ "number", argv( index("-n") + 1 ) ]

    print(argv)

    return

"""
    parse argue
        -> -h (show usage)
        -> nothing print one dice
        -> -n 10 (print multiple dice)
        -> -l (print dice in the same line)
"""

if __name__ == "__main__":

    parsed_arg = parse_arg(argv)

    if parsed_arg[0] == "help":
        usage()

    elif parsed_arg[0] == "empty":
        print_dice( parsed_arg )

    elif parsed_arg[0] == "number":
        print_dice( parsed_arg )

    else:
        fatal()
