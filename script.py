import ply.lex as lex;

reserved = {
    'print' : 'PRINT',
    'cat' : 'CAT',
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE'
}

tokens = [
'ID',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'MODULO',
'EQUALS',
'LPAREN',
'RPAREN',
'LBRACKET',
'RBRACKET',
'LT',
'LE',
'GT',
'GE',
'ET',
'NE',
'COMMA',
'SEMICOLON',
'FLOAT',
'INTEGER',
'STRING',
'BOOLEAN'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'\%\%'
t_EQUALS = r'<-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_ET = r'=='
t_NE = r'!='
t_COMMA = r'\,'
t_SEMICOLON = r';'
t_STRING = r'\".*?\n*\"'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_FLOAT(t):
    r'[+-]?\d*\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t

def t_BOOLEAN(t):
    r'T(RUE)? | F(ALSE)?'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s" %t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

lexer = lex.lex()

# Print Statement
# data = 'print("Hello, world!")\n'
# data += 'cat("Thanks")\n'

# Arithmetic Expression
# data = 'num1 <- 10\n'
# data += 'num2 <- 20\n'
# data += 'num3 <- 30\n'
# data += 'sum <- num1 + num2 + num3\n'
# data += 'avg <- sum / 3\n'

# Conditional IF ELSE
# data = 'num <- 10\n'
# data += 'num <- 20\n'
# data += 'if(num1 > num2){\n'
# data += '   bignum<-num1;\n'
# data += '   cat("Big Number is ", bignum, "\n")\n'
# data += '}else{\n'
# data += '   bignum<-num2;\n'
# data += '   cat("Big Number is ", bignum, "\n")\n'
# data += '}\n'

# Looping with Conditional IF ELSE
# data = 'cat("List of odd numbers 1-100: \n")\n'
# data += 'num <- 1\n'
# data += 'while (num <= 100){\n'
# data += '   sisa <- num %% 2\n'
# data += '   if(sisa != 0){\n'
# data += '       oddnum <- num\n'
# data += '       cat(oddnum, " ");\n'
# data += '   }\n'
# data += '   num <- num + 1\n'
# data += '}\n'

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)