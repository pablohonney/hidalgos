### Variable width encoding


Data is stored internally through bit combinations.
To avoid uncertainty these combinations should be unique to each symbol.

Example. encode AAAAABCD

First let's choose an encoding size.

 - 1 bit has capacity to represent to symbols
 - 2 bits = 2^2 = 4 capacity
 - 3 bits = 2^3 = 8 capacity
 
Since we have three symbols, 2 bits will be sufficient.

we make an encoding set
    A - 00
    B - 01
    C - 10
    D - 11

which results in:
    00 00 00 00 00 01 10 11
    8*2 = 16 bits overall
    
Can we do better? What if more frequently used letters are encoded with shorter combinations?

our new variable size encoding set.
    A - 0
    B - 01
    C - 10
    C - 11
    
And we end up with:
    0 0 0 0 0 01 10 11
    11 bits


Nice, so don't we use variable size encoding everywhere?
Well let's try to decode our output.

Make a reversed table:
    0  - A
    01 - B
    10 - C
    11 - D
    
    0 0 0 0 0 0 1 1 0 1 0
    A A A A A   B   C   D  correct
    A A A A A A   D   B A  wrong
    
We got ambiguity. Whats the problem?
0 for A happens to be a prefix to 01 for B.

to be continued ...