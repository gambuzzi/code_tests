# Medium Questions

## 20 Linked Lists

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

### Solution

Ok, we can reason on node pointer and not node values, because of the phrase "In this example, assume nodes with the same value are the exact same node objects."

So is a metter of pointers.

* compute the difference of length of the 2 lists => `n`
* skip the first `n` nodes of the longest list
* now, keep 2 pointers and update them with the `.next` until they are not the same (or a list ends).
* we are on top of the common node (or `null`).

```python
def ll_len(linked_list):
    ret = 0
    ptr = linked_list
    while ptr:
        ret += 1
        ptr = ptr.next
    return ret

def common_node(A, B):
    la = len(A)
    lb = len(B)

    if la > lb:  # in this way B will always be the longest linked list
        A, B = B, A

    for _ in range(abs(lb-la)):
        B = B.next

    while A != B and A and B:
        B = B.next
        A = A.next

    return A
```

## 26 Linked Lists Removing

Given a singly linked list and an integer k, remove the k<sup>th</sup> last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

### Solution

Given `start` as the start of the linked list and `k` as from problem definition

```python
def sol(start, k):
    ptr_k = ptr_curr = start
    while ptr_curr.next:
        if k == 0:
            ptr_k = ptr_k.next
        else:
            k -= 1
        ptr_curr = ptr_curr.next
    ptr_k.next = ptr_k.next.next

```

I start with 2 pointers and then I start to increment the second one when 'distant' by `k` steps from the first one.

## 51 Deck Shuffle

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the `52!` permutations of the deck is equally likely.

### Solution

Let's start creating a sorted deck, then choose the first card between 0 and 51, then the second one between 1 and 51 and so on, until the last one is betweek 51 and 51 (here we can skip)

```python
from random import randint

deck = [f'{n}{s}' for n in list(range(2,11)) + list('JQKA') for s in '♥♦♣♠']

for position in range(51):
    swap_with = randint(position, 51)
    if position != swap_with:
        deck[position], deck[swap_with] = deck[swap_with], deck[position]
```

## 53 Queue

Implement a queue using two stacks.

Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:

* `enqueue`, which inserts an element into the queue, and
* `dequeue`, which removes it.

### Solution

The concept is the following:
* Put the insert into the stack A
* Pull elements from the stack B, if B is empty, copy all A into B, this will reverse the order of the element and preserve the FIFO rule.

```python

from queue import LifoQueue

class Fifo:
    def __init__(self):
        self.A = LifoQueue()
        self.B = LifoQueue()

    def enqueue(self, e):
        self.A.put(e)

    def dequeue(self):
        if self.B.empty():
            while not self.A.empty():
                self.B.put(self.A.get())
        return self.B.get()
```

## 56 Color a Graph (dup 492)

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

## 58 Rolled Sorted Array

An sorted array of integers was rotated an unknown number of times.
Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.
For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
You can assume all the integers in the array are unique.

## 60 multiset sums

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.
For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.

## 66 Biased Coin Toss

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.
Write a function to simulate an unbiased coin toss.

## 68

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.
You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
For example, given M = 5 and the list of bishops:
(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:
[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.

## 62

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.
For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:
Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

## 61

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
Do this faster than the naive method of repeated multiplication.
For example, pow(2, 10) should return 1024.

## 49

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
Do this in O(N) time.

## 48

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
For example, given the following preorder traversal:
[a, b, d, e, c, f, g]
And the following inorder traversal:
[d, b, e, a, f, c, g]
You should return the following tree:
    a
   / \
  b   c
 / \ / \
d  e f  g

## 74

This problem was asked by Apple.
Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is `(i + 1) * (j + 1) (if 0-indexed)` or `i * j` (if 1-indexed).
Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.
For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:
| 1 | 2 | 3 | 4 | 5 | 6 |
| 2 | 4 | 6 | 8 | 10 | 12 |
| 3 | 6 | 9 | 12 | 15 | 18 |
| 4 | 8 | 12 | 16 | 20 | 24 |
| 5 | 10 | 15 | 20 | 25 | 30 |
| 6 | 12 | 18 | 24 | 30 | 36 |
And there are 4 12's in the table.

## 45

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).

## 76

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.
For example, given the following table:
cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to make it ordered:
ca
df
gi
So your function should return 1, since we only needed to remove 1 column.
As another example, given the following table:
abcdef
Your function should return 0, since the rows are already ordered (there's only one row).
As another example, given the following table:
zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it.

## 78

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

```python

# class Node():
#     value
#     next

def idx_of_smallest(l):
    idx = None
    _min = None
    for i,x in enumerate(l):
        if x in None:
            continue
        if _min is None or x.value < _min:
            idx = i
            _min = x.value
    return idx


def merge(list_of_linked_lists):
    loll = list(list_of_linked_lists)
    output = None
    current_output = None
    while any(loll):
        i = idx_of_smallest(loll)
        if i is None:
            break
        if output is None:
            output = copy(loll[i])
            current_output = output
        else:
            current_output.next = copy(loll[i])
            current_output = current_output.next
        current_output.next = None
        loll[i] = loll[i].next
    return output
```

## 79

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

## 83

This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:
```
    a
   / \
  b   c
 / \  /
d   e f
```
should become:
```
  a
 / \
 c  b
 \  / \
  f e  d
```

## 84

Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

```
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1     0 0 1
```

## 85

This problem was asked by Facebook.

Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.

```cpp
return (x * b) | ((1-b) * y);
```


## 86

This problem was asked by Google.
Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).
For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.

## 88

This question was asked by ContextLogic.
Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

## 89

This problem was asked by LinkedIn.
Determine whether a tree is a valid binary search tree.
A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.



## 90

This question was asked by Google.
Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).


## 97

This problem was asked by Stripe.

Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

