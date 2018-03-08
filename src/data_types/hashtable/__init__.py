"""
Hash collisions can be solved in two ways.
  1. open hashing aka chaining
     easier to implement. breaks the O(n) guaranty
  2. closed hashing aka rehashing
     2.1 linear probing
     2.2 quadratic probing
     2.3 double hashing

When rehashing we get a rehash path that needs to be walked each time
the key is looked for.

Removing elements may leave gaps in these rehash paths. consider this:

array of size 3, e is empty, <> is the checked index
hashing is modulus, rehashing is linear probing,

put 1      -hash> [<e>, e, e] -put> [1, e, e]
put 4      -hash> [<1>, e, e] -rehash> [1, <e>, e] -put> [1, 4, e]
get 4      -hash> [<1>, 4, e] -rehash> [1, <4>, e] -get> 4
remove 1   -hash> [<1>, 4, e] -remove> [e, 4, e]
get 4      -hash> [<e>, 4, e] -error> couldn't find

solutions?
1: rehash all values on remove. bad.
2: rehash round robin on get/put/remove. bad.
3: damn, any ideas ?  Gotcha. use chaining for a while.

------------------------------------

Base hash-table class with polymorphic closed rehashing

write a custom hash function. should support salting !

Imitate sparse_index/dense_entry solution
"""

# resolve collisions with rehashing
from .rehashed_hashtable import RehashedHashTable

# resolve collisions with chaining
from .chained_hashtable import ChainedHashTable
