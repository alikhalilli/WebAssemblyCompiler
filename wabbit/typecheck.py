# typecheck.py
#
# Type Checking
# =============
#
# This file implements type checking.  But first, what is type-checking?
# In the file interp.py, you wrote an interpreter that actually executed
# Wabbit code.  A type-checker, in some sense, is one step removed
# from that.  Instead of literally executing a program, a checker looks at a
# program and determines what it would do *if* it actually executed.  As
# an example, suppose you had an arithmetic expression like this:
#
#      2 + 3
#
# Instead of literally performing that calculation, a type checker would
# view the expression as an operation like this:
#
#      int + int
#
# It would then conclude that the result of the calculation has type "int".
# A type checker tries to discover errors.  For example, if it encountered
# a fragment of code like this:
#
#      2 + true
#
# It would look at the underlying types and see:
#
#      int + bool
#
# Because the types of the left and right operands don't match up,
# an error would be reported.
#
# A critical part of type-checking concerns the notion of "types"
# themselves.  Wabbit uses what's known as "nominal typing."  That
# means that types are given unique names such as "int", "float",
# "bool", etc. Two types are the same if they have exactly the same
# name.  That's it.
#
# In implementing the type checker, the best starting strategy might
# be to not overthink the problem at hand. Basically, you have type
# names.  You can represent these names using Python strings and
# compare them using string comparison. This gives you most of what
# you need for nominal typing.
#
# A secondary problem concerns knowing the capabilities of different
# operators.  For example, if you're implementing a binary operator like
# "+", you need to know what combinations of types are allowed and
# the ensuing result type.  You might be able to encode much of this
# in lookup tables.
#
# The directory tests/Errors has Wabbit programs with various errors.

from .model import *

# Top-level function used to check programs
def check_program(model):
    env = { }
    check(model, env)
    # Maybe return True/False if there are errors

# Internal function used to check nodes with an environment.  Critical
# point: Everything is focused on types.  The result of an expression
# is a type.  The inputs to different operations are types.

def check(node, env):
    if isinstance(node, Integer):
        return "int"
    ...
    raise RuntimeError(f"Couldn't check {node}")

# Sample main program
def main(filename):
    from .parse import parse_file
    model = parse_file(filename)
    check_program(model)

if __name__ == '__main__':
    import sys
    main(sys.argv[1])



        


        
