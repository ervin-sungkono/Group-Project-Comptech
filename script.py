import ply.lex as lex;

tokens = [
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'RPAREN',
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s" %t.value[0])
    t.lexer.skip(1)

t_ignore = '\t'

lexer = lex.lex()

lexer.input('2*(2+3)')

while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)