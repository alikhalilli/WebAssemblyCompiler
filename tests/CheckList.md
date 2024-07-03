The tests are ordered in possible sequence of how you
might work on your implementation.   Here is a checklist
you can use to mark-off your progress.  If you mark
this as you work and check it in with your work, it will
help me know more about your progress.

Legend:
-------
T = Tokenize
P = Parse
C = Typecheck
I = Interpreter
R = IRCode
L = LLVM

Script/
-------
[ ] 00_intliteral.wb           Integer literals
[ ] 01_intbinop.wb             Integer binary operators
[ ] 02_intunaryop.wb           Integer unary operators
[ ] 03_intvar.wb               Integer variables/operators
[ ] 04_floatliteral.wb         Floating point literals
[ ] 05_floatbinop.wb           Float binary operators
[ ] 06_floatunaryop.wb         Float unary operators
[ ] 07_floatvar.wb             Float variables/operators
[ ] 08_intrel.wb               Integer relations
[ ] 09_floatrel.wb             Floating point relations
[ ] 10_bool.wb                 Boolean literals/operators
[ ] 11_cond.wb                 Conditionals (if-else)
[ ] 12_loop.wb                 While-loop
[ ] 13_charliteral.wb          Character literals
[ ] 14_charrel.wb              Character relations
[ ] 15_mandel.wb               Mandelbrot set example
[ ] 16_brk.wb                  break/continue in loops
[ ] 17_compound.wb             Compound expressions
[ ] 18_shortcircuit.wb         Short-circuit evaluation
[ ] Errors/19_error_script.wb  Errors in WabbitScript

Func/
-----
[ ] 20_square.wb               Simple function definition
[ ] 21_sqrt.wb                 More complex functions
[ ] 22_fib.wb                  Recursive functions
[ ] 23_mandel.wb               Mandelbrot example
[ ] 24_conversions.wb          Type conversions
[ ] Errors/25_error_func.wb    Errors in WabbitFunc

Type/
-----
[ ] 30_unit.wb                 Implementation of unit type
[ ] 31_struct.wb               Structure definitions
[ ] 32_nested.wb               Nested structures
[ ] 33_enum.wb                 Enumerations
[ ] 34_mandel.wb               Mandelbrot example
[ ] 35_error_type.wb           Errors in WabbitType