* `set(key, value, time)`: sets key to value for t = time.
* `get(key, time)`: gets the key at t = time.

The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

Consider the following examples:

```python
d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2

d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
```

## 99

This problem was asked by Microsoft.
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.
Your algorithm should run in O(n) complexity.

## 113

This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?

## 109

This problem was asked by Cisco.
Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.
For example, 10101010 should be 01010101. 11100010 should be 11010001.
Bonus: Can you do this in one line?

         swap 1 with 2 and so on ...  swap 2 with 1 and so on
out_word = ((in_word & 0x55) << 1) | ((in_word & 0xAA) >> 1)

## 106

This problem was asked by Pinterest.
Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.
For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

## 103

TThis problem was asked by Square.
Given a string and a set of characters, return the shortest substring containing all the characters in the set.
For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".
If there is no substring containing all the characters in the set, return null.

## 102

This problem was asked by Lyft.
Given a list of integers and a number K, return which contiguous elements of the list sum to K.
For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.


## 110
This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

```
   1
  / \
 2   3
    / \
   4   5
```
Return [[1, 2], [1, 3, 4], [1, 3, 5]].

```
def solve(root):
    stack = [(root,)]
    while stack:
        path = stack.pop(0)
        last = path[-1]
        if last is None:
            continue
        if last.left is None and last.right is None:  # if we are a leaf
            yield [x.value for x in path if x is not None]
        if last.left is not None
            stack.append(path+(last.left,))
        if last.right is not None
            stack.append(path+(last.right,))
```

## 116

This problem was asked by Jane Street.

Generate a finite, but an arbitrarily large binary tree quickly in `O(1)`.

That is, `generate()` should return a tree whose size is unbounded but finite.

### Solution

#### Eager tree generation

If we ignore the O(1) generation constraint, we can create an unbounded tree by using randomness.

That is, we can generate the left and right sub-trees recursively `X%` of the time.

Since the question doesn’t have any constraints about the values the nodes can have, we’ll arbitrarily set it to 0.

```python
import random

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate():
    root = Node(0)

    if random.random() < 0.5:
        root.left = generate()
    if random.random() < 0.5:
        root.right = generate()

    return root
```

#### Lazy tree generation
The trick here is that we can generate the tree lazily. Here we use Python's property keyword, which lets us define a property on an object at look-up.

When the left or right property is looked up, we check if that sub-tree has been evaluated. If not, we recursively create a new node half the time. If it has been evaluated already, then we just return that node.

The object is created in constant time since none of the subtrees are evaluated when it’s created.

```python

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self._left = left
        self._right = right

        self._is_left_evaluated = False
        self._is_right_evaluated = False


    @property
    def left(self):
        if not self._is_left_evaluated:
            if random.random() < 0.5:
                self._left = Node(0)

        self._is_left_evaluated = True
        return self._left

    @property
    def right(self):
        if not self._is_right_evaluated:
            if random.random() < 0.5:
                self._right = Node(0)

        self._is_right_evaluated = True
        return self._right

def generate():
    return Node(0)

```

## 119

This problem was asked by Google.
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.
For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.

## 120

This problem was asked by Microsoft.
Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances. And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance.

## 122

This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at `matrix[0][0]`, and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

```
0 3 1 1
2 0 0 4
1 5 3 1
```

The most we can collect is `0 + 2 + 1 + 5 + 3 + 1` = `12` coins.


```python

from collections import deque, namedtuple

State = namedtuple('State', 'x y sum')

matrix = [
[0, 3, 1, 1],
[2, 0, 0, 4],
[1, 5, 3, 1],
]

def sol(m):
    def all():
        stack = deque((State(0,0,0),))

        while stack:
            p = stack.popleft()
            if p.x==len(m[-1])-1 and p.y==len(m)-1:
                yield p.sum+m[-1][-1]
            else:
                if p.x < len(m[p.y])-1:
                    stack.append(State(p.x+1, p.y, p.sum+m[p.y][p.x]))
                if p.y < len(m)-1:
                    stack.append(State(p.x, p.y+1, p.sum+m[p.y][p.x]))

    return max(all())

print(sol(matrix))

```


## 128

Good morning! Here's your coding interview problem for today.
The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.
All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the bottom and the smallest one at the top.
The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:
You can only move one disk at a time.
A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
You cannot place a larger disk on top of a smaller disk.
Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the rods are numbered, with the first rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.
For example, with n = 3, we can do this in 7 moves:
Move 1 to 3
Move 1 to 2
Move 3 to 2
Move 1 to 3
Move 2 to 1
Move 2 to 3
Move 1 to 3

## 129

Given a real number n, find the square root of n. For example, given n = 9, return 3.

## 130

This problem was asked by Facebook.
Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.
For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

## 131

This question was asked by Snapchat.
Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.

## 133

This problem was asked by Amazon.

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

```
   10
  /  \
 5    30
     /  \
   22    35
```

You can assume each node has a parent pointer.

## 136

This question was asked by Google.
Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.
For example, given the following matrix:
[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.

## 137

This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

* `init(size)`: initialize the array with size
* `set(i, val)`: updates index at i with val where val is either 1 or 0.
* `get(i)`: gets the value at index i.

## 139

This problem was asked by Google.
Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also implements peek(). peek shows the next element that would be returned on next().
Here is the interface:
class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass

## 140

This problem was asked by Facebook.
Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.
For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.
Follow-up: Can you do this in linear time and constant space?

## 143

This problem was asked by Amazon.
Given a pivot x, and a list lst, partition the list into three parts.
The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.
For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].

## 148

This problem was asked by Apple.
Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. Gray code is common in hardware so that we don't see temporary spurious values during transitions.
Given a number of bits n, generate a possible gray code for it.
For example, for n = 2, one gray code would be [00, 01, 11, 10].

