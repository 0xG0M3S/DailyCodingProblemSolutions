This problem was asked by Google.

The game of Nim is played as follows. Starting with **three heaps**, each containing a variable number of items, two players take turns removing one or more items from a single pile. The player who eventually is forced to take the last stone loses. For example, if the initial heap sizes are `3`, `4`, and `5`, a game could be played as shown below:

```
  A  |  B  |  C
-----------------
  3  |  4  |  5
  3  |  1  |  3
  3  |  1  |  3
  0  |  1  |  3
  0  |  1  |  0
  0  |  0  |  0 
```

In other words, to start, the first player takes three items from pile B. The second player responds by removing two stones from pile C. The game continues in this way until player one takes last stone and loses.

Given a list of non-zero starting values `[a, b, c]`, and assuming optimal play, determine whether the first player has a forced win.