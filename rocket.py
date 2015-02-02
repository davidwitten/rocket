# Rocket
# David Witten, Noah Kim

# Import
import fractions
from ply import lex
from ply import yacc

from rocketlex import *
from rocketyacc import *

# Setup
namespace = {}

# Lex
lex.lex()
s = "1+5*-3.24"
lex.input(s)

# Yacc
yacc.yacc()
result = yacc.parse()
print(result)

