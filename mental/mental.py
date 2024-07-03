# mental.py
# 
# A key idea in "computation" is the idea of breaking a calculation
# down to single steps.  It's kind of like "showing your work" in
# a math class from school.   For example, if you are asked
# to evaluate the following:
#
#     2 + (3+4)*(5+6) + 7
#
# You evaluate it by executing one step at a time:
#
#     2 + 7*(5+6) + 7
#     2 + 7*11 + 7
#     2 + 77 + 7
#     79 + 7
#     86
#
# This idea of "single steps" is at the heart of actual computers.
# CPUs have instructions that perform a single small computation.  For
# example, in the Metal exercise, you wrote small machine language
# programs to carry out calculations.  You had to convert the
# calculation steps to operations on hardware such as "ADD", "SUB",
# and so forth.
#
# This exercise puts a slightly different abstraction on the whole affair.
# We'll start by abstracting the idea of an "operation" to functions.
# Consider the following:

def ADD(x, y, next):
    return lambda: next(x+y)

def SUB(x, y, next):
    return lambda: next(x-y)

def MUL(x, y, next):
    return lambda: next(x*y)

def DIV(x, y, next):
    return lambda: next(x//y)

# These functions take two inputs and a function called "next"
# which receives the result of the calculation.  The return
# value is a zero-argument function that actually makes the
# computation run.
#
# It looks a bit strange, but in this context, "next" represents the
# the *next* step of the calculation.  It might be easier to visualize
# it as a dataflow
#            ________
#       x ->|        |
#           |  ADD   | -> next
#       y ->|________|
#
# The purpose of the lambda return is to delay the actual computation
# until the result is needed. 

# Here is an example of computing 2 + 3 and printing out the result.

result = ADD(2, 3, print)
result()   # --> Prints 5

# Here is an example of computing 2 * 3 + 4 as a sequence of steps

result = MUL(2, 3,
             lambda result: ADD(result, 4, print))
result()()   # --> Prints 10

# Ponder.... why are two sets of parentheses needed to get the final output?

# -----------------------------------------------------------------------------
# Exercise 1:
#
# Show how you would calculate and print the final value of the following
# math expression using only the above functions.
#
#    2 + 3 * 4 - 5


# -----------------------------------------------------------------------------
# Exercise 2:
#
# So, here's a weird thing... all of these functions actually create a
# kind of machine that can run through a step by step process.  Consider
# this mysterious fragment of code.

def run(next):
    while next:
        next = next()

# Try using run() on an earlier example
run(MUL(2, 3, lambda result: ADD(result, 4, print)))  # --> 10

# Now try using run() on your solution to Exercise 1.
# run(... exercise 1 code ...)

# -----------------------------------------------------------------------------
# Exercise 3:
#
# Suppose the following functions has been written to perform a comparison.

def EQ(x, y, next):
    return lambda: next(x == y)

def NE(x, y, next):
    return lambda: next(x != y)

def LT(x, y, next):
    return lambda: next(x < y)

def LE(x, y, next):
    return lambda: next(x <= y)

def GT(x, y, next):
    return lambda: next(x > y)

def GE(x, y, next):
    return lambda: next(x >= y)

def CBRANCH(test, consequence, alternative):
    # consequence and alternative should be zero-argument functions
    # that continue the calculation (could be created by above
    # functions in some way).
    if test:
        return consequence
    else:
        return alternative

# Using these functions, can you write a function MAX(a, b, next)
# that computes the maximum value of a and b, giving the result
# to next?

def MAX(a, b, next):
    ...
    
run(MAX(2, 3, print))        # Should print 3

# -----------------------------------------------------------------------------
# Exercise 4
#
# Suppose you wanted to sum the first n integers.  Here's a Python
# function that does it:
#
#    def sumn(n):
#        result = 0
#        while n > 0:
#            result = result + n
#            n -= 1
#        return result
#
# Can you encode this computation using some combination of the
# functions above?

def SUMN(n, next):
    ...

run(SUMN(10, print))       # prints 55
run(SUMN(1000000, print))  # prints 500000500000


