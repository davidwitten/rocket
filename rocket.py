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
            print(' '.join( (eval(line[1:],Local).split() ) ) )
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
@a;
=0;
@b;
=1;
!b;
@a;

$<20000:;

@c;=b+a;
@a;=b;
@b;=c;
!b;

END;
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
@_a;
=[1,2,3,4,5];
&3;
&[1,2];
|;
=15 [0];
!_a[0];
'''

TestSort = '''
@_a;
=[1,2,3,2,1];
|;
!_a;
'''

script = '''
'''

main(TestAppend)
