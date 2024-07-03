# ircode.py
#
# Ultimately, the goal of a compiler to create an "executable program"
# consisting of low-level instructions that run on actual hardware.
# However, the details of real CPUs are messy. Thus, rather than
# directly going there, it is more common to have the compiler target
# an abstract machine that emulates a generic CPU.  The instructions
# for this abstract machine form what is known as "Intermediate
# Representation" or "IR" for short.  IR is meant to be simpler than
# an actual CPU, but not so far removed that it can't be translated
# into actual machine instructions.  In fact, we'll do that in later
# step.
#
# IR has a few important parts to it which are outlined below:
#
# 1.  Datatypes and data representation. 
#
# Real CPUs usually only perform computation on integers and floating
# point numbers.  These datatypes come in variety of sizes (32-bit,
# 64-bit, 16-bit, etc.).  Integers may also come in both signed and
# unsigned varieties.  As part of your IR, you need to give these
# types names.  I suggest the following naming scheme:
#
#         i1     : 1-bit integer (boolean)
#         i8     : 8-bit integer (char/bytes)
#         i32    : 32-bit integer (int)
#         f64    : 64-bit float (float)
#
# Potentially you could have many more variants of these types in your IR.
# For example:
#
#         u32    : Unsigned 32-bit integer
#         f32    : 32-bit single precision float
#         i64    : 64-bit integer
#         ...
#
# 2. Operators
#
# Your IR needs to provide basic mathematical operators that mimic the
# operations found on an actual CPU.  Moreover, these operators need
# to account for different datatypes as listed in part (1).  Thus,
# have instructions incorporate both a type and an operation like this:
#
#        i32.add          # Integer addition (32 bit)
#        i32.sub          # Integer subtraction (32 bit)
#        i32.mul          # Integer multiplication (32 bit)
#        i32.div          # Integer division (32 bit)
#        f64.add          # Floating point addition (64 bit)
#        f64.sub          ...
#        f64.mul
#        f64.div
#
# Keep in mind that IR is something of your own creation.  If you feel
# like you need to make up an instruction for some operation, go for it.
#
# 3. Computational Model
#
# The IR needs to have some kind of underlying computational model.
# It could be based on register machine.   With a register machine,
# all operations involve named input and output registers.
# For example, to compute "2 + 3 * 4", the following instructions
# might be generated:
#
#        ('i32.const', 2, 'r1')               # r1 = 2
#        ('i32.const', 3, 'r2')               # r2 = 3
#        ('i32.const', 4, 'r3')               # r3 = 4
#        ('i32.mul', 'r2', 'r3', 'r4')        # r4 = r2 * r3  (12)
#        ('i32.add', 'r1', 'r4', 'r5')        # r5 = r1 + r4  (14)
#
# Alternatively, you might base your IR on a stack.  Here's what
# "2 + 3 * 4" might look like with a stack machine:
#
#        ('i32.push', 2)           # stack = [ 2 ]
#        ('i32.push', 3)           # stack = [ 2, 3 ]
#        ('i32.push', 4)           # stack = [ 2, 3, 4 ]
#        ('i32.mul',)              # stack = [ 2, 12 ]
#        ('i32.add',)              # stack = [ 14 ]
#
# 4. Memory and variables
#
# The IR needs to have a model for working with variables and memory.
# In Wabbit, variables are declared using a declaration such as:
#
#       var x int;
#
# Variables can exist in two different environments.  Global variables
# are defined outside of any function definition and are visible
# everywhere.  Local variables are defined inside a function definition
# and are only visible inside the function.  Locals are also ephemeral
# meaning that they disappear after a function has returned.
#
#       const pi = 3.14159;         // Global variable
#
#       func area(r float) float {  // Local variable "r"
#           var a = pi * r * r;     // Local variable "a"
#           return a;
#       }
#
# To manage variables, you'll need to organize your IR into objects
# that are able to represent the runtime environment. Define an
# IRFunction class that holds information that's local to a specific
# function (your class will need have more than this--this is just the
# start of it):
#
#       class IRFunction:
#           def __init__(self, name):
#               self.name = name
#               self.locals = [ ]
#
#           def alloc_local(self, name, type):
#               self.locals.append((name, type))
#               return len(self.locals) - 1
#
# With the IRFunction, define a method such as alloc_local() that
# creates a local variable and returns its slot within an internal
# locals table.
#
# Define an IRModule class that holds information about the global
# environment.  Give it a similar alloc_global() method.
#
#       class IRModule:
#           def __init__(self):
#               self.globals = [ ]
#
#           def alloc_global(self, name, type):
#               self.globals.append((name, type)
#               return len(self.globals) - 1
#
# Whenever you encounter a variable declaration such as "var x" or
# "const y", you'll execute an appropriate alloc_local() or
# alloc_global() method depending on where the variable lives.
#
# To access the contents of a variable, provide "load" and "store"
# instructions.  For example, for a register machine:
#
#        ('local.load', slot, 'rn')       # rn is a target register name
#        ('local.store', 'rn', slot)      # rn is a source register name
#        ('global.load', slot, 'rn')
#        ('global.store', 'rn', slot)
#
# These instructions take a "slot" number that corresponds to a given local
# or global variable as represented by the number returned by alloc_local()
# or alloc_global() above.
#
# Your IR code might also have more generic "load" or "store" operations
# to access to arbitrary memory locations or to dereference pointers.
# You won't need anything like that to start however.
#
# 5. Control Flow
#
# The IR needs to be able to model control flow.  This can be done using
# labels, gotos, and conditional branches.  
#
#        ('label', 'name')                     # Declare a jump label
#        ('goto', 'name')                      # Unconditional jump to a label
#        ('br_if', 'test', 'label1', 'label2') # Conditional branch
#
# The 'label' instruction doesn't perform any computation. It's merely
# a marker that identifies the destination of a jump or branch.
#
# 6. Runtime
#
# Certain operations such as printing involve access to a runtime
# library. Runtime functions are often written in a different language,
# that's external to the compiler.   You could support this by
# providing some kind of "call" instruction:
#
#       ('call_ext', 'funcname', [args], 'rn') # Call external function
#
# For example, a statement such as "print 42" might become this:
#
#       ('i32.const', 42, 'r1')
#       ('call_ext', '_printi', ['r1'], 'r2')
#
# 7. Initialization Function and main()
#
# All programs run within an global environment. This environment
# often contains global variables and other "scripting" type
# statements that carry out calculations.   All of this code
# should be placed into a function called "_init()" or something
# similar.   Just as an example, if you had the following Wabbit
# program:
#
#       const pi = 3.14159;
#       print 2.0*pi;
#       
# This program such be translated into something like this:
#
#    var pi float;    // Global declaration
#
#    func _init() int {
#        pi = 3.14159;
#        print 2.0*pi;
#        return 0;
#    }
#
#    // main() - entry point.  Generated automatically.
#    func main() int {
#        _init();
#        return 0;
#    }
# 
# Programs always start in a function main().  If none is provided
# by the program, create one as shown above.  If the user provides
# their own main(), insert a call to _init() into it as the first
# step.
#
# YOUR TASK
# =========
# Your task is to pull all of this together and to create an IR for
# Wabbit.  Once you have done that, you need to write code that
# translates Wabbit to IR.   The final product should be some kind
# of "IRModule" object that contains a collection of globals,
# functions, and other objects represent the result of compilation.
#
# If you're feeling up to it, go to the file irrun.py and write
# an interpreter for your IR Code.
#
# -----------------------------------------------------------------------------