## 146

This question was asked by BufferBox.
Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.
For example, given the following tree:
   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:
   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.

## 144

This problem was asked by Google.
Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i, where distance is measured in array indices.
For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a nearest larger integer, then return null.
Follow-up: If you can preprocess the array, can you do this in constant time?

## 151

Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

```
B B W
W W W
W W W
B B B
```

Becomes

```
B B G
G G G
G G G
B B B
```

## 152 (dup 493)

This problem was asked by Triplebyte.

You are given `n` numbers as well as `n` probabilities that sum up to 1. Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers `[1, 2, 3, 4]` and probabilities `[0.1, 0.5, 0.2, 0.2]`, your function should return `1` 10% of the time, `2` 50% of the time, and `3` and `4` 20% of the time.

You can generate random numbers between 0 and 1 uniformly.

## 155

This problem was asked by MongoDB.
Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).
You can assume that such element exists.
For example, given [1, 2, 1, 1, 3, 4, 0], return 1.

## 172

This problem was asked by Dropbox.
Given a string s and a list of words words, where each word is the same length, find all starting indices of substrings in s that is a concatenation of every word in words exactly once.
For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.
Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of "dog" and "cat" in s.
The order of the indices does not matter.

## 169

This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list `4 -> 1 -> -3 -> 99` should become `-3 -> 1 -> 4 -> 99`.

## 174

This problem was asked by Microsoft.
Describe and give an example of each of the following types of polymorphism:

- Ad-hoc polymorphism
- Parametric polymorphism
- Subtype polymorphism

## 179

This problem was asked by Google.
Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.
For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:
    5
   / \
  3   7
 / \   \
2   4   8

## 180

This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.

## 168

This problem was asked by Facebook.
Given an N by N matrix, rotate it by 90 degrees clockwise.
For example, given the following matrix:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?

```python
>>> a = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
>>> list(zip(*a[::-1]))
[(7, 4, 1), (8, 5, 2), (9, 6, 3)]
```

## 166

This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

* `next()`: returns the next element in the array of arrays. If there are no more elements, raise an exception.
* `has_next()`: returns whether or not the iterator still has elements left.

For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use `flatten` or otherwise clone the arrays. Some of the arrays can be empty.

## 164

This problem was asked by Google.
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate. Find it in linear time and space.

## 162

This problem was asked by Square.
Given a list of words, return the shortest unique prefix of each word. For example, given the list:
dog
cat
apple
apricot
fish
Return the list:
d
c
app
apr
f

## 158

This problem was asked by Slack.
You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?
You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.
For example, given the following matrix:
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:
Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.

## 156


This problem was asked by Facebook.
Given a positive integer n, find the smallest number of squared integers which sum to n.
For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.
Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.

## 192

This problem was asked by Google.
You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you can get to the end of the array.
For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.
Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

## 190

This problem was asked by Facebook.
Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.
For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.
Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

## 203

This problem was asked by Uber.

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.

## 198

This problem was asked by Google.
Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.
For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].

## 207

This problem was asked by Dropbox.
Given an undirected graph G, check whether it is bipartite. Recall that a graph is bipartite if its vertices can be divided into two independent sets, U and V, such that no edge connects vertices of the same set.

## 208

This problem was asked by LinkedIn.
Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before nodes greater than or equal to k.

For example, given the linked list `5 -> 1 -> 8 -> 0 -> 3` and `k = 3`, the solution could be `1 -> 0 -> 5 -> 8 -> 3`.

## 213

This problem was asked by Snapchat.

Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given `"2542540123"`, you should return `['254.25.40.123', '254.254.0.123']`.

## 211

This problem was asked by Microsoft.
Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].

## 215 (dup 490)

This problem was asked by Yelp.
The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:
* The horizontal distance of the root is 0.
* The horizontal distance of a left child is `hd(parent) - 1`.
* The horizontal distance of a right child is `hd(parent) + 1`.

For example, for the following tree, `hd(1) = -2`, and `hd(6) = 0`.

```
             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8
```

The bottom view of a tree, then, consists of the lowest node at each horizontal distance. If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be `[0, 1, 3, 6, 8, 9]`.

Given the root to a binary tree, return its bottom view.

## 222

This problem was asked by Quora.
Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.
For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".

## 216

