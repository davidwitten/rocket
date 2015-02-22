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
ply.yacc.parser = ply.yacc

# File
def run(path):
    with open(path) as file:
        code = file.read()
    ply.lex.input(code)
    result = ply.yacc.parse(lexer=ply.lex, tracking=1)
    return result

# Main
def shell():
    while True:
        s = input("> ")
        if s == "quit": break
        if s and not s.endswith(";"): s += ";"
        ply.lex.input(s)
        ast = ply.yacc.parse(lexer=ply.lex)
        print(ast)
