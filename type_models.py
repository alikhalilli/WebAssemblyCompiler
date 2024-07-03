# type_models.py
#
# The WabbitType language extends WabbitScript with support for
# user-defined types including structures, enums, and matching.
# Support for types is the most difficult part of the project.
# See:
#
#     docs/WabbitType.md
#
# You might start working on this and decide to come back to it
# later (or not at all).

from wabbit.model import *

# -----------------------------------------------------------------------------
# Program 9: Structures.  The following program defines and uses a structure.
#
# You'll need to support structure definition, creation, and usage with other
# parts of your language such as functions.

source9 = '''
struct Fraction {
   numerator int;
   denominator int;
}

func frac_mul(a Fraction, b Fraction) Fraction {
    return Fraction(a.numerator * b.numerator, a.denominator * b.denominator);
}

var x = Fraction(1, 2);
var y = frac_mul(x, x);
y.numerator = -y.numerator;
print y.numerator;
print y.denominator;
'''

model9 = None

# -----------------------------------------------------------------------------
# Program 10: Enums.  The following program defines and uses an enum.
#
# To this, you'll need to support the enum definition, enum values,
# and pattern matching with match.  You will also need to have type
# conversions (int(), float()) as well as compound expressions.

source10 = '''
enum Number {
    Integer(int);
    Float(float);
}

func add(a Number, b Number) Number {
   return match(a) {
             Integer(x) => match(b) {
                   Integer(y) => Number::Integer(x + y);
                   Float(y) => Number::Float(float(x) + y);
             };
             Float(x) => match(b) {
                   Integer(y) => Number::Float(x + float(x));
                   Float(y) => Number::Float(x + y);
             };
   };
}

var a = Number::Integer(42);
var b = Number::Float(3.7);
var c = add(a, b);

match(c) {
    Integer(x) => { print x; };
    Float(x) => { print x; };
};
'''

model10 = None
