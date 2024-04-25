from lex import *
from emit import *
from parse import *
import sys
import os

if __name__ == "__main__":
    print("Teeny Tiny Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    # Initialize the lexer and parser.
    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    os.system(f"gcc out.c -o " + sys.argv[1].rstrip(".teeny"))
    print("Compiling completed.")