This problem was asked by Facebook.
Given a number in Roman numeral format, convert it to decimal.
The values of Roman numerals are as follows:
{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.
For the input XIV, for instance, you should return 14.

## 218

This problem was asked by Yahoo.
Write an algorithm that computes the reversal of a directed graph. For example, if a graph consists of A -> B -> C, it should become A <- B <- C.

## 220

This problem was asked by Square.
In front of you is a row of N coins, with values v1, v1, ..., vn.
You are asked to play the following game. You and an opponent take turns choosing either the first or last coin from the row, removing it from the row, and receiving the value of the coin.
Write a program that returns the maximum amount of money you can win with certainty, if you move first, assuming your opponent plays optimally.

## 228

This problem was asked by Twitter.

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. For example, given `[10, 7, 76, 415]`, you should return `77641510`.

## 229

This problem was asked by Flipkart.
Snakes and Ladders is a game played on a 10 x 10 board, the goal of which is get from square 1 to square 100. On each turn players will roll a six-sided die and move forward a number of spaces equal to the result. If they land on a square that represents a snake or ladder, they will be transported ahead or behind, respectively, to a new square.
Find the smallest number of turns it takes to play snakes and ladders.
For convenience, here are the squares representing snakes and ladders, and their outcomes:
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

## 239

This problem was asked by Uber.
One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.
For a pattern to be valid, it must satisfy the following:
All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.
Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.

## 243

This problem was asked by Etsy.
Given an array of numbers N and an integer k, your task is to split N into k partitions such that the maximum sum of any partition is minimized. Return this sum.
For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8, since the optimal partition is [5, 1, 2], [7], [3, 4].

## 245

This problem was asked by Yelp.
You are given an array of integers, where each element represents the maximum number of steps that can be jumped going forward from that element. Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.
For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.

## 246


This problem was asked by Dropbox.

Given a list of words, determine whether the words can be chained to form a circle. A word X can be placed in front of another word Y in a circle if the last character of X is same as the first character of Y.

For example, the words `['chair', 'height', 'racket', 'touch', 'tunic']` can form
the following circle: `chair --> racket --> touch --> height --> tunic --> chair`.

```python

def sol(l):
    stack = [([x], l[:i]+l[i+1:]) for i, x in enumerate(l)]
    yielded = set()

    while stack:
        chain, words = stack.pop()
        if not words:
            if chain[0][0] == chain[-1][-1]:
                s = frozenset(chain)
                if s not in yielded:
                    yielded.add(s)
                    yield chain
        else:
            c = chain[-1][-1]
            for i, w in enumerate(words):
                if w[0] == c:
                    chain2 = chain + [w]
                    words2 = words[:i]+words[i+1:]
                    stack.append((chain2, words2))

print(list(sol(['chair', 'height', 'racket', 'touch', 'tunic'])))

```

## 250

This problem was asked by Google.
A cryptarithmet ic puzzle is a mathematical game where the digits of some numbers are represented by letters. Each letter represents a unique digit.
For example, a puzzle of the form:
  SEND
+ MORE
--------
 MONEY
may have the solution:
{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}
Given a three-word puzzle like the one above, create an algorithm that finds a solution.

## 251

This problem was asked by Amazon.
Given an array of a million integers between zero and a billion, out of order, how can you efficiently sort it? Assume that you cannot store an array of a billion elements in memory.

## 253

This problem was asked by PayPal.
Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.
For example, given the sentence "thisisazigzag" and k = 4, you should print:
t     a     g
 h   s z   a
  i i   i z
   s     g

## 254

This problem was asked by Yahoo.
Recall that a full binary tree is one in which each node is either a leaf node, or has two children. Given a binary tree, convert it to a full one by removing nodes with only one child.

For example, given the following tree:

```
         0
      /     \
    1         2
  /            \
3                 4
  \             /   \
    5          6     7
```

You should convert it to:

```
     0
  /     \
5         4
        /   \
       6     7
```


## 256

This problem was asked by Fitbit.
Given a linked list, rearrange the node values such that they appear in alternating low -> high -> low -> high ... form. For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return 1 -> 3 -> 2 -> 5 -> 4.

## 257

This problem was asked by WhatsApp.

Given an array of integers out of order, determine the bounds of the smallest window that must be sorted in order for the entire array to be sorted. For example, given `[3, 7, 5, 6, 9]`, you should return `(1, 3)`.

## 260

This problem was asked by Pinterest.

The sequence `[0, 1, ..., N]` has been jumbled, and the only clue you have for its order is an array representing whether each number is larger or smaller than the last. Given this information, reconstruct an array that is consistent with it. For example, given `[None, +, +, -, +]`, you could return `[1, 2, 3, 0, 4]`SSS.

## 262

This problem was asked by Mozilla.

A bridge in a connected (undirected) graph is an edge that, if removed, causes the graph to become disconnected. Find all the bridges in a graph.

## 263 (dup 431)

This problem was asked by Nest.
Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences. If a sentence is valid, the program should print it out.
We can consider a sentence valid if it conforms to the following rules:
The sentence must start with a capital letter, followed by a lowercase letter or a space.
All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
There must be a single space between each word.
The sentence must end with a terminal mark immediately following a word.

## 268

This problem was asked by Indeed.
Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.

## 270

This problem was asked by Twitter.
A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t), describing the time t it takes for a message to be sent from node a to node b. Whenever a node receives a message, it immediately passes the message on to a 7neighboring node, if possible.
Assuming all nodes are connected, determine how long it will take for every node to receive a message that begins at node 0.
For example, given N = 5, and the following edges:
edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take that much time.

## 272

This problem was asked by Spotify.

Write a function, `throw_dice(N, faces, total)`, that determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.

For example, `throw_dice(3, 6, 7)` should equal `15`.

## 275

This problem was asked by Epic.
The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221

As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.
Given an integer N, print the Nth term of this sequence.


## 281

