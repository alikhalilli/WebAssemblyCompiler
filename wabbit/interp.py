# interp.py
#
# In order to write a compiler for a programming language, it helps to
# have some kind of specification of how programs written in the
# programming language are actually supposed to work. A language is
# more than just "syntax" or a data model.  There has to be some kind
# of operational semantics that describe what happens when a program
# in the language executes.
#
# One way to specify the operational semantics is to write a so-called
# "definitional interpreter" that directly executes the data
# model. This might seem like cheating--after all, our final goal is
# not to write an interpreter, but a compiler. However, if you can't
# write an interpreter, chances are you can't write a compiler either.
# So, the purpose of doing this is to pin down details as well as build
# our overall understanding of what needs to happen when programs run.
#
# The idea of writing an interpreter is somewhat straightforward.
# For each class in the model.py file, you're going to write a
# function similar to this:
#
#    def interpret_node_name(node, env):
#        # Execute "node" in the environment "env"
#        ...
#        return result
#   
# The input to the function will be an object from model.py (node)
# along with an object respresenting the contents of the execution
# environment (env).  The function will then execute the node in the
# environment and return a result.  It might also modify the
# environment (for example, when executing assignment statements,
# variable definitions, etc.).
#
# For the purposes of this project, assume that all programs provided
# as input are "sound"--meaning that there are no programming errors
# in the input. Our purpose is not to create a "production grade"
# interpreter.  We're just trying to understand how things actually
# work when a correct program runs.
#
# For testing, try running your interpreter on the models you
# created in the script_models.py file.   Verify that their output
# is what you expect it to be.  Move on to func_models.py and
# type_models.py to test programs involving functions and types.
#

from .model import *

# Top level function that interprets an entire program. It creates the
# initial environment that's used for storing variables.

def interpret_program(model):
    # Make the initial environment (a dict).  The environment is
    # where you will create and store variables.
    env = { }
    return interpret(model, env)

# Internal function to interpret a node in the environment.  You need
# to expand to cover all of the classes in the model.py file. 

def interpret(node, env):
    # Expand to check for different node types
    if isinstance(node, Integer):
        return interpret_integer(node, env)

    elif isinstance(node, PrintStatement):
        return interpret_print_statement(node, env)

    else:
        raise RuntimeError(f"Can't interpret {node}")

# Each node in the model should have some function.  This
# function should carry out the expected operation for that node.
def interpret_integer(node, env):
    return int(node.value)
    
def interpret_print_statement(node, env):
    value = interpret(node.value, env)
    print(value)
                             
                             

        
        
        
