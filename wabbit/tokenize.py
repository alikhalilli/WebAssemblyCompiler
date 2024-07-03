# tokenizer.py
#
# The role of a tokenizer is to turn raw text into symbols known as
# tokens.  A token consists of a type and a value.  For example, the
# text "123" is represented as the token ('INTEGER', '123').
#
# The following set of tokens are defined for "WabbitScript".  Later
# parts of the project require you to add more tokens.  The suggested
# name of the token is on the left. An example of matching text is on
# the right.
#
# Reserved Keywords:
#     CONST   : 'const'
#     VAR     : 'var'  
#     PRINT   : 'print'
#     BREAK   : 'break'
#     CONTINUE: 'continue'
#     IF      : 'if'
#     ELSE    : 'else'
#     WHILE   : 'while'
#     FUNC    : 'func'
#     RETURN  : 'return'
#     STRUCT  : 'struct'
#     ENUM    : 'enum'
#     MATCH   : 'match'
#     TRUE    : 'true'
#     FALSE   : 'false'
#
# Identifiers/Names
#     NAME    : Text starting with a letter or '_', followed by any number
#               number of letters, digits, or underscores.
#               Examples:  'abc' 'ABC' 'abc123' '_abc' 'a_b_c'
#
# Literals:
#     INTEGER :  123   (decimal)
#
#     FLOAT   : 1.234
#               .1234
#               1234.
#
#     CHAR    : 'a'     (a single character - byte)
#               '\n'    (newline)
#
# Operators:
#     PLUS     : '+'
#     MINUS    : '-'
#     TIMES    : '*'
#     DIVIDE   : '/'
#     LT       : '<'
#     LE       : '<='
#     GT       : '>'
#     GE       : '>='
#     EQ       : '=='
#     NE       : '!='
#     LAND     : '&&'     (logical and, not bitwise)
#     LOR      : '||'     (logical or, not bitwise)
#     LNOT     : '!'      (logical not, not bitwise)
#    
# Miscellaneous Symbols
#     ASSIGN   : '='
#     SEMI     : ';'
#     LPAREN   : '('
#     RPAREN   : ')'
#     LBRACE   : '{'
#     RBRACE   : '}'
#     DOT      : '.'
#     COMMA    : ','
#     DCOLON   : '::'
#     ARROW    : '=>'
#
# Comments:  To be ignored
#      //             Skips the rest of the line
#      /* ... */      Skips a block (no nesting allowed)
#
# Errors: Your lexer may optionally recognize and report errors
# related to bad characters, unterminated comments, and other problems.
# ----------------------------------------------------------------------

# Class that represents a token
class Token:
    def __init__(self, type, value, lineno):
        self.type = type
        self.value = value
        self.lineno = lineno

    def __repr__(self):
        return f'Token({self.type!r}, {self.value!r}, {self.lineno})'

# High level function that takes input source text and turns it into
# tokens.  This might be a natural place to use some kind of generator
# function or iterator.

def tokenize(text):
    ...
    yield tok
    ...

# Main program to test on input files
def main(filename):
    with open(filename) as file:
        text = file.read()

    for tok in tokenize(text):
        print(tok)

if __name__ == '__main__':
    import sys
    main(sys.argv[1])

    
            
        

            
    
