# parse.py
#
# Wabbit parser.  The parser needs to construct the data model or an
# abstract syntax tree from text input.  The precise format of the
# text input is described by a grammar.  The grammar shown here
# represents WabbitScript--a subset of the full Wabbit language.  It's
# written as a PEG.  You will need to expand the grammar to include
# later features like functions and types.
#
# Reference: docs/WabbitScript.md
#
# The following conventions are used in the grammar:
# 
#       ALLCAPS       --> A token
#       { symbols }   --> Zero or more repetitions of symbols
#       [ symbols ]   --> Zero or *one* occurence of symbols (optional)
#       s / t         --> First match of s or t (check in order)
#       EOF           --> End of file 
#
# program : statements EOF        
# 
# statements : { statement }
#
# statement : print_statement
#           / assignment_statement
#           / variable_definition
#           / const_definition
#           / func_definition
#           / struct_definition
#           / enum_definition
#           / if_statement
#           / while_statement
#           / break_statement
#           / continue_statement
#           / return_statement
#           / expression SEMI
#
# print_statement : PRINT expression SEMI
#
# assignment_statement : location ASSIGN expression SEMI
#
# variable_definition : VAR NAME [ type ] [ ASSIGN expression ] SEMI
#
# const_definition : CONST NAME [ type ] ASSIGN expression SEMI
#
# func_definition : FUNC NAME LPAREN [ parameters ] RPAREN [ type ] LBRACE statements RBRACE
#
# struct_definition : STRUCT NAME LBRACE { struct_field } RBRACE
#
# struct_field : NAME type SEMI
#
# enum_definition : ENUM NAME LBRACE { enum_field } RBRACE
#
# enum_field : NAME [ LPAREN type RPAREN ] SEMI;
#
# if_statement : IF expression LBRACE statements RBRACE [ ELSE LBRACE statements RBRACE ]
#
# while_statement : WHILE expression LBRACE statements RBRACE
#
# break_statement : BREAK SEMI
#
# continue_statement : CONTINUE SEMI
#
# return_statement : RETURN expression SEMI
#
# ::::: Special discussion about expressions :::::
#
# Expression parsing is probably the most difficult part of writing the
# parser.  This is because expressions need to capture precedence
# rules.   For example, how is the following expression evaluated?
#
#           2 + 3 * 4 < 30 / 6 - 7
#
# There are essentially different parsing "levels".  For example, to
# evaluate this expression, multiplication and division get evaluated
# first:
#
#            2 + (3 * 4) < (30 / 6) - 7
#            2 + 12 < 5 - 7
#
# Addition and subtraction then go next:
#
#            (2 + 12) < (5 - 7)
#              14     <   -2
#
# The relation goes last, producing false in this example.
# To make this work, each level of precedence gets its own
# parsing rule.  The rules are listed from lowest precedence
# to highest precedence.
#
# Note: Wabbit does not allow chained relations. "a < b" is
# legal, but "a < b < c" is not.   That's why the "relation"
# rule below looks different than everything else.
#
# expression :  relation
#
# relation : sumterm [ LT/LE/GT/GE/EQ/NE sumterm ]         # <, <=, >, >=, ==, !=
#
# sumterm : multerm { PLUS/MINUS multerm }                 # +, -
#
# multerm : factor { TIMES/DIVIDE factor }                 # *, /
#
# factor  : PLUS factor
#         / MINUS factor
#         / LNOT factor
#         / literal
#         / LPAREN expression RPAREN
#         / NAME LPAREN [ arguments ] RPAREN
#         / NAME DCOLON NAME [ LPAREN expression RPAREN ]
#         / MATCH expression LBRACE { match_clause } RBRACE
#         / location
#       
# literal : INTEGER
#         / FLOAT
#         / CHAR
#         / TRUE
#         / FALSE
#         / LPAREN RPAREN
#
# arguments : expression { COMMA expression }
#
# match_clause : NAME [ LPAREN NAME RPAREN ] ARROW expression SEMI
#
# location : NAME
#
# type : NAME
# ======================================================================

# How to proceed:  
#
# At first glance, writing a parser might look daunting. The key is to
# take it in tiny pieces.  Focus on one specific part of the language.
# For example, the print statement.  Start with something really basic
# like printing literals:
#
#     print 1;
#
# Next, focus on how to parse multiple statements:
#
#     print 1;
#     print 2.5;
#
# Start adding some new features like variable and const declarations:
#
#     var x = 3;
#     const pi = 3.14159;
#     print x;
#     print pi;
#
# From there, expand it to handle expressions:
#
#     print 2 + 3 * -4;
#
# Keep on expanding to more and more features of the language.  Once
# you've started to fill in more pieces, try to parse the programs
# in the top-level script_models.py file.  Once you're able to
# parse all of those programs, you're well on your way.  Move
# onto the programs in tests/Script to test more features.
#

from .model import *
from .tokenize import tokenize

# Top-level function that runs everything    
def parse_source(text):
    tokens = tokenize(text)
    model = parse_tokens(tokens)     # You need to implement this part
    return model

def parse_tokens(tokens):
    ...

# Example of a main program
def parse_file(filename):
    with open(filename) as file:
        text = file.read()
    return parse_source(text)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        raise SystemExit('Usage: wabbit.parse filename')
    model = parse_file(sys.argv[1])
    print(model)


