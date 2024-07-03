# irrun.py
#
# Your challenge, should you choose to accept it, is to write a
# simulator that directly runs your IR Code as defined in the
# ircode.py file.

class IRMachine:
    pass       # You define
        
def main(filename):
    from .parse import parse_file
    from .typecheck import check_program
    from .ircode import generate_ircode
    from .transform import transform
    
    model = parse_file(filename)
    check_program(model)
    model = transform(model)
    irmodule = generate_ircode(model)

    # You'll have to adapt this as needed to make it work
    machine = IRMachine(irmodule)
    machine.run()

if __name__ == '__main__':
    import sys
    main(sys.argv[1])
    