This problem was asked by LinkedIn.
A wall consists of several rows of bricks of various integer lengths and uniform height. Your goal is to find a vertical line going from the top to the bottom of the wall that cuts through the fewest number of bricks. If the line goes through the edge between two bricks, this does not count as a cut.
For example, suppose the input is as follows, where values in each row represent the lengths of bricks in that row:
[[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]
The best we can we do here is to draw a line after the eighth brick, which will only require cutting through the bricks in the third and fifth row.
Given an input consisting of brick lengths for each row such as the one above, return the fewest number of bricks that must be cut to create a vertical line.

## 284 (dup 487)

This problem was asked by Yext.
Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents. For example, in the following diagram 4 and 6 are cousins.

```
    1
   / \
  2   3
 / \   \
4   5   6
```

Given a binary tree and a particular node, find all cousins of that node.

## 287

This problem was asked by Quora.

You are given a list of (website, user) pairs that represent users visiting websites. Come up with a program that identifies the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

```
[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e': 5), ('e', 6)]
```

Then a reasonable similarity metric would most likely conclude that a and e are the most similar, so your program should return [('a', 'e')].

## 288

This problem was asked by Salesforce.

The number 6174 is known as Kaprekar's contant, after the mathematician who discovered an associated property: for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value. The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.

Subtract the smaller number from the larger number.

For example, this algorithm terminates in three steps when starting from 1234:

```
4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
```

Write a function that returns how many steps this will take for a given input N.

## 291

This problem was asked by Glassdoor.
An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.
For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats required will be three.

## 294

This problem was asked by Square.
A competitive runner would like to create a route that starts and ends at his house, with the condition that the route goes entirely uphill at first, and then entirely downhill.
Given a dictionary of places of the form {location: elevation}, and a dictionary mapping paths between some of these locations to their corresponding distances, find the length of the shortest route satisfying the condition above. Assume the runner's home is location 0.
For example, suppose you are given the following input:
elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.

## 295

This problem was asked by Stitch Fix.
Pascal's triangle is a triangular array of integers constructed with the following formula:
The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.
Bonus: Can you do this using only O(k) space?

## 297

This problem was asked by Amazon.
At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set. For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.
preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize. Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.
For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.

## 302

This problem was asked by Uber.
You are given a 2-d matrix where each cell consists of either /, \, or an empty space. Write an algorithm that determines into how many regions the slashes divide the space.
For example, suppose the input for a three-by-six grid is the following:
\    /
 \  /
  \/
Considering the edges of the matrix as boundaries, this divides the grid into three triangles, so you should return 3.

## 301

This problem was asked by Triplebyte.

Implement a data structure which carries out the following operations without resizing the underlying array:

* `add(value)`: Add a value to the set of values.
* `check(value)`: Check whether a value is in the set.

The check method may return occasional false positives (in other words, incorrectly identifying an element as part of the set), but should always correctly identify a true element.

## 306

This problem was asked by Palantir.
You are given a list of N numbers, in which each number is located at most k places away from its sorted position. For example, if k = 1, a given element at index 4 might end up at indices 3, 4, or 5.
Come up with an algorithm that sorts this list in O(N log k) time.

## 316

You are given an array of length N, where each element i represents the number of ways we can produce i units of change. For example, [1, 0, 1, 1, 2] would indicate that there is only one way to make 0, 2, or 3 units, and two ways of making 4 units.
Given such an array, determine the denominations that must be in use. In the case above, for example, there must be coins with value 2, 3, and 4.

## 309

This problem was asked by Walmart Labs.

There are M people sitting in a row of N seats, where M < N. Your task is to redistribute people such that there are no gaps between any of them, while keeping overall movement to a minimum.

For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1], where 0 represents an empty seat and 1 represents a person. In this case, one solution would be to place the person on the right in the fourth seat. We can consider the cost of a solution to be the sum of the absolute distance each person must move, so that the cost here would be five.

Given an input such as the one above, return the lowest possible cost of moving people to remove all gaps.

## 314

This problem was asked by Spotify.
You are the technical director of WSPT radio, serving listeners nationwide. For simplicity's sake we can consider each listener to live along a horizontal line stretching from 0 (west) to 1000 (east).
Given a list of N listeners, and a list of M radio towers, each placed at various locations along this line, determine what the minimum broadcast range would have to be in order for each listener's home to be covered.
For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15]. In this case the minimum range would be 5, since that would be required for the tower at position 15 to reach the listener at position 20.

## 317

This problem was asked by Yahoo.
Write a function that returns the bitwise AND of all integers between M and N, inclusive.

## 320

This problem was asked by Amazon.

Given a string, find the length of the smallest window that contains every distinct character. Characters may appear more than once in the window.

For example, given "jiujitsu", you should return `5`, corresponding to the final five letters.

### Solution

```python
def solve(s):
    s_set = set(s)
    ps = 0
    pe = len(s)
    pre_pe = pe

    while s_set == set(s[ps:pe]):
        if s_set == set(s[ps+1:pe]):
            ps+=1
        else:
            pre_pe = pe
            pe-=1
    return pre_pe - ps
```

## 322

This problem was asked by Flipkart.

Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.

On the ith jump, you may move exactly i places to the left or right.

Find a path with the fewest number of jumps required to get from 0 to N.

```python
def sol(n):
    ret = [1,]
    _sum = 1
    p = 2
    while (_sum - n) < 0 or (_sum - n) %2 == 1:
        ret.append(p)
        _sum+=p
        p+=1
    m = (_sum - n)//2
    if m:
        ret[m-1] = -ret[m-1]
    return ret


print(sol(89))
```

## 323

This problem was asked by Dropbox.
Create an algorithm to efficiently compute the approximate median of a list of numbers.
More precisely, given an unordered list of N numbers, find an element whose rank is between N / 4 and 3 * N / 4, with a high level of certainty, in less than O(N) time.

## 328

Good morning! Here's your coding interview problem for today.
This problem was asked by Facebook.
In chess, the Elo rating system is used to calculate player strengths based on game results.
A simplified description of the Elo system is as follows. Every player begins at the same score. For each subsequent game, the loser transfers some points to the winner, where the amount of points transferred depends on how unlikely the win is. For example, a 1200-ranked player should gain much more points for beating a 2000-ranked player than for beating a 1300-ranked player.
Implement this system.

## 331 (dup 460)

This problem was asked by LinkedIn.

You are given a string consisting of the letters x and y, such as xyxxxyxyy. In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come before all y's. In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.

## 333 (dup 486)

This problem was asked by Pinterest.

At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.

Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.

## 336

This problem was asked by Microsoft.

Write a program to determine how many distinct ways there are to create a max heap from a list of N given integers.

For example, if N = 3, and our integers are [1, 2, 3], there are two ways, shown below.

```
  3      3
 / \    / \
1   2  2   1
```

## 338

This problem was asked by Facebook.

Given an integer n, find the next biggest integer with the same number of 1-bits on. For example, given the number 6 (`0110` in binary), return 9 (`1001`).

## 342

This problem was asked by Stripe.

