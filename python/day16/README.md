# Day 16

Wow there are a lot of files in here, let's describe them for posterity.

* Day16p1-og.py is the original part 1 solution I worte that prints out intermediate steps
* Day16p2-attempt.py is an attempt to keep track of the path we took to reduce backtracking and minimize the search space, unformatunately it doesn't work and doesn't allow enough caching
* Day16p2-attempt2.py attempts to solve the problem by simplifying the graph, it should maybe work one day but I can't figure out what's wrong
* Day16.py is the first working solution I had after watching [Neil Thistlethwaite's solution on YouTube](https://www.youtube.com/watch?v=SAk5yyua8L4). I already had all the building blocks at the time so it made the most sense.
* Day16-chain.py is an additional solution written afterwards based on [this reddit comment](https://www.reddit.com/r/adventofcode/comments/zn6k1l/2022_day_16_solutions/j0fpyu4/)
* Day16-chain2.py combines the implementation of Day16-chain.py with simplified graph of Day16.py to achieve a speed increase