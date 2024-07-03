# Project 1 - The Model

To start the compiler project, we're going to focus on the problem of
representing programs as a proper data structure.  The focus of this
project starts with the [WabbitScript](WabbitScript.md) subset of the
Wabbit language.

## Setup

In the top-level directory, you will find the file `script_models.py`
as well as the `wabbit/` directory.  This is where you will be doing
most of your work.  However, please make sure you are working in your
own GitHub branch:

```
bash $ git checkout -b yourname
bash $ git push origin -u yourname
```

## High-level overview

The input to a compiler is a text-file sometimes referred to as the
"source."  However, a compiler doesn't like to work with your program
as text.  Instead, it builds a proper data structure representing the
contents and structure of the program.  Typically, this is a tree-like
structure known as an "Abstract Syntax Tree".  We're simply going to
call it the "model".  Programs don't necessarily have to originate
with text files--they could be constructed graphically (i.e.,
block-based programming) or generated algorithmically.  Hence, the
"model" terminology is perhaps a bit more generic.

## Extension to Functions

The file `func_models.py` extends WabbitScript with support for
functions as described in [WabbitFunc](WabbitFunc.md).  Take a look at
it and try to create data structures for representing function
definitions and function calls.

If you're feeling overwhelmed with work from WabbitScript, it's fine
to wait on functions until later.

## Extension to Types

The file `type_models.py` extends WabbitFunc with further support
for structures and enums as described in [WabbitType](WabbitType.md).
This is by far the hardest part of the project.  Give it a go
if you're feeling up to it, but it's fine to wait until later
(or to avoid it entirely depending on how much work you have to do
for other parts).