from .model import *

# Mapping of Wabbit types to IR datatypes
typemap = {
    'int': 'i32',
    'float': 'f64',
    'char': 'i8',
    'bool': 'i1',
    }

# IRModule is a container for everything that gets created
class IRModule:
    def __init__(self):
        # Global variables.  Should record names and types
        self.globals = [ ]

        # Function table (contains IRFunction objects)
        self.functions = [ ]
        
    def alloc_global(self, name, type):
        # Allocate a new global variable
        self.globals.append((name, type))
        return len(self.globals) - 1

    def new_function(self, name, argtypes, rettype):
        # Create a new function 
        func = IRFunction(self, name, argtypes, rettype, len(self.functions))
        self.functions.append(func)
        return func

    def dump(self):
        # Debugging function to show module contents
        print(":::: Module")
        print(":::: Globals")
        for n, glob in self.globals:
            print(f"     {n}: {glob}")
        print(":::: Functions")
        for func in self.functions:
            func.dump()

# IRFunction holds all of the generated code for a function            
class IRFunction:
    def __init__(self, module, name, argtypes, rettype, index):
        self.module = module
        self.name = name
        self.argtypes = argtypes
        self.rettype = rettype
        self.index = index

        # Local variables.  Should record names and types
        self.locals = [ ]

        # Generated code
        self.code = [ ]

    def append(self, instruction):
        # Add a new instruction to the function
        self.code.append(instruction)

    def alloc_local(self, name, type):
        # Define a new local variable
        self.locals.append((name, type))
        return len(self.locals) - 1
    
    def dump(self):
        # Debugging function to dump function information
        print(f":::: FUNCTION {self.name} {self.argtypes} {self.rettype}")
        print(f":::: LOCALS:")
        for n, loc in enumerate(self.locals):
            print(f'    {n}: {loc}')
        print(":::: CODE:")
        for instr in self.code:
            print("    ", instr)

# IRContext holds information needed to generate code.  This
# includes information about the current module, function,
# and environment.  The environment is used to track variable
# names much like the interpreter and type-checker projects.

class IRContext:
    def __init__(self, module):
        self.module = module
        self.current = self.module.new_function('_init', [], 'i32')
        self.env = ChainMap()
        self.n = 0

    def new_label(self):
        self.n += 1
        return f'L{self.n}'

    def append(self, instruction):
        # Append a new instruction to the current instruction
        self.current.append(instruction)

# Top level function for generating IR from the model.
def generate_ircode(model):
    module = IRModule()
    context = IRContext(module)
    generate(model, context)

    # Note: You might have to terminate the _init function
    context.append(('i32.const', 0))
    context.append(('ret',))

    # You might have to create a main() function if none exists.
    ...
    
    # Return the final IRModule.  It will contain all of the generated code.
    return module

# Internal function for creating instructions
def generate(node, context):
    if isinstance(node, Integer):
        context.current.append(('i32.const', int(node.value)))

    elif isinstance(node, Float):
        context.current.append(('f64.const', float(node.value)))

    # ... more nodes follow

    else:
        RuntimeError(f"Can't generate code for {node}")
