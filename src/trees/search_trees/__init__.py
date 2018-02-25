"""
Search trees

Structural properties:
  search tree: left.key < parent.key < right.key

Here is an illustration with a binary tree

              10                      | depth/levels
     5                 15             |
  3      7        12        17        |
1  2   6  8     11  14    16   18    \/

Number of nodes doubles at each next level.
Summing up nodes in all levels gives the total count n.

n = 17
  = 1 + 2 + 4 + 8
  = 2**0 + 2**1 + 2**2 + 2**3
  = sum(2**i for i in range(4))

more generally...
n = sum(2**i for i in range(depth))
  = 2**(depth+1) - 1

thus

n ~ 2**(depth+1)
log(n) ~ depth + 1
depth ~ log(n)

Tree is searched starting from the root.
Each depth level corresponds to a comparison. Thus

time: O(log(n))

&

space: O(|V|+|E|)
trees are sparse graphs with |E| = |V| - 1

==============================

Implementation notes:

Technically speaking tree is more than a bunch of nodes.
It's an API wrapped around it.

When planting trees, I often face a dilemma.
Where should I put the dirty code?

- Fat tree + skinny nodes
- Skinny tree + fat nodes

I believe most of the time the latter is more appropriate.
Using different nodes for the root, branches and leaves we can get cleaner code
that will handle the edge cases through polymorphism, instead of using if-else
clauses in the tree.

Meanwhile tree itself is freed of heavy-weight duties and provides clear API.

Remember 'smart data structures and dumb code' principle?
"""
