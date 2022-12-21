import ply.yacc as yacc

from rLexical import tokens

# Print Statement
def p_print_statement(p):
    'print_statement : PRINT LPAREN expression_list RPAREN'
    for expression in p[3]:
        print(expression)

def p_expression_list(p):
    '''expression_list : expression_list COMMA expression 
        | expression'''
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = [p[1]]

def p_expression(p):
    'expression : STRING'
    p[0] = p[1]

# Aritmethic Expression
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]
    
def p_expression_minus(p):	
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]
    
def p_expression_times(p):	
    'expression : expression TIMES term'
    p[0] = p[1] * p[3]
    
def p_expression_divide(p):	
    'expression : expression DIVIDE term'
    p[0] = p[1] / p[3]

def p_term_lessthan(p):
    'expression : term LE term'

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_num(p):
    'term : NUMBER'
    p[0] = p[1]

# def p_relexpr(p):
#     '''relexpr : expr LT expr
#                 | expr LE expr
#                 | expr GT expr
#                 | expr GE expr
#                 | expr EQUALS expr
#                 | expr NE expr'''
#     p[0] = ('RELOP', p[2], p[1], p[3])

def p_comparison_binop(p):
    '''comparison : expression EQUAL expression'''
    if p[2] == '==':
        p[0] = p[1] == p[3]

# def p_expression_number(p):
#     '''term : INTEGER
#             | FLOAT'''
#     p[0] = ('NUMBER', eval(p[1]))

def p_error(p):
    print("Syntax error in input!")



# If Else

# def p_statement(p):
#     '''statement : if_statement
#                  | assignment'''
#     p[0] = p[1]

# def p_if_statement(p):
#     '''if_statement : IF LPAREN expression RPAREN LBRACKET statement_list RBRACKET
#                     | IF LPAREN expression RPAREN LBRACKET statement_list RBRACKET ELSE LBRACKET statement_list RBRACKET'''
#     if len(p) == 7:
#         p[0] = ('if', p[3], p[6])
#     else:
#         p[0] = ('if', p[3], p[6], 'else', p[10])

# def p_statement_list(p):
#     '''statement_list : statement_list statement
#                       | statement'''
#     if len(p) == 2:
#         p[1].append(p[2])
#         p[0] = p[1]
#     else:
#         p[0] = p[1]

# def p_statement(p):
#     '''statement : print_statement'''
#     p[0] = p[1]

# def p_if_statement(p):
#     '''if_statement : IF LPAREN CONDITION RPAREN LBRACKET STATEMENT RBRACKET
#                     | IF LPAREN CONDITION RPAREN LBRACKET STATEMENT RBRACKET ELSE LBRACKET STATEMENT RBRACKET'''
#     if len(p) == 8:
#         if eval(p[3]):
#             exec(p[6])
#     else:
#         if eval(p[3]):
#             exec(p[6])
#         else:
#             exec(p[10])

def p_statement_if(p):
    '''statement : IF LPAREN comparison RPAREN LBRAKET statement RBRAKET
                 | IF LPAREN comparison RPAREN LBRAKET statement RBRAKET ELSE LBRAKET statement RBRAKET'''
    if p[3]:
        p[0] = p[6]
    else:
        if p[10] is not None:
            p[0] = p[10]

# Looping

#Building Parser
parser = yacc.yacc()
# parser.parse('print("Hello, world!")')

while True:
   try:
       s = input('R > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   if(result):
    print(result)