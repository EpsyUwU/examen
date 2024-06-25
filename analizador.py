import ply.lex as lex
import ply.yacc as yacc

class MyParser:
    def __init__(self):
        self.variables = set()  # Conjunto para rastrear variables declaradas

    # Lista de tokens
    tokens = (
        'INCLUDE', 'LIBRARY', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN',
        'INT', 'MAIN', 'RETURN', 'FOR', 'ASSIGN', 'SEMICOLON', 'NUMBER',
        'PLUS', 'MULT_OP', 'ID', 'COMMA', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'
    )

    # Expresiones regulares para tokens simples
    t_INCLUDE = r'\#include'
    t_LT = r'\<'
    t_LE = r'\<='
    t_GT = r'\>'
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
    def t_LIBRARY(self, t):
        r'stdio\.h'
        return t

    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, 'ID')  # Acceder usando self
        return t

    # Ignorar espacios y tabulaciones
    t_ignore = ' \t'

    # Manejo de saltos de línea
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count('\n')

    # Manejador de errores
    def t_error(self, t):
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
    def build_lexer(self):
        self.lexer = lex.lex(module=self)

    # Definición de la gramática
    def build_parser(self):
        self.parser = yacc.yacc(module=self)

    def p_program(self, p):
        '''program : include function'''
        p[0] = ('program', p[1], p[2])

    def p_include(self, p):
        '''include : INCLUDE LT LIBRARY GT'''
        p[0] = ('include', p[3])

    def p_function(self, p):
        '''function : INT MAIN LPAREN RPAREN LBRACE statements RBRACE'''
        p[0] = ('function', 'main', p[6])

    def p_statements(self, p):
        '''statements : statement
                      | statement statements'''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[2]

    def p_statement(self, p):
        '''statement : declaration
                     | assignment
                     | for_statement
                     | return_statement'''
        p[0] = p[1]

    def p_declaration(self, p):
        '''declaration : INT ID ASSIGN NUMBER SEMICOLON'''
        if len(p) == 6:
            p[0] = ('declaration', 'int', p[2], p[4])
            self.variables.add(p[2])  # Agregar la variable declarada al conjunto
        else:
            p[0] = ('declaration', 'int', p[2])
            self.variables.add(p[2])

    def p_assignment(self, p):
        '''assignment : ID ASSIGN expression SEMICOLON'''
        if p[1] not in self.variables:
            raise Exception(f"Error: Variable no declarada en la línea {p.lineno(1)}")
        p[0] = ('assignment', p[1], p[3])

    def p_for_statement(self, p):
        '''for_statement : FOR LPAREN assignment condition SEMICOLON increment RPAREN LBRACE statements RBRACE'''
        p[0] = ('for', p[3], p[5], p[7], p[10])

    def p_condition(self, p):
        '''condition : ID LT NUMBER
                     | ID LE NUMBER
                     | ID GT NUMBER
                     | ID GE NUMBER
                     | ID EQ NUMBER
                     | ID NE NUMBER'''
        if p[1] not in self.variables:
            raise Exception(f"Error: Variable no declarada en la línea {p.lineno(1)}")
        p[0] = ('condition', p[1], p[2], p[3])

    def p_increment(self, p):
        '''increment : ID PLUS PLUS'''
        if p[1] not in self.variables:
            raise Exception(f"Error: Variable no declarada en la línea {p.lineno(1)}")
        p[0] = ('increment', p[1], '++')

    def p_return_statement(self, p):
        '''return_statement : RETURN NUMBER SEMICOLON'''
        p[0] = ('return', p[2])

    def p_expression(self, p):
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
    def p_error(self, p):
        if p:
            print(f"Error de sintaxis en '{p.value}' en la línea {p.lineno}, posición {p.lexpos}")
        else:
            print("Error de sintaxis en EOF - se esperaba más código o una estructura de bloque está incompleta")


if __name__ == "__main__":
    parser = MyParser()
    parser.build_lexer()
    parser.build_parser()

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

    # Ejecutar el análisis léxico y sintáctico
    result = parser.parser.parse(data_c)
    print("Resultado del análisis sintáctico:", result)

