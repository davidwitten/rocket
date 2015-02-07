<<<<<<< HEAD
#Rocket
#David W, Noah K

#Import
import string

"""
Syntax
! : output
? : input
@ : load (with variable) (_variable to denote list)

+ : addition
- : subtraction
* : multiplication
/ : division
% : modulus
^ : exponentiation

$ : while-loop
~ : if-statement

LIST:
& : add element
| : sorted list
[n] : index of list
"""

Local,Lists = {v: 0 for v in string.ascii_lowercase},{'_' + v:[] for v in string.ascii_lowercase}
Local.update(Lists)
current = ''
def Mapit(List,Operation):
    Operation = Operation[0] + str(eval(Operation[1:],Local))
    Operation = Operation.replace('^','**')
    return list(map(lambda x: eval('x' + Operation),List))
def interpret(line):
    global current
    global Local
    themain = ('_' in current)
    if not(themain):
        line = line.replace('^','**')
    if line.startswith("!"):
        if not(themain):
            print(eval(line[1:], Local))
        else:
            if '[' in line:
                print(' '.join(eval(line[1:],Local).split() ) )
            else:
                print(' '.join([str(i) for i in eval(line[1:],Local)]))
    elif line.startswith("?"):
        Local[line[1]] = eval(input("?%s " % line[1]))
    elif line.startswith("@"):
        current = line[1:]
    elif line.startswith("~"):
        if eval(str(Local[current]) + line[1:line.index(':')]):
            interpret(line[line.index(":") + 1:])

    elif line.startswith("="):
        assert current
        if not(themain) and '[' in line:#non-list
            raise TypeError("Integral variable name must have integral value")
        if ('[' in line.split()[-1]) and len(line.split()) != 1:
            n = ''.join([i for i in line.split()[-1] if i not in '[]'])
            Local[current][eval(n)] = line.split()[0][1:] #code would look like "=5 [0]"
        else:
             Local[current] = eval(line[1:], Local)
    elif line.startswith("&"):
        assert current
        if themain:
            if type(eval(line[1:],Local))!=list:
                Local[current].append(eval(line[1:],Local))
            else:
                Local[current].extend(eval(line[1:],Local))
        else:
            raise TypeError("List only function")
    elif line.startswith('|'):
        assert current
        if not(themain):
            raise TypeError("List only function")
        Local[current] = sorted(Local[current])
    elif line.startswith("#") or line == "":
        pass
    else:
        assert current
        if not(themain):
            
            Local[current] = eval(str(Local[current])+str(line),Local)
        else:
            Local[current] = Mapit(Local[current],line)

##        raise SyntaxError("Bad syntax: %s" % line)

def main(script):
    global current
    global Local
    trigger = False #True if in while loop

    lines = [line.strip() for line in script.split(';')]
    for place,line in enumerate(lines):
        if line.startswith("$"):
            trigger = True
            g = lines[place+1:lines.index("END")]
            assert current
            while eval(str(Local[current]) + line[1:line.index(':')]): #while CURRENT (comparison) :
                for inloop in g:
                    interpret(inloop)
        elif line == 'END':
            trigger = False
        else:
            if not(trigger):
                interpret(line)

###
'''Edit script below'''
### 

fibonacci = '''
@_a;=[1,1];

$[-1]<20000:;
@b;=0;+_a[-1];+_a[-2];
@_a;&b;
END;

!_a;
'''

TestIf = """
@a;
=3;
~<=4:*5;
!a;
"""
TestMapping= '''
@_a;
=[1,2,3,4,5];
^5;
*15;
!_a;'''

TestAppend = '''
@b;
=32;
@_a;
=[1,2,3,4,5];
&b;
&[1,2];
|;
=15 [0];
!_a;
'''

TestSort = '''
@_a;
=[1,2,3,2,1];
|;
!_a;
'''

script = '''
'''

main(fibonacci)
=======
# Rocket
# David Witten, Noah Kim


# Import
import fractions
from ply import lex
from ply import yacc


# Set up
namespace = {}


# Lexer
tokens = [
    "COMMENT", "NUMBER", "VARIABLE",
    
    "BACKSLASH", "QUESTION", "EXCLAMATION",
    "COLON", "SEMI", "PERIOD", "COMMA",

    "PLUS", "MINUS", "TIMES", "DIVIDE", "MODULUS", "POWER", "DOLLAR",
    "EQUALS", "GREATER", "LESS", "AND", "OR", "NOT",

    "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE",
]

def t_COMMENT(t):
    r"\#.*"
    pass

def t_NUMBER(t):
    r"([0-9]*\.[0-9]+|[0-9]+)"
    t.value = fractions.Fraction(t.value)
    return t

t_VARIABLE = r"[a-zA-Z]"

t_BACKSLASH = r"\\"
t_QUESTION = r"\?"
t_EXCLAMATION = r"!"
t_COLON = r":"
t_SEMI = r";"
t_PERIOD = r"\."
t_COMMA = r","

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MODULUS = r"%"
t_POWER = r"\^"
t_DOLLAR = r"\$"
t_EQUALS = r"="
t_GREATER = r"<"
t_LESS = r">"
t_AND = r"&"
t_OR = r"\|"
t_NOT = r"~"

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_LBRACE = r"\{"
t_RBRACE = r"\}"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("invalid character %s" % t.value)
    t.lexer.skip(1)

t_ignore = " \t"

lex.lex()


# Parser
precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
    ("left", "MODULUS"),
    ("right", "NEGATE"),
    ("left", "POWER"),
)

def p_statement_assignment(p):
    """statement : assignment"""
    pass

def p_assignment(p):
    """assignment : VARIABLE COLON expression"""
    namespace[p[1]] = p[3]
    p[0] = p[3]

def p_statement_expression(p):
    """statement : expression"""
    p[0] = p[1]

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

def p_expression_variable(p):
    """expression : VARIABLE"""
    p[0] = namespace[p[1]]

def p_expression_parenthesis(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_unary(p):
    """expression : MINUS expression %prec NEGATE"""
    if p[1] == "-": p[0] = -p[2]

def p_expression_binary(p):
    """expression : expression POWER expression
                  | expression MODULUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression PLUS expression
                  | expression MINUS expression
    """
    if p[2] == "^": p[0] = p[1] ** p[3]
    elif p[2] == "%": p[0] = p[1] % p[3]
    elif p[2] == "*": p[0] = p[1] * p[3]
    elif p[2] == "/": p[0] = p[1] / p[3]
    elif p[2] == "+": p[0] = p[1] + p[3]
    elif p[2] == "-": p[0] = p[1] - p[3]

def p_statement_print(p):
    """statement : BACKSLASH expression"""
    print(p[2])

def p_error(p):
    print("error", p)

yacc.yacc()


# Main
while True:
    s = input("> ")
    if s == "quit": break
    for line in s.split(";"):
        lex.input(line)
        result = yacc.parse(lexer=lex)

>>>>>>> rewrite
