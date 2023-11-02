# Seven Segment Display

This is a project just for fun to mimic [Seven-segment display]https://en.wikipedia.org/wiki/Seven-segment_display in the command line.

The project requires Python 3.11+, and has no other dependency. It could work with older Python version if `typing.Self` was not used.

You can simply run it by:

`python3.11 -m seven_segment_display 1234.56`

```
1234.56
      ---   ---         ---   ---
  |     |     |   | |   |     |
      ---   ---   ---   ---   ---
  |   |       |     |     |   | |
      ---   ---       . ---   ---
```

You can also play with decimal precision via `-p` or `--precision` argument.


`python3.11 -m seven_segment_display 1234.56789 -p 3`

```
1234.568
      ---   ---         ---   ---   ---
  |     |     |   | |   |     |       |
      ---   ---   ---   ---   ---
  |   |       |     |     |   | |     |
      ---   ---       . ---   ---
```
