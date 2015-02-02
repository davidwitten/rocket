# Rocket
# David Witten, Noah Kim

# Import
import fractions
from ply import lex
from ply import yacc

from rocketlex import *
from rocketyacc import *

# Lex
lex.lex()
s = "a: -5^-2"

lex.input(s)

# Yacc
yacc.yacc()
result = yacc.parse()
print(result)

