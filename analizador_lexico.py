import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'INCLUDE', 'LIBRARY', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN',
    'INT', 'MAIN', 'RETURN', 'FOR', 'ASSIGN', 'SEMICOLON', 'NUMBER',
    'PLUS', 'MULT_OP', 'ID', 'COMMA', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NE'
)

# Expresiones regulares para tokens simples
t_INCLUDE = r'\#include'
t_LT = r'\<'
t_GT = r'\>'
t_LE = r'\<='
t_GE = r'\>='
t_EQ = r'=='
t_NE = r'!='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MULT_OP = r'\*'
t_COMMA = r','

# Expresión regular para las librerías
def t_LIBRARY(t):
    r'stdio\.h'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica si es una palabra reservada
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Manejador de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}, posición {t.lexpos}")
    t.lexer.skip(1)

# Definiciones de palabras reservadas
reserved = {
    'int': 'INT',
    'main': 'MAIN',
    'return': 'RETURN',
    'for': 'FOR'
}

# Definición del analizador léxico
lexer = lex.lex()

# Definición de la gramática
def p_program(p):
    '''program : include function'''
    p[0] = ('program', p[1], p[2])

def p_include(p):
    '''include : INCLUDE LT LIBRARY GT'''
    p[0] = ('include', p[3])

def p_function(p):
    '''function : INT MAIN LPAREN RPAREN LBRACE statements RBRACE'''
    p[0] = ('function', 'main', p[6])

def p_statements(p):
    '''statements : statement
                  | statement statements'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | for_statement
                 | return_statement'''
    p[0] = p[1]

def p_declaration(p):
    '''declaration : INT ID ASSIGN NUMBER SEMICOLON
                   | INT ID SEMICOLON'''
    if len(p) == 6:
        p[0] = ('declaration', 'int', p[2], p[4])
    else:
        p[0] = ('declaration', 'int', p[2])

def p_assignment(p):
    '''assignment : ID ASSIGN expression SEMICOLON'''
    p[0] = ('assignment', p[1], p[3])

def p_for_statement(p):
    '''for_statement : FOR LPAREN assignment condition SEMICOLON increment RPAREN LBRACE statements RBRACE'''
    p[0] = ('for', p[3], p[5], p[7], p[10])

def p_condition(p):
    '''condition : ID LT NUMBER
                 | ID LE NUMBER
                 | ID GT NUMBER
                 | ID GE NUMBER
                 | ID EQ NUMBER
                 | ID NE NUMBER'''
    p[0] = ('condition', p[1], p[2], p[3])

def p_increment(p):
    '''increment : ID PLUS PLUS'''
    p[0] = ('increment', p[1], '++')

def p_return_statement(p):
    '''return_statement : RETURN NUMBER SEMICOLON'''
    p[0] = ('return', p[2])

def p_expression(p):
    '''expression : NUMBER
                  | ID MULT_OP NUMBER
                  | ID PLUS ID'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '*':
        p[0] = ('mul', p[1], p[3])
    elif p[2] == '+':
        p[0] = ('add', p[1], p[3])

# Manejador de errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' en la línea {p.lineno}, posición {p.lexpos}")
    else:
        print("Error de sintaxis en EOF - se esperaba más código o una estructura de bloque está incompleta")

# Definición del analizador sintáctico
parser = yacc.yacc()

# Código en C estándar que deseas analizar
data_c = '''
#include <stdio.h>
int main() {
    int z = 0;
    int val = 0;
    int suma = 0;
    for(z = 0; z <= 10; z++){
        val = z * 10;
        suma = suma + val;
    } 
    return 0;
}
'''

# Ejecutar el analizador léxico y sintáctico
lexer.input(data_c)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok.type)

result = parser.parse(data_c)
print("Resultado del análisis sintáctico:", result)
