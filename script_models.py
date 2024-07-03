# script_models.py
#
# Within the bowels of your compiler, you need to represent programs
# as a data structure.  Sometimes this is known as an "Abstract Syntax
# Tree" or AST.  In this file, you will manually encode some simple
# Wabbit programs using the data model you're creating in the file
# wabbit/model.py
#
# The purpose of this is two-fold:
#
#   1. Make sure you fully understand the internal data structures
#      used by the compiler. You will need this to do everything else.
#
#   2. Have some program structures that you can use for later testing,
#      debugging, and experimentation.
#
# This file is broken into sections. Follow the instructions for
# each part.  Parts of this file might be referenced in later
# parts of the project.  Plan to have a lot of discussion.
#
# Note: This file only includes examples for WabbitScript which is
# a subset of the Wabbit language. See
#
#     docs/WabbitScript.md
#
# Also, these examples don't cover every possible language feature.
# More exhaustive testing becomes easier once you have the parser
# working.

from wabbit.model import *

# ----------------------------------------------------------------------
# A simple Expression
#
# This one is given to you as an example. You might need to adapt it
# according to the names/classes you defined in wabbit.model

expr_source = "2 + 3 * 4;"

expr_model  = BinOp('+', Integer('2'),
                         BinOp('*', Integer('3'), Integer('4')))

# Can you turn it back into source code?  Note: the to_source()
# function is found in wabbit/model.py.

# Uncomment:
# print(to_source(expr_model))

# ----------------------------------------------------------------------
# Program 1: Printing
#
# Encode the following program which tests printing and evaluates some
# simple expressions using Wabbit's core math operators.
#

source1 = """
    print 2 + 3 * -4;
    print 2.0 - 3.0 / -4.0;
"""

model1 = None

#print(to_source(model1))

# ----------------------------------------------------------------------
# Program 2: Variable and constant declarations. 
#            Expressions and assignment.
#
# Encode the following statements.

source2 = """
    const pi = 3.14159;  
    var tau float;
    tau = 2.0 * pi;
    print -tau + 10.0;
"""

model2 = None

#print(to_source(model2))

# ----------------------------------------------------------------------
# Program 3: Relations.  Values have the concept of equality and relations.

source3 = '''
    // Each statement below prints "true"
    print 1 == 1;
    print 0 < 1;         
    print 1 > 0;
'''

model3 = None

# print(to_source(model3))

# ----------------------------------------------------------------------
# Program 4: Conditionals.  This program prints out the minimum
# value of two variables.
#
source4 = '''
    var a int = 2;
    var b int = 3;
    if a < b {
        print a;
    } else {
        print b;
    }
'''

model4 = None

# print(to_source(model4))

# ----------------------------------------------------------------------
# Program 5: Loops.  This program prints out the first 10 factorials.

source5 = '''
    const n = 10;
    var x int = 1;
    var fact int = 1;

    while x < n {
        fact = fact * x;
        x = x + 1;
        print fact;
    }
'''

model5 = None
# print(to_source(model5))

# -----------------------------------------------------------------------------
# Program 6: Break/continue.  This program changes loop control flow

source6 = '''
    var n = 0;
    while true {
        if n == 2 {
            break;
        }
        n = n + 1;
        if n == 1 {
            continue;
        }
        print n;
    }
'''
model6 = None
# print(to_source(model6))

# ----------------------------------------------------------------------
# Program 7: Compound Expressions.  This program swaps the values of
# two variables using a single expression.
#
# A compound expression is a series of statements/expressions enclosed
# in { ... }.  The value of a compound expression is the value represented
# by the last operation. 

source7 = '''
    var x = 37;
    var y = 42;
    x = { var t = y; y = x; t; };  // Compound expression (value is "t")
    print x;
    print y;
'''

model7 = None
# print(to_source(model7))


# ----------------------------------------------------------------------
# What's next?  If you've made it here are are looking for more,
# proceed to the file "func_models.py" and continue.

