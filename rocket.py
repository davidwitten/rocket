# Rocket
# David Witten, Noah Kim

# Import
import sys
import ply.lex
import ply.yacc
import rocket.lexer
import rocket.parser

# Namespace
namespace = {}

# Build
ply.lex.lex(module=rocket.lexer)
ply.yacc.yacc(module=rocket.parser, debug=0)

# File
if len(sys.argv) == 2:
    with open(sys.argv[1]) as file:
        code = file.read()
    ply.lex.input(code)
    ply.yacc.parse(lexer=ply.lex)

# Main
def shell():
    while True:
        s = input("> ")
        if s == "quit": break
        if not s.endswith(";"): s += ";"
        ply.lex.input(s)
        result = ply.yacc.parse(lexer=ply.lex)
