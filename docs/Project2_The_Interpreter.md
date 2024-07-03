# Project 2 - The Interpreter

In this project, you will build a definitional interpreter that
directly executes [WabbitScript](WabbitScript.md) from the associated
data model.  Essentially you will be able to take all of the models
you defined in `script_models.py` and make them run in some way. The
purpose of this project is to understand how programs evaluate.

Go to the file `wabbit/interp.py` and follow the instructions inside.

## Extension to Functions

If you previously made models for [WabbitFunc](WabbitFunc.md), see
if you can make your interpreter execute user-defined functions.

This is likely to be significantly more difficult that the scripting
portion in the first part.  Functions require you to think in more
detail about environments, scoping rules, stack frames, and other
runtime details.  You may want to wait.

## Extension to Types

If you have functions working, try to give your interpreter for
the features of [WabbitType](WabbitType.md).

This is also likely to be difficult at first.  You may want to
wait until later stages of the project before attempting to
support user-defined types.





