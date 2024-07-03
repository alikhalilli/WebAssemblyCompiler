# wabbit/llvm.py
#
# In this file you will have your compiler generate LLVM output.  Don't
# start this unless you have first worked through the LLVM Tutorial in
#
#     docs/LLVM-Tutorial.md
#
# Once you have done that, come back here.
#
# The overall strategy here is to take your IR and convert it to
# LLVM.  In theory, the two representations should be very similar
# to each other.  Your IRModule will become an LLVM module.
# IRFunctions will become LLVM functions.  Low-level instructions
# such as 'i32.add' will be converted to LLVM builder instructions
# such as 'builder.add'.

from llvmlite import ir

# Define LLVM types corresponding to IR types
i32_type = ir.IntType(32)
f64_type = ir.DoubleType()
i1_type = ir.IntType(1)
i8_type = ir.IntType(8)

# The LLVM module/environment that Wabbit is populating
class WabbitLLVMModule:
    pass

# Top-level function
def generate_llvm(irmodule):
    llmod = WabbitLLVMModule()
    convert_module(irmodule, llmod)
    return llmod

def convert_module(irmodule, llmod):
    # Convert an IRModule to an LLVM Module
    ...

# Sample main program that runs the compiler
def main(filename):
    from .parse import parse_file
    from .typecheck import check_program
    from .ircode import generate_ircode
    from .transform import transform
    
    model = parse_file(filename)
    check_program(model)
    model = transform(model)
    irmodule = generate_ircode(model)
    llmodule = generate_llvm(irmodule)
    
    with open('out.ll', 'w') as file:
        file.write(str(llmodule))
    print('Wrote out.ll')

if __name__ == '__main__':
    import sys
    main(sys.argv[1])



