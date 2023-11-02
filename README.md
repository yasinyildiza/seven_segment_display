# Seven Segment Display

This is a project just for fun to mimic [Seven-segment display]https://en.wikipedia.org/wiki/Seven-segment_display in the command line.

The project does not have any dependency, but requires 3.10+ due to type hints.

You can simply run it by:

`python3 -m seven_segment_display 1234.56`

```
1234.56
      ---   ---         ---   ---
  |     |     |   | |   |     |
      ---   ---   ---   ---   ---
  |   |       |     |     |   | |
      ---   ---       . ---   ---
```

You can also play with decimal precision via `-p` or `--precision` argument.


`python3 -m seven_segment_display 1234.56789 -p 3`

```
1234.568
      ---   ---         ---   ---   ---
  |     |     |   | |   |     |       |
      ---   ---   ---   ---   ---
  |   |       |     |     |   | |     |
      ---   ---       . ---   ---
```
