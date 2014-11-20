# Rocket
# David Witten, Noah Kim

"""

Rocket Syntax

Identities
<a-z>   number variables
<A-Z>   list variables

Identity Operations
expression->a     set number or list
a                 get number
expression->a:0   set list element
a:0               get list element 

Number Operations
+   add
-   subtract
*   multiply
/   divide
%   mod
^   power

List Operations
$   sort


Comparison
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
?(<expression>){...}   if
!(<expression>){...}   while


"""

# Import
import fractions

from ply import lex
from ply import yacc