reduce (also known as fold) is a function that takes in an array, a combining function, and an initial value and builds up a result by calling the combining function on each element of the array, left to right. For example, we can write sum() in terms of reduce:

def add(a, b):
    return a + b

def sum(lst):
    return reduce(lst, add, 0)

This should call add on the initial value with the first element of the array, and then the result of that with the second element of the array, and so on until we reach the end, when we return the sum of the array.

Implement your own version of reduce.

```python

def reduce(lst, fx, ret):
    for x in lst:
        ret = fx(ret, x)
    return ret

```


## 343 - duplicate 482

This problem was asked by Google.

Given a binary search tree and a range [a, b] (inclusive), return the sum of the elements of the binary search tree within the range.

For example, given the following tree:

```
    5
   / \
  3   8
 / \ / \
2  4 6  10
```

and the range [4, 9], return 23 (5 + 4 + 6 + 8).

## 345

This problem was asked by Google.

You are given a set of synonyms, such as (big, large) and (eat, consume). Using this set, determine if two sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:

* "He wants to eat food."
* "He wants to consume food."

Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c): consider the case of (coach, bus) and (coach, teacher).

Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply (b, c)?

## 346

This problem was asked by Airbnb.

You are given a huge list of airline ticket prices between different cities around the world on a given day. These are all direct flights. Each element in the list has the format (source_city, destination, price).

Consider a user who is willing to take up to k connections from their origin city A to their destination B. Find the cheapest fare possible for this journey and print the itinerary for that journey.

For example, our traveler wants to go from JFK to LAX with up to 3 connections, and our input flights are as follows:

```
[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
```

Due to some improbably low flight prices, the cheapest itinerary would be JFK -> ATL -> ORD -> LAX, costing $440.

## 350

This problem was asked by Uber.

Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:

Given N = 4, return 1 (4)
Given N = 17, return 2 (16 + 1)
Given N = 18, return 2 (9 + 9)

## 353

This problem was asked by Square.

You are given a histogram consisting of rectangles of different heights. These heights are represented in an input list, such that [1, 3, 2, 5] corresponds to the following diagram:

```
      x
      x
  x   x
  x x x
x x x x
```

Determine the area of the largest rectangle that can be formed only from the bars of the histogram. For the diagram above, for example, this would be six, representing the `2 x 3` area at the bottom right.

## 360

This problem was asked by Spotify.

You have access to ranked lists of songs for various users. Each song is represented as an integer, and more preferred songs appear earlier in each list. For example, the list `[4, 1, 7]` indicates that a user likes song `4` the best, followed by songs `1` and `7`.

Given a set of these ranked lists, interleave them to create a playlist that satisfies everyone's priorities.

For example, suppose your input is `{[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]}`. In this case a satisfactory playlist could be `[2, 1, 6, 7, 3, 9, 5]`.

## 361

This problem was asked by Facebook.

Mastermind is a two-player game in which the first player attempts to guess the secret code of the second. In this version, the code may be any six-digit number with all distinct digits.

Each turn the first player guesses some number, and the second player responds by saying how many digits in this number correctly matched their location in the secret code. For example, if the secret code were 123456, then a guess of 175286 would score two, since 1 and 6 were correctly placed.

Write an algorithm which, given a sequence of guesses and their scores, determines whether there exists some secret code that could have produced them.

For example, for the following scores you should return True, since they correspond to the secret code 123456:

```
{175286: 2, 293416: 3, 654321: 0}
```

However, it is impossible for any key to result in the following scores, so in this case you should return False:

```
{123456: 4, 345678: 4, 567890: 4}
```

## 363

This problem was asked by Squarespace.

Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:

```python
add_subtract(7) -> 7

add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0

add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11
```


## 364

This problem was asked by Facebook.

Describe an algorithm to compute the longest increasing subsequence of an array of numbers in O(n log n) time.


## 366

This problem was asked by Flexport.

Given a string s, rearrange the characters so that any two adjacent characters are not the same. If this is not possible, return null.

For example, if s = yyz then return yzy. If s = yyy then return null.


## 367

This problem was asked by Two Sigma.

Given two sorted iterators, merge it into one iterator.

For example, given these two iterators:

```
foo = iter([5, 10, 15])
bar = iter([3, 8, 9])
```

You should be able to do:

```
for num in merge_iterators(foo, bar):
    print(num)

# 3
# 5
# 8
# 9
# 10
# 15
```

Bonus: Make it work without pulling in the contents of the iterators in memory.


## 369

This problem was asked by Two Sigma.

You’re tracking stock price at a given instance of time. Implement an API with the following functions: add(), update(), remove(), which adds/updates/removes a datapoint for the stock price you are tracking. The data is given as (timestamp, price), where timestamp is specified in unix epoch time.

Also, provide max(), min(), and average() functions that give the max/min/average of all values seen thus far.


## 375

This problem was asked by Google.

The h-index is a metric used to measure the impact and productivity of a scientist or researcher.

A scientist has index h if h of their N papers have at least h citations each, and the other N - h papers have no more than h citations each. If there are multiple possible values for h, the maximum value is used.

Given an array of natural numbers, with each value representing the number of citations of a researcher's paper, return the h-index of that researcher.

For example, if the array was:

```
[4, 0, 0, 2, 3]
```

This means the researcher has 5 papers with 4, 1, 0, 2, and 3 citations respectively. The h-index for this researcher is 2, since they have 2 papers with at least 2 citations and the remaining 3 papers have no more than 2 citations.

## 378

This problem was asked by Coinbase.

Write a function that takes in a number, string, list, or dictionary and returns its JSON encoding. It should also handle nulls.

For example, given the following input:
```
[None, 123, ["a", "b"], {"c":"d"}]
```
You should return the following, as a string:

