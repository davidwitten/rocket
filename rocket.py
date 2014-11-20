# Rocket
# David Witten, Noah Kim

"""

Rocket Syntax

Comments
#Comment

Input and Output
\<a-zA-Z>   outputs variable to stream

Identities
<a-z>   number variables 1
<A-Z>   list variables [1, 2, 3]

Identity Operations
<a-zA-Z>:expression      set number or list
<a-zA-Z>                 get number or list 
A.b:expression           set list element at index b
A.b                      get list element at index b

Number Operations
+   add
-   subtract
*   multiply
/   divide
%   mod
^   power

List Operations
$   length

Comparisons
=    equal 
>    greater
<    less

Boolean
&   and
|   or
~   not

Grouping
(...)   higher precedence operation

Control
?(<expression>){}     if
!(<expression>){}     while

"""

# Import
import fractions
from ply import lex
from ply import yacc

# Lexer
tokens = [
    "COMMENT",

    "BACKSLASH",
    
    "NUMBER",
    "NUMBERVARIABLE", "LISTVARIABLE",

    "SQUOTE", "DQUOTE",
    
    "PLUS", "MINUS", "TIMES", "DIVIDE", "MOD", "POWER",
    "DOLLAR",

    "EQUAL", "GREATER", "LESS",
    "AND", "OR", "NOT",

    "QUESTION", "EXCLAMATION",
    
    "LPAREN", "RPAREN",
    "LBRACKET", "RBRACKET",
    "LBRACE", "RBRACE",
    
    "SEMICOLON", "COLON",
    "COMMA", "PERIOD"
]

def t_COMMENT(t):
    r"\#.*"
    pass

t_BACKSLASH = r"\\"

def t_NUMBER(t):
    r"\d+(\.d+)?"
    t.value = fractions.Fraction(t.value)
    return t

t_NUMBERVARIABLE = r"[a-z]"
t_LISTVARIABLE = r"[A-Z]"

t_SQUOTE = r"'"
t_DQUOTE = r"\""

t_PLUS = r"\+"
t_MINUS = r"\-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MOD = r"%"
t_POWER = r"\^"
t_DOLLAR = r"\$"

t_EQUAL = r"="
t_GREATER = r">"
t_LESS = r"<"
t_AND = r"&"
t_OR = r"\|"
t_NOT = r"~"

t_QUESTION = r"\?"
t_EXCLAMATION = "!"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_LBRACE = r"\{"
t_RBRACE = r"\}"

t_SEMICOLON = r";"
t_COLON = r":"
t_COMMA = r","
t_PERIOD = r"\."

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = " \t"

def t_error(t):
    print("bad character %s" % t.value)
    t.lexer.skip(1)

lex.lex()
s = "a:1;?(a>0){a:a+1;}{\\a;}"
lex.input(s)

while True:
    token = lex.token()
    if not token: break      # No more input
    print(token)

