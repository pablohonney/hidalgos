"""
String metrics are often times edit distance algorithms.

They compute how many edit operations should be performed to turn one string into the other.
There are a few edit operations. namely...
    insert a char
    delete a char
    replace a char with a new one (technically insert and delete at once)
    keep the char. (technically replace with the same char)
    swap 2 chars

    * when insert/delete have the same cost they are often referred to as indel

Edit distance algorithms are customized to work with different subsets of operations.
Each operation has a cost assigned to it.

Costs can be further tuned based on the input value. e.g. cost(a, b) may differ from cost(b, a)
This is done with char-2-char cost tables like this one for replace/keep operations.
  a b
a 0 3
b 2 0
"""


# string metrics
from .hamming import hamming_str
from .hamming import hamming_decimal
from .hamming import hamming_bits_and as hamming_bits
from .levenshtein import levenshtein_compressed_matrix as levenshtein
from .levenshtein import wagner_fischer_compressed_matrix as wagner_fischer
from .jaro import jaro

