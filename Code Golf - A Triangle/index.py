"""Task
Given three sides a, b and c, determine if a triangle can be built out of them.

Code limit
Your code can be up to 40 characters long.

Note
Degenerate triangles are not valid in this kata.
"""

def triangle(*a):return 2*max(a)<sum(a)