```
'[null, 123, ["a", "b"], {"c": "d"}]'
```

## 380

This problem was asked by Nextdoor.

Implement integer division without using the division operator. Your function should return a tuple of (dividend, remainder) and it should take two numbers, the product and divisor.

For example, calling divide(10, 3) should return (3, 1) since the divisor is 3 and the remainder is 1.

Bonus: Can you do it in O(log n) time?

## 383

This problem was asked by Gusto.

Implement the function embolden(s, lst) which takes in a string s and list of substrings lst, and wraps all substrings in s with an HTML bold tag <b> and </b>.

If two bold tags overlap or are contiguous, they should be merged.

For example, given s = abcdefg and lst = ["bc", "ef"], return the string a<b>bc</b>d<b>ef</b>g.

Given s = abcdefg and lst = ["bcd", "def"], return the string a<b>bcdef</b>g, since they overlap.

## 384

This problem was asked by WeWork.

You are given an array of integers representing coin denominations and a total amount of money. Write a function to compute the fewest number of coins needed to make up that amount. If it is not possible to make that amount, return null.

For example, given an array of [1, 5, 10] and an amount 56, return 7 since we can use 5 dimes, 1 nickel, and 1 penny.

Given an array of [5, 8] and an amount 15, return 3 since we can use 5 5-cent coins.


## 385

This problem was asked by Apple.

You are given a hexadecimal-encoded string that has been XOR'd against a single char.

Decrypt the message. For example, given the string:

```
7a575e5e5d12455d405e561254405d5f1276535b5e4b12715d565b5c551262405d505e575f
```

You should be able to decrypt it and get:

```
Hello world from Daily Coding Problem
```

## 390

This problem was asked by Two Sigma.

You are given an unsorted list of 999,000 unique integers, each from 1 and 1,000,000. Find the missing 1000 numbers. What is the computational and space complexity of your solution?

## 393

This problem was asked by Airbnb.

Given an array of integers, return the largest range, inclusive, of integers that are all included in the array.

For example, given the array `[9, 6, 1, 3, 8, 10, 12, 11]`, return `(8, 12)` since `8, 9, 10, 11, and 12` are all in the array.

## 395

This problem was asked by Robinhood.

Given an array of strings, group anagrams together.

For example, given the following array:
```
['eat', 'ate', 'apt', 'pat', 'tea', 'now']
```

Return:

```
[['eat', 'ate', 'tea'],
 ['apt', 'pat'],
 ['now']]
 ```

## 407

This problem was asked by Samsung.

A group of houses is connected to the main water plant by means of a set of pipes. A house can either be connected by a set of pipes extending directly to the plant, or indirectly by a pipe to a nearby house which is otherwise connected.

For example, here is a possible configuration, where A, B, and C are houses, and arrows represent pipes:
```
A <--> B <--> C <--> plant
```
Each pipe has an associated cost, which the utility company would like to minimize. Given an undirected graph of pipe connections, return the lowest cost configuration of pipes such that each house has access to water.

In the following setup, for example, we can remove all but the pipes from plant to A, plant to B, and B to C, for a total cost of 16.

```
pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
```

## 408

This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

## 412

This problem was asked by Epic.

The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:
```
1
11
21
1211
111221
```
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.

## 421

This problem was asked by Amazon.

Given an array of a million integers between zero and a billion, out of order, how can you efficiently sort it? Assume that you cannot store an array of a billion elements in memory.

## 424

This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?

## 427

This problem was asked by Square.

A competitive runner would like to create a route that starts and ends at his house, with the condition that the route goes entirely uphill at first, and then entirely downhill.

Given a dictionary of places of the form {location: elevation}, and a dictionary mapping paths between some of these locations to their corresponding distances, find the length of the shortest route satisfying the condition above. Assume the runner's home is location 0.

For example, suppose you are given the following input:

```
elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
```

In this case, the shortest valid path would be `0 -> 2 -> 4 -> 0`, with a distance of 28.

## 429

This problem was asked by Stitch Fix.

Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number `1`.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:

```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```
Given an input `k`, return the `k`<sup>`th`</sup> row of Pascal's triangle.

Bonus: Can you do this using only `O(k)` space?

## 431

This problem was asked by Nest.

Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences. If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

The sentence must start with a capital letter, followed by a lowercase letter or a space.
All other characters must be lowercase letters, separators (`,`,`;`,`:`) or terminal marks (`.`,`?`,`!`,`‽`).
There must be a single space between each word.
The sentence must end with a terminal mark immediately following a word.

## 433

This problem was asked by Facebook.

Given an integer n, find the next biggest integer with the same number of 1-bits on. For example, given the number 6 (0110 in binary), return 9 (1001).

## 435

This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

```
[a, b, d, e, c, f, g]
```

And the following inorder traversal:

```
[d, b, e, a, f, c, g]
```

You should return the following tree:
```
    a
   / \
  b   c
 / \ / \
d  e f  g
```

## 461

This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

## 437

This problem was asked by Square.

Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.

## 439

This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

## 440

This problem was asked by Microsoft.

Describe and give an example of each of the following types of polymorphism:

* Ad-hoc polymorphism
* Parametric polymorphism
* Subtype polymorphism

## 441

This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

* The first part contains all elements in lst that are less than x
* The second part contains all elements in lst that are equal to x
* The third part contains all elements in lst that are larger than x

Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].

## 443 (dup 53)

This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.


## 445

This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

```
   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
```

should be pruned to:

```
   0
  / \
 1   0
    /
   1
```

We do not remove the tree at the root or its left child because it still has a 1 as a descendant.

## 446

This problem was asked by Indeed.

Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.

## 447

This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.

## 454

This problem was asked by Facebook.

Describe an algorithm to compute the longest increasing subsequence of an array of numbers in O(n log n) time

