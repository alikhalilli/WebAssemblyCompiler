# func_models.py
#
# The WabbitFunc language extends WabbitScript with support for
# user-defined functions.  This requires additional support
# for the following constructs:
#
#     1. Function definitions.
#     2. Function application.
#     3. The return statement.
# 
# This file contains a single example that you should represent
# using your model.  Please see the following document for more information.
#
#     docs/WabbitFunc.md

from wabbit.model import *

# ----------------------------------------------------------------------
# Program 8: Functions.  This program tests the basics of function
# calls and returns.

source8 = '''
func add(x int, y int) int {
    return x + y;
}
func main() int {
    var result = add(2, 3);
    print result;
    return 0;
}
'''

model8 = None

# print(to_source(model8))

# ----------------------------------------------------------------------
# Bring it!  If you're here wanting even more, proceed to the file 
# "type_models.py".
