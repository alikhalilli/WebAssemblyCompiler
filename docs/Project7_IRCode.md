# Project 7 - Intermediate Representation

A primary goal of a compiler is to translate a high level
language down to a lower-level language that runs on the hardware.
However, there are many different types of CPUs and hardware targets.
Instead of picking one, a common approach is to have the compiler
produce something known as Intermediate Representation (IR).
IR is like a generic machine language.  It's low level and
meant to be something that could be easily translated into
actual machine language for a particular CPU.

In this project, we're going to create a basic IR.  Time permitting,
we'll even write a small interpreter for running the IR.

See the file `wabbit/ircode.py` for further instructions.

## A Word on Functions

Supporting functions in your IR will require some thought about
the overall packaging of the final code.  You'll need to
create a module.  Within that module, you'll need to have
multiple functions.   You'll need to figure out some way for
functions to call each other.   There are a lot of fiddly bits
that you'll need to resolve.

## A Word on Types

To support user-defined types, you'll need to think about
the low-level representation of struct and enum objects.  This
may require you to add instructions for memory access and
possibly memory allocation.   This is likely to be non-trivial.
Only word on this if you think you have everything else working.