## 455

This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

* Any live cell with less than two live neighbours dies.
* Any live cell with two or three live neighbours remains living.
* Any live cell with more than three live neighbours dies.
* Any dead cell with exactly three live neighbours becomes a live cell.

A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

## 460

This problem was asked by LinkedIn.

You are given a string consisting of the letters `x` and `y`, such as `xyxxxyxyy`. In addition, you have an operation called flip, which changes a single `x` to `y` or vice versa.

Determine how many times you would need to apply this operation to ensure that all `x`'s come before all `y`'s. In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.

## 459

This problem was asked by Uber.

Write a program that determines the smallest number of perfect squares that sum up to `N`.

Here are a few examples:

- Given `N = 4`, return `1` (4)
- Given `N = 17`, return `2` (16 + 1)
- Given `N = 18`, return `2` (9 + 9)

## 472

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

## 469 (361)

This problem was asked by Facebook.

Mastermind is a two-player game in which the first player attempts to guess the secret code of the second. In this version, the code may be any six-digit number with all distinct digits.

Each turn the first player guesses some number, and the second player responds by saying how many digits in this number correctly matched their location in the secret code. For example, if the secret code were `123456`, then a guess of `175286` would score two, since `1` and `6` were correctly placed.

Write an algorithm which, given a sequence of guesses and their scores, determines whether there exists some secret code that could have produced them.

For example, for the following scores you should return `True`, since they correspond to the secret code `123456`:

```python
{175286: 2, 293416: 3, 654321: 0}
```

However, it is impossible for any key to result in the following scores, so in this case you should return False:

```python
{123456: 4, 345678: 4, 567890: 4}
```

## 470 (144)

This problem was asked by Google.

Given an array of numbers and an index `i`, return the index of the nearest larger number of the number at index `i`, where distance is measured in array indices.

For example, given `[4, 1, 3, 5, 6]` and index `0`, you should return `3`.

If two distances to larger numbers are the equal, then return any one of them. If the array at `i` doesn't have a nearest larger integer, then return `null`.

Follow-up: If you can preprocess the array, can you do this in constant time?

## 495

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

## 535

This problem was asked by Goldman Sachs.

You are given `N` identical eggs and access to a building with `k` floors. Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks when dropped from the `x`<sup>`th`</sup> floor, you can assume it will also break when dropped from any floor greater than `x`.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if `N = 1` and `k = 5`, we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor, so our solution will be `5`.

## 546

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array `[3, 4, 9, 6, 1]`, return `[1, 1, 2, 1, 0]`, since:

* There is 1 smaller element to the right of 3
* There is 1 smaller element to the right of 4
* There are 2 smaller elements to the right of 9
* There is 1 smaller element to the right of 6
* There are no smaller elements to the right of 1

## 558

This problem was asked by Google.

The area of a circle is defined as `πr<sup>2</sup>`. Estimate `π` to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is `x<sup>2</sup> + y<sup>2</sup>= r<sup>2<sup>`.

### Solution

Let's define a circle of radius 1 and let's create random points between `(0,0)` and `(1,1)`. if the square of the coordinates of the point summed togheter are <=1 it means we are inside the circle otherwise they are are outside.

Let's work on a single quadrante and multiply be 4.

```python
from random import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, p2):
        return Point(self.x+p2.x, self.y+p2.y)
    def __iter__(self):
        def gen():
            yield self.x
            yield self.y
        return gen()
    def __repr__(self):
        return f"{self.__class__}({self.x}, {self.y})"

def gen():
   while True:
       yield Point(random(), random())


def sol(precision = 3):
    inside = 0
    prepi = 0
    zeros = 10**(precision+2)
    mult = 4 * zeros
    for i,(x,y) in enumerate(gen()):
        if (x**2+y**2)<=1:
            inside+=1
        if i>258_000 and i%zeros == 0:
            pi = mult*inside//(i+1)
            if pi == prepi:  ## wait for a stable value
                break
            prepi=pi
    print(("{:0.%if}" % precision).format(pi/zeros))

sol()

```

## 566

This problem was asked by Facebook.

A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected. For example, any binary tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. You can choose to represent the graph as either an adjacency matrix or adjacency list.

## 567

This problem was asked by Jane Street.

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair. For example, `car(cons(3, 4))` returns `3`, and `cdr(cons(3, 4))` returns `4`.

Given this implementation of cons:

```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

Implement `car` and `cdr`.

## 593

This problem was asked by Mailchimp.

You are given an array representing the heights of neighboring buildings on a city street, from east to west. The city assessor would like you to write an algorithm that returns how many of these buildings have a view of the setting sun, in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the top floors of the buildings with heights 8, 6, and 1 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?

## 616

This problem was asked by Google.

A cryptarithmetic puzzle is a mathematical game where the digits of some numbers are represented by letters. Each letter represents a unique digit.

For example, a puzzle of the form:

```
  SEND
+ MORE
--------
 MONEY
```

may have the solution:

```
{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}
```

Given a three-word puzzle like the one above, create an algorithm that finds a solution.

## 692

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string `s` and a set of all possible query strings, return all strings in the set that have `s` as a prefix.

For example, given the query string `de` and the set of strings `[dog, deer, deal]`, return `[deer, deal]`.

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

## 693

This problem was asked by Cisco.

Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

For example, `10101010` should be `01010101`. `11100010` should be `11010001`.

Bonus: Can you do this in one line?

### Solution
```
out_word = ((in_word & 0x55) << 1) | ((in_word & 0xAA) >> 1)
```

### 702

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

The following test should pass:

```
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```


## 758 This problem was asked by Facebook.

Write a function that rotates a list by k elements.

For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].

Try solving this without creating a copy of the list.

How many swap or move operations do you need?