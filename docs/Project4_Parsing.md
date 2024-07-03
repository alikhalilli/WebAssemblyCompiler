# Project 4 - Parsing

In this project, we write a proper parser for
[WabbitScript](WabbitScript.md).  This will allow us to build data
models directly from source code as opposed to having to build them by
hand as we did in `script_models.py`.

Go to the file `wabbit/parse.py` and follow the instructions inside.

## Testing 

When you are done with this project, you should be able to run the
parser on programs in `tests/Script/` and see the resulting data
model.  Here is an example of what it might look like:

```
bash $ cat tests/Script/12_loop.wb
/* 12_loop.wb

   Test of a while-loop
*/

var n int = 1;
var value int = 1;

/* Prints out the first 10 factorials */
while n < 10 {
    value = value * n;
    print value ;
    n = n + 1;
}

bash $ python3 -m wabbit.parse tests/Script/12_loop.wb
[Variable(n, int, Integer(1)), Variable(value, int, Integer(1)), While(BinOp(<, Load(NamedLocation(n)),
 Integer(10)), [Assignment(NamedLocation(value), BinOp(*, Load(NamedLocation(value)), Load(NamedLocation(n)))), 
Print(Load(NamedLocation(value))), Assignment(NamedLocation(n), BinOp(+, Load(NamedLocation(n)), Integer(1)))])]
```

Again, your output might vary depending on how you defined your data
model.  Reading that is not always so easy. You might want to add some
debugging functions to make it easier to view.  For example, the
`to_source()` function in the `wabbit/model.py` file.


## How to Proceed

The programs in `tests/Script` are listed in a numerical order that
matchs steps/features that you might try to match with your parser.
One strategy is to start working on `tests/Script/00_intliteral.wb`
and to move to each program, one-by-one, until you can parse
every program.

## Interpretation

If you are feeling lucky, modify your `wabbit/interp.py` file so that
it can run programs. Have it read source code, parse it into a model,
and run it.  For example:

```
bash $ python3 -m wabbit.interp tests/Script/12_loop.wb
1
2
6
24
120
720
5040
40320
362880
bash $
```

If this works, you should be able to run all of the programs
in `tests/Script`.   Congratulations! You just wrote the
core of a scripting language--albeit a really slow one.

## Extension to Functions and Types

See if you can extend your parser to handle the features of
[WabbitFunc](WabbitFunc.md) and [WabbitType](WabbitType.md).  Some of
this might be quite difficult and not achievable at first.  When
starting out, it's fine to focus exclusively on WabbitScript.  You can
always come back to this later.




