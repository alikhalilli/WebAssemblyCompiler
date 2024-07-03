# wasm.py
#
# Generate WebAssembly from the Wabbit model.  Don't even attempt this
# unless you have first worked through the WebAssembly tutorial.
#
#     docs/WebAssembly-Tutorial.md
#
# The overall strategy here is to take your IR and convert it to
# Wasm.  There should be many similarities in types and features.
# However, one challenge concerns the Wasm use of a stack
# machine.  If your IRCode is using registers, you will need to
# figure out some way to translate that to a stack.

from .model import *

# Class representing the world of Wasm
class WabbitWasmModule:
    pass

# Top-level function for generating code from the model
def generate_wasm(irmodule):
    wasmmod = WabbitWasmModule()
    convert_module(irmodule, wasmmod)
    return wasmmod

# Internal function for generating code on each node
def convert_module(irmodule, wasmmod):
    raise RuntimeError(f"Can't generate {node}")

def main(filename):
    from .parse import parse_file
    from .typecheck import check_program
    from .ircode import generate_ircode
    from .transform import transform
    
    model = parse_file(filename)
    check_program(model)
    model = transform(model)
    irmodule = generate_ircode(model)
    wasmmodule = generate_wasm(irmodule)
    
    with open('out.wasm', 'wb') as file:
        file.write(encode_module(wasmmodule))
    print('Wrote out.wasm')

if __name__ == '__main__':
    import sys
    main(sys.argv[1])

        
        

    

                   
