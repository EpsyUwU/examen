
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN COMMA EQ FOR GE GT ID INCLUDE INT LBRACE LE LIBRARY LPAREN LT MAIN MULT_OP NE NUMBER PLUS RBRACE RETURN RPAREN SEMICOLONprogram : include functioninclude : INCLUDE LT LIBRARY GTfunction : INT MAIN LPAREN RPAREN LBRACE statements RBRACEstatements : statement\n                      | statement statementsstatement : declaration\n                     | assignment\n                     | for_statement\n                     | return_statementdeclaration : INT ID ASSIGN NUMBER SEMICOLONassignment : ID ASSIGN expression SEMICOLONfor_statement : FOR LPAREN assignment condition SEMICOLON increment RPAREN LBRACE statements RBRACEcondition : ID LT NUMBER\n                     | ID LE NUMBER\n                     | ID GT NUMBER\n                     | ID GE NUMBER\n                     | ID EQ NUMBER\n                     | ID NE NUMBERincrement : ID PLUS PLUSreturn_statement : RETURN NUMBER SEMICOLONexpression : NUMBER\n                      | ID MULT_OP NUMBER\n                      | ID PLUS ID'
    
_lr_action_items = {'INCLUDE':([0,],[3,]),'$end':([1,4,24,],[0,-1,-3,]),'INT':([2,10,12,15,16,17,18,19,34,38,41,61,64,],[5,-2,13,13,-6,-7,-8,-9,-20,-11,-10,13,-12,]),'LT':([3,40,],[6,45,]),'MAIN':([5,],[7,]),'LIBRARY':([6,],[8,]),'LPAREN':([7,21,],[9,27,]),'GT':([8,40,],[10,47,]),'RPAREN':([9,51,62,],[11,59,-19,]),'LBRACE':([11,59,],[12,61,]),'ID':([12,13,15,16,17,18,19,26,27,33,34,37,38,41,44,61,64,],[20,23,20,-6,-7,-8,-9,30,20,40,-20,43,-11,-10,52,20,-12,]),'FOR':([12,15,16,17,18,19,34,38,41,61,64,],[21,21,-6,-7,-8,-9,-20,-11,-10,21,-12,]),'RETURN':([12,15,16,17,18,19,34,38,41,61,64,],[22,22,-6,-7,-8,-9,-20,-11,-10,22,-12,]),'RBRACE':([14,15,16,17,18,19,25,34,38,41,63,64,],[24,-4,-6,-7,-8,-9,-5,-20,-11,-10,64,-12,]),'ASSIGN':([20,23,],[26,29,]),'NUMBER':([22,26,29,36,45,46,47,48,49,50,],[28,32,35,42,53,54,55,56,57,58,]),'SEMICOLON':([28,31,32,35,39,42,43,53,54,55,56,57,58,],[34,38,-21,41,44,-22,-23,-13,-14,-15,-16,-17,-18,]),'MULT_OP':([30,],[36,]),'PLUS':([30,52,60,],[37,60,62,]),'LE':([40,],[46,]),'GE':([40,],[48,]),'EQ':([40,],[49,]),'NE':([40,],[50,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'include':([0,],[2,]),'function':([2,],[4,]),'statements':([12,15,61,],[14,25,63,]),'statement':([12,15,61,],[15,15,15,]),'declaration':([12,15,61,],[16,16,16,]),'assignment':([12,15,27,61,],[17,17,33,17,]),'for_statement':([12,15,61,],[18,18,18,]),'return_statement':([12,15,61,],[19,19,19,]),'expression':([26,],[31,]),'condition':([33,],[39,]),'increment':([44,],[51,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> include function','program',2,'p_program','analizador.py',78),
  ('include -> INCLUDE LT LIBRARY GT','include',4,'p_include','analizador.py',82),
  ('function -> INT MAIN LPAREN RPAREN LBRACE statements RBRACE','function',7,'p_function','analizador.py',86),
  ('statements -> statement','statements',1,'p_statements','analizador.py',90),
  ('statements -> statement statements','statements',2,'p_statements','analizador.py',91),
  ('statement -> declaration','statement',1,'p_statement','analizador.py',98),
  ('statement -> assignment','statement',1,'p_statement','analizador.py',99),
  ('statement -> for_statement','statement',1,'p_statement','analizador.py',100),
  ('statement -> return_statement','statement',1,'p_statement','analizador.py',101),
  ('declaration -> INT ID ASSIGN NUMBER SEMICOLON','declaration',5,'p_declaration','analizador.py',105),
  ('assignment -> ID ASSIGN expression SEMICOLON','assignment',4,'p_assignment','analizador.py',114),
  ('for_statement -> FOR LPAREN assignment condition SEMICOLON increment RPAREN LBRACE statements RBRACE','for_statement',10,'p_for_statement','analizador.py',120),
  ('condition -> ID LT NUMBER','condition',3,'p_condition','analizador.py',124),
  ('condition -> ID LE NUMBER','condition',3,'p_condition','analizador.py',125),
  ('condition -> ID GT NUMBER','condition',3,'p_condition','analizador.py',126),
  ('condition -> ID GE NUMBER','condition',3,'p_condition','analizador.py',127),
  ('condition -> ID EQ NUMBER','condition',3,'p_condition','analizador.py',128),
  ('condition -> ID NE NUMBER','condition',3,'p_condition','analizador.py',129),
  ('increment -> ID PLUS PLUS','increment',3,'p_increment','analizador.py',135),
  ('return_statement -> RETURN NUMBER SEMICOLON','return_statement',3,'p_return_statement','analizador.py',141),
  ('expression -> NUMBER','expression',1,'p_expression','analizador.py',145),
  ('expression -> ID MULT_OP NUMBER','expression',3,'p_expression','analizador.py',146),
  ('expression -> ID PLUS ID','expression',3,'p_expression','analizador.py',147),
]