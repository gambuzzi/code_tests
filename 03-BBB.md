# Hard Questions

## 19 Houses

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.
Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

## 52 Least Recently Used

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size `n`, and contain the following methods:

* `set(key, value)`: sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
* `get(key)`: gets the value at key. If no such key exists, return `null`.

Each operation should run in `O(1)` time.

## 744

This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size `n`, and contain the following methods:

* `set(key, value)`: sets key to value. If there are already `n` items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
* `get(key)`: gets the value at key. If no such key exists, return `null`.

Each operation should run in `O(1)` time.

## 54 Sudoku

Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.
Implement an efficient sudoku solver.

## 57 Break Text

Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or less. You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.
You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.
For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

## 59 file syncing

Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?

## 64

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.

## 75

This problem was asked by Microsoft.
Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.
For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

## 87

This problem was asked by Uber.
A rule looks like this:
A NE B
This means this means point A is located northeast of point B.
A SW C
means that point A is southwest of C.
Given a list of rules, check if the sum of the rules validate. For example:
A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.
A NW B
A N B
is considered valid.

## 92

Good morning! Here's your coding interview problem for today.
This problem was asked by Airbnb.
We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.
Return null if there is no such ordering.
For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].

## 93

This problem was asked by Apple.
Given a tree, find the largest tree/subtree that is a BST.
Given a tree, return the size of the largest tree/subtree that is a BST.

## 115

This problem was asked by Google.

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

## 114

This problem was asked by Facebook.
Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"
Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"

## 112

This problem was asked by Twitter.
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

## 111

This problem was asked by Twitter.
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

## 121

This problem was asked by Google.
Given a string which we can delete at most k, return whether you can make a palindrome.
For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.

## 123

This problem was asked by LinkedIn.
Given a string, return whether it represents a number. Here are the different kinds of numbers:
"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:
"a"
"x 1"
"a -2"
"-"

## 138

This problem was asked by Google.

Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢

## 141

This problem was asked by Microsoft.
Implement 3 stacks using a single list:
class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass

## 142

This problem was asked by Google.
You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.
For example, (()* and (*) are balanced. )*( is not balanced.

## 147

Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.

## 153

Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", return 1 because there's only one word "cat" in between the two words.

## 178

This problem was asked by Two Sigma.

Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.

## 160

his problem was asked by Uber.
Given a tree where each edge has a weight, compute the length of the longest path in the tree.
For example, given the following tree:
   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, the longest path would be c -> a -> d -> f, with a length of 17.
The path does not have to pass through the root, and each node can have any amount of children.

## 163 (481)

This problem was asked by Jane Street.
Given an arithmetic expression in [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation), write a program to evaluate it.
The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.
For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.
You can assume the given expression is always valid.

## 167

This problem was asked by Airbnb.
Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.
For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].

## 181

This problem was asked by Google.
Given a string, split it into as few strings as possible such that each string is a palindrome.
For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].
Given the input string abc, return ["a", "b", "c"].

## 186

This problem was asked by Microsoft.
Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.
For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which is the smallest possible difference.

## 193

This problem was asked by Affirm.
Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock. You're also given a number fee that represents a transaction fee for each buy and sell transaction.
You must buy before you can sell the stock, but you can make as many transactions as you like.
For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you could buy the stock at 1 dollar, and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10 dollars. Since we did two transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.

## 195

This problem was asked by Google.
Let A be an N by M matrix in which every row and every column is sorted.
Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].
For example, given the following matrix:
[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]
And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.

## 199

This problem was asked by Facebook.

Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".

## 200

This problem was asked by Microsoft.

Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X if every interval in X contains at least one point in P. Compute the smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].

## 209

This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.

## 217

This problem was asked by Oracle.

We say a number is sparse if there are no adjacent ones in its binary representation. For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N, find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.

## 219

This problem was asked by Salesforce.
Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6 vertically suspended grid. The game ends either when one player creates a line of four consecutive discs of their color (horizontally, vertically, or diagonally), or when there are no more spots left in the grid.
Design and implement Connect 4.

## 223

This problem was asked by Palantir.

Typically, an implementation of in-order traversal of a binary tree has O(h) space complexity, where h is the height of the tree.

Write a program to compute the in-order traversal of a binary tree using O(1) space.

## 234

This problem was asked by Microsoft.
Recall that the minimum spanning tree is the subset of edges of a tree that connect all its vertices with the smallest possible total edge weight. Given an undirected graph with weighted edges, compute the maximum weight spanning tree.

## 235

This problem was asked by Facebook.

Given an array of numbers of length `N`, find both the minimum and maximum using less than `2 * (N - 2)` comparisons.

## 240

This problem was asked by Spotify.
There are N couples sitting in a row of length 2 * N. They are currently ordered randomly, but would like to rearrange themselves so that each couple's partners can sit side by side.
What is the minimum number of swaps necessary for this to happen?

## 242

You are given an array of length 24, where each element represents the number of new subscribers during the corresponding hour. Implement a data structure that efficiently supports the following:
update(hour: int, value: int): Increment the element at index hour by value.
query(start: int, end: int): Retrieve the number of subscribers that have signed up between start and end (inclusive).
You can assume that all values get cleared at the end of the day, and that you will not be asked for start and end values that wrap around midnight.

## 248

This problem was asked by Nvidia.

Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.

```python

"""
let's stick to math functions
"""

def _max(a, b):
    try:
        sa = a/abs(a)
    except:
        sa = 1
    try:
        sb = b/abs(b)
    except:
        sb = 1
    try:
        m = abs(a)//abs(b)
    except:
        m = abs(a+1)//abs(b+1)
    try:
        m //= m
    except:
        pass
    d = {
        (-1, 1, 0): b,
        (-1, 1, 1): b,
        ( 1,-1, 0): a,
        ( 1,-1, 0): a,
        (-1,-1, 0): a,
        (-1,-1, 1): b,
        ( 1, 1, 0): b,
        ( 1, 1, 1): a,
    }
    return d[(sa,sb,m)]

assert _max(6,10) == 10
assert _max(6,0) == 6
assert _max(-6,10) == 10
assert _max(-6,-10) == -6

```

## 249

This problem was asked by Salesforce.
Given an array of integers, find the maximum XOR of any two elements.

## 264

This problem was asked by LinkedIn.
Given a set of characters C and an integer k, a De Bruijn sequence is a cyclic sequence in which every possible k-length string of characters in C occurs exactly once.
For example, suppose C = {0, 1} and k = 3. Then our sequence should contain the substrings {'000', '001', '010', '011', '100', '101', '110', '111'}, and one possible solution would be 00010111.
Create an algorithm that finds a De Bruijn sequence.

## 267

This problem was asked by Oracle.
You are presented with an 8 by 8 matrix representing the positions of pieces on a chess board. The only pieces on the board are the black king and various white pieces. Given this matrix, determine whether the king is in check.
For details on how each piece moves, see here.
For example, given the following matrix:
...K....
........
.B......
......P.
.......R
..N.....
........
.....Q..
You should return True, since the bishop is attacking the king diagonally.

## 271

This problem was asked by Netflix.
Given a sorted list of integers of length N, determine if an element x is in the list without performing any multiplication, division, or bit-shift operations.
Do this in O(log N) time.

## 274

This problem was asked by Facebook.
Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a mathematical expression to obtain the answer.
Don't use eval or a similar built-in parser.
For example, given '-1 + (2 + 3)', you should return 4.

## 276

This problem was asked by Dropbox.
Implement an efficient string matching algorithm.
That is, given a string of length N and a pattern of length k, write a program that searches for the pattern in the string with less than O(N * k) worst-case time complexity.
If the pattern is found, return the start index of its location. If not, return False.

## 286

The skyline of a city is composed of several buildings of various widths and heights, possibly overlapping one another when viewed from a distance.

We can represent the buildings using an array of (left, right, height) tuples, which tell us where on an imaginary x-axis a building begins and ends, and how tall it is.

The skyline itself can be described by a list of (x, height) tuples, giving the locations at which the height visible to a distant observer changes, and each new height.

Given an array of buildings as described above, create a function that returns the skyline.

For example, suppose the input consists of the buildings [(0, 15, 3), (4, 11, 5), (19, 23, 4)]. In aggregate, these buildings would create a skyline that looks like the one below.

```
     ______
    |      |        ___
 ___|      |___    |   |
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------

```

As a result, your function should return [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)].

## 289

Google.

The game of Nim is played as follows. Starting with three heaps, each containing a variable number of items, two players take turns removing one or more items from a single pile. The player who eventually is forced to take the last stone loses. For example, if the initial heap sizes are 3, 4, and 5, a game could be played as shown below:

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

Given a list of non-zero starting values [a, b, c], and assuming optimal play, determine whether the first player has a forced win.

## 292

This problem was asked by Twitter.
A teacher must divide a class of students into two teams to play dodgeball. Unfortunately, not all the kids get along, and several refuse to be put on the same team as that of their enemies.
Given an adjacency list of students and their enemies, write an algorithm that finds a satisfactory pair of teams, or returns False if none exists.
For example, given the following enemy graph you should return the teams {0, 1, 4, 5} and {2, 3}.
students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}
On the other hand, given the input below, you should return False.
students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}

## 293

This problem was asked by Uber.
You have N stones in a row, and would like to create from them a pyramid. This pyramid should be constructed such that the height of each stone increases by one until reaching the tallest stone, after which the heights decrease by one. In addition, the start and end stones of the pyramid should each be one stone high.
You can change the height of any stone by paying a cost of 1 unit to lower its height by 1, as many times as necessary. Given this information, determine the lowest cost method to produce this pyramid.
For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is to pay 2 to create [0, 1, 2, 3, 2, 1].


## 296

This problem was asked by Etsy.

Given a sorted array, convert it into a height-balanced binary search tree.

```python
"""
Let's have the array as a list
Let's create the tree as a list
Root is tree[0]
First left node is tree[1]
First right node is tree[2]
the usul rule is : tree[<parent>] => left:tree[<parent>*2+1] , right:tree[<parent>*2+2]

Let's create a generator to get the mapping between the 2 lists.
The generator is visiting the binary tree in order to generate a sorted array.
So we just have to map the list back to the tree.
"""

def make_tree(arr):
    def gen(_len, p=0):
        l = 2*p+1
        r = 2*p+2
        if l<_len:
            yield from gen(_len, l)
        yield p
        if r<_len:
            yield from gen(_len, r)

    l = len(arr)
    tree = [None] * l
    for i, g in enumerate(gen(l)):
            tree[g] = arr[i]

    return tree

```

## 304

This problem was asked by Two Sigma.
A knight is placed on a given square on an 8 x 8 chessboard. It is then moved randomly several times, where each move is a standard knight move. If the knight jumps off the board at any point, however, it is not allowed to jump back on.
After k moves, what is the probability that the knight remains on the board?

## 308

This problem was asked by Quantcast.
You are presented with an array representing a Boolean expression. The elements are of two kinds:
T and F, representing the values True and False.
&, |, and ^, representing the bitwise operators for AND, OR, and XOR.
Determine the number of ways to group the array elements using parentheses so that the entire expression evaluates to True.
For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case, there are two acceptable groupings: (F | T) & T and F | (T & T).

## 313

This problem was asked by Citrix.
You are given a circular lock with three wheels, each of which display the numbers 0 through 9 in order. Each of these wheels rotate clockwise and counterclockwise.
In addition, the lock has a certain number of "dead ends", meaning that if you turn the wheels to one of these combinations, the lock becomes stuck in that state and cannot be opened.
Let us consider a "move" to be a rotation of a single wheel by one digit, in either direction. Given a lock initially set to 000, a target combination, and a list of dead ends, write a function that returns the minimum number of moves required to reach the target state, or None if this is impossible.

## 318

This problem was asked by Apple.
You are going on a road trip, and would like to create a suitable music playlist. The trip will require N songs, though you only have M songs downloaded, where M < N. A valid playlist should select each song at least once, and guarantee a buffer of B songs between repeats.
Given N, M, and B, determine the number of valid playlists.

## 319

This problem was asked by Airbnb.
An 8-puzzle is a game played on a 3 x 3 board of tiles, with the ninth tile missing. The remaining tiles are labeled 1 through 8 but shuffled randomly. Tiles may slide horizontally or vertically into an empty space, but may not be removed from the board.
Design a class to represent the board, and find a series of steps to bring the board to the state [[1, 2, 3], [4, 5, 6], [7, 8, None]].

## 326

This problem was asked by Netflix.

A Cartesian tree with sequence S is a binary tree defined by the following two properties:

    It is heap-ordered, so that each parent value is strictly less than that of its children.
    An in-order traversal of the tree produces nodes with values that correspond exactly to S.

For example, given the sequence [3, 2, 6, 1, 9], the resulting Cartesian tree would be:

```
      1
    /   \
  2       9
 / \
3   6
```
Given a sequence S, construct the corresponding Cartesian tree.

## 330

This problem was asked by Dropbox.

A Boolean formula can be said to be satisfiable if there is a way to assign truth values to each variable such that the entire formula evaluates to true.

For example, suppose we have the following formula, where the symbol ¬ is used to denote negation:

(¬c OR b) AND (b OR c) AND (¬b OR c) AND (¬c OR ¬a)

One way to satisfy this formula would be to let a = False, b = True, and c = True.

This type of formula, with AND statements joining tuples containing exactly one OR, is known as 2-CNF.

Given a 2-CNF formula, find a way to assign truth values to satisfy it, or return False if this is impossible.

## 329

This problem was asked by Amazon.

The stable marriage problem is defined as follows:

Suppose you have N men and N women, and each person has ranked their prospective opposite-sex partners in order of preference.

For example, if N = 3, the input could be something like this:

guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}

Write an algorithm that pairs the men and women together in such a way that no two people of opposite sex would both rather be with each other than with their current partners.

## 335

This problem was asked by Google.

PageRank is an algorithm used by Google to rank the importance of different websites. While there have been changes over the years, the central idea is to assign each site a score based on the importance of other pages that link to that page.

More mathematically, suppose there are N sites, and each site i has a certain count Ci of outgoing links. Then the score for a particular site Sj is defined as :

score(Sj) = (1 - d) / N + d * (score(Sx) / Cx+ score(Sy) / Cy+ ... + score(Sz) / Cz))

Here, Sx, Sy, ..., Sz denote the scores of all the other sites that have outgoing links to Sj, and d is a damping factor, usually set to around 0.85, used to model the probability that a user will stop searching.

Given a directed graph of links between various websites, write a program that calculates each site's page rank.

## 337

This problem was asked by Apple.

Given a linked list, uniformly shuffle the nodes. What if we want to prioritize space over time?

## 344

This problem was asked by Adobe.

You are given a tree with an even number of nodes. Consider each connection between a parent and child node to be an "edge". You would like to remove some of these edges, such that the disconnected subtrees that remain each have an even number of nodes.

For example, suppose your input was the following tree:

```
   1
  / \
 2   3
    / \
   4   5
 / | \
6  7  8
```

In this case, removing the edge (3, 4) satisfies our requirement.

Write a function that returns the maximum number of edges you can remove while still satisfying this requirement.

## 349

This problem was asked by Grammarly.

Soundex is an algorithm used to categorize phonetically, such that two names that sound alike but are spelled differently have the same representation.

Soundex maps every name to a string consisting of one letter and three numbers, like M460.

One version of the algorithm is as follows:

* Remove consecutive consonants with the same sound (for example, change ck -> c).
* Keep the first letter. The remaining steps only apply to the rest of the string.
* Remove all vowels, including y, w, and h.
* Replace all consonants with the following digits:
 * b, f, p, v → 1
 * c, g, j, k, q, s, x, z → 2
 * d, t → 3
 * l → 4
 * m, n → 5
 * r → 6

If you don't have three numbers yet, append zeros until you do. Keep the first three numbers.

Using this scheme, Jackson and Jaxen both map to J250.

Implement Soundex.

## 351

This problem was asked by Quora.

Word sense disambiguation is the problem of determining which sense a word takes on in a particular setting, if that word has multiple meanings. For example, in the sentence "I went to get money from the bank", bank probably means the place where people deposit money, not the land beside a river or lake.

Suppose you are given a list of meanings for several words, formatted like so:

```
{
    "word_1": ["meaning one", "meaning two", ...],
    ...
    "word_n": ["meaning one", "meaning two", ...]
}
```

Given a sentence, most of whose words are contained in the meaning list above, create an algorithm that determines the likely sense of each possibly ambiguous word.

## 354

This problem was asked by Google.

Design a system to crawl and copy all of Wikipedia using a distributed network of machines.

More specifically, suppose your server has access to a set of client machines. Your client machines can execute code you have written to access Wikipedia pages, download and parse their data, and write the results to a database.

Some questions you may want to consider as part of your solution are:

* How will you reach as many pages as possible?
* How can you keep track of pages that have already been visited?
* How will you deal with your client machines being blacklisted?
* How can you update your database when Wikipedia pages are added or updated?

## 355

This problem was asked by Airbnb.

You are given an array X of floating-point numbers x1, x2, ... xn. These can be rounded up or down to create a corresponding array Y of integers y1, y2, ... yn.

Write an algorithm that finds an appropriate Y array with the following properties:

* The rounded sums of both arrays should be equal.
* The absolute pairwise difference between elements is minimized. In other words, |x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.
For example, suppose your input is [1.3, 2.3, 4.4]. In this case you cannot do better than [1, 2, 5], which has an absolute difference of |1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1.

## 356 (dup 488)

This problem was asked by Netflix.

Implement a queue using a set of fixed-length arrays.

The queue should support enqueue, dequeue, and get_size operations.

## 357

This problem was asked by LinkedIn.

You are given a binary tree in a peculiar string representation. Each node is written in the form `(lr)`, where `l` corresponds to the left child and `r` corresponds to the right child.

If either `l` or `r` is null, it will be represented as a zero. Otherwise, it will be represented by a new `(lr)` pair.

Here are a few examples:

* A root node with no children: `(00)`
* A root node with two children: `((00)(00))`
* An unbalanced tree with three consecutive left children: `((((00)0)0)0)`

Given this representation, determine the depth of the tree.

## 358

This problem was asked by Dropbox.

Create a data structure that performs all the following operations in `O(1)` time:

* `plus`: Add a key with value `1`. If the key already exists, increment its value by one.
* `minus`: Decrement the value of a key. If the key's value is currently `1`, remove it.
* `get_max`: Return a key with the highest value.
* `get_min`: Return a key with the lowest value.

## 365

This problem was asked by Google.

A quack is a data structure combining properties of both stacks and queues. It can be viewed as a list of elements written left to right such that three operations are possible:

* push(x): add a new item x to the left end of the list
* pop(): remove and return the item on the left end of the list
* pull(): remove the item on the right end of the list.

Implement a quack using three stacks and O(1) additional memory, so that the amortized time for any push, pop, or pull operation is O(1).

## 368

This problem was asked by Google.

Implement a key value store, where keys and values are integers, with the following methods:

* update(key, vl): updates the value at key to val, or sets it if doesn't exist
get(key): returns the value with key, or None if no such value exists
* max_key(val): returns the largest key with value val, or None if no key with that value exists
For example, if we ran the following calls:

```
kv.update(1, 1)
kv.update(2, 1)
```

And then called kv.max_key(1), it should return 2, since it's the largest key with value 1.

## 371

This problem was asked by Google.

You are given a series of arithmetic equations as a string, such as:
```
y = x + 1
5 = x + 3
10 = z + y + 2
```
The equations use addition only and are separated by newlines. Return a mapping of all variables to their values. If it's not possible, then return null. In this example, you should return:
```
{
  x: 2,
  y: 3,
  z: 5
}
```

## 377

This problem was asked by Microsoft.

Given an array of numbers arr and a window of size k, print out the median of each window of size k starting from the left and moving right by one position each time.

For example, given the following array and k = 3:
```
[-1, 5, 13, 8, 2, 3, 3, 1]
```
Your function should print out the following:
```
5 <- median of [-1, 5, 13]
8 <- median of [5, 13, 8]
8 <- median of [13, 8, 2]
3 <- median of [8, 2, 3]
3 <- median of [2, 3, 3]
3 <- median of [3, 3, 1]
```
Recall that the median of an even-sized list is the average of the two middle numbers.

## 391

This problem was asked by Facebook.

We have some historical clickstream data gathered from our site anonymously using cookies. The histories contain URLs that users have visited in chronological order.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appear in both.

For example, given the following two users' histories:

```
user1 = ['/home', '/register', '/login', '/user', '/one', '/two']
user2 = ['/home', '/red', '/login', '/user', '/one', '/pink']
```

You should return the following:

```
['/login', '/user', '/one']
```

## 392

This problem was asked by Google.

You are given a 2D matrix of 1s and 0s where 1 represents land and 0 represents water.

Grid cells are connected horizontally orvertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

An island is a group is cells connected horizontally or vertically, but not diagonally. There is guaranteed to be exactly one island in this grid, and the island doesn't have water inside that isn't connected to the water around the island. Each cell has a side length of 1.

Determine the perimeter of this island.

For example, given the following matrix:

```
[[0, 1, 1, 0],
[1, 1, 1, 0],
[0, 1, 1, 0],
[0, 0, 1, 0]]
```

Return 14.

## 396

This problem was asked by Google.

Given a string, return the length of the longest palindromic subsequence in the string.

For example, given the following string:

```
MAPTPTMTPA
```

Return 7, since the longest palindromic subsequence in the string is APTMTPA. Recall that a subsequence of a string does not have to be contiguous!

Your algorithm should run in O(n^2) time and space.

## 397

This problem was asked by Microsoft.

You are given a list of jobs to be done, where each job is represented by a start time and end time. Two jobs are compatible if they don't overlap. Find the largest subset of compatible jobs.

For example, given the following jobs (there is no guarantee that jobs will be sorted):

```
[(0, 6),
(1, 4),
(3, 5),
(3, 8),
(4, 7),
(5, 9),
(6, 10),
(8, 11)]
```

Return:

```
[(1, 4),
(4, 7),
(8, 11)]
```
## 398

This problem was asked by Amazon.

Given a linked list and an integer k, remove the k-th node from the end of the list and return the head of the list.

k is guaranteed to be smaller than the length of the list.

Do this in one pass.


## 400

This problem was asked by Goldman Sachs.

Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.

## 405

This problem was asked by Apple.

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.

## 406

This problem was asked by Quantcast.

You are presented with an array representing a Boolean expression. The elements are of two kinds:

* T and F, representing the values True and False.
* &, |, and ^, representing the bitwise operators for AND, OR, and XOR.

Determine the number of ways to group the array elements using parentheses so that the entire expression evaluates to True.

For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case, there are two acceptable groupings: (F | T) & T and F | (T & T).

## 409

This problem was asked by Google.

PageRank is an algorithm used by Google to rank the importance of different websites. While there have been changes over the years, the central idea is to assign each site a score based on the importance of other pages that link to that page.

More mathematically, suppose there are N sites, and each site i has a certain count C<sub>i</sub> of outgoing links. Then the score for a particular site S<sub>j</sub> is defined as :

`score(S<sub>j</sub>) = (1 - d) / N + d * (score(Sx) / Cx+ score(Sy) / Cy+ ... + score(Sz) / Cz))`

Here, Sx, Sy, ..., Sz denote the scores of all the other sites that have outgoing links to Sj, and d is a damping factor, usually set to around `0.85`, used to model the probability that a user will stop searching.

Given a directed graph of links between various websites, write a program that calculates each site's page rank.

## 410

This problem was asked by Airbnb.

You are given an array X of floating-point numbers x1, x2, ... xn. These can be rounded up or down to create a corresponding array Y of integers y1, y2, ... yn.

Write an algorithm that finds an appropriate Y array with the following properties:

* The rounded sums of both arrays should be equal.
* The absolute pairwise difference between elements is minimized. In other words, |x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.

For example, suppose your input is [1.3, 2.3, 4.4]. In this case you cannot do better than [1, 2, 5], which has an absolute difference of |1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1.

## 411

This problem was asked by Google.

Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.

## 413

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

## 414

This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

## 415

This problem was asked by Affirm.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock. You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you could buy the stock at 1 dollar, and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10 dollars. Since we did two transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.

## 425

This problem was asked by Oracle.

You are presented with an 8 by 8 matrix representing the positions of pieces on a chess board. The only pieces on the board are the black king and various white pieces. Given this matrix, determine whether the king is in check.

For details on how each piece moves, see [here](https://en.wikipedia.org/wiki/Chess_piece#Moves_of_the_pieces).

For example, given the following matrix:

```
...K....
........
.B......
......P.
.......R
..N.....
........
.....Q..
```

You should return `True`, since the bishop is attacking the king diagonally.

## 428

This problem was asked by Uber.

You have N stones in a row, and would like to create from them a pyramid. This pyramid should be constructed such that the height of each stone increases by one until reaching the tallest stone, after which the heights decrease by one. In addition, the start and end stones of the pyramid should each be one stone high.

You can change the height of any stone by paying a cost of 1 unit to lower its height by 1, as many times as necessary. Given this information, determine the lowest cost method to produce this pyramid.

For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is to pay 2 to create [0, 1, 2, 3, 2, 1].

## 430

This problem was asked by Facebook.

Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".

## 432

This problem was asked by Google.

Design a system to crawl and copy all of Wikipedia using a distributed network of machines.

More specifically, suppose your server has access to a set of client machines. Your client machines can execute code you have written to access Wikipedia pages, download and parse their data, and write the results to a database.

Some questions you may want to consider as part of your solution are:

- How will you reach as many pages as possible?
- How can you keep track of pages that have already been visited?
- How will you deal with your client machines being blacklisted?
- How can you update your database when Wikipedia pages are added or updated?

## 436

This problem was asked by Microsoft.

Implement 3 stacks using a single list:

```
class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass
```

## 442

This problem was asked by Netflix.

A Cartesian tree with sequence S is a binary tree defined by the following two properties:

- It is heap-ordered, so that each parent value is strictly less than that of its children.
- An in-order traversal of the tree produces nodes with values that correspond exactly to S.

For example, given the sequence `[3, 2, 6, 1, 9]`, the resulting Cartesian tree would be:

```
      1
    /   \
  2       9
 / \
3   6
```

Given a sequence `S`, construct the corresponding Cartesian tree.

## 444

This problem was asked by Dropbox.

Implement an efficient string matching algorithm.

That is, given a string of length `N` and a pattern of length `k`, write a program that searches for the pattern in the string with less than `O(N * k)` worst-case time complexity.

If the pattern is found, return the start index of its location. If not, return `False`.

## 448

This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

## 450

This problem was asked by Google.

You're given a string consisting solely of `(`, `)`, and `*`. `*` can represent either a `(`, `)`, or an empty string. Determine whether the parentheses are balanced.

For example, `(()*` and `(*)` are balanced. `)*(` is not balanced.

## 457

This problem was asked by Google.

Given a word `W` and a string `S`, find all starting indices in `S` which are anagrams of `W`.

For example, given that `W` is `"ab"`, and `S` is `"abxaba"`, return 0, 3, and 4.

## 458

This problem was asked by Uber.

A rule looks like this:

```
A NE B
```

This means this means point A is located northeast of point B.

```
A SW C
```

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

```
A N B
B NE C
C N A
```

does not validate, since A cannot be both north and south of C.

```
A NW B
A N B
```

is considered valid.

## 478

This problem was asked by Google.

Implement a file syncing algorithm for two computers over a low-bandwidth network. What if we know the files in the two computers are mostly the same?

## 485

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

## 545

This problem was asked by Twitter.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia [https://en.wikipedia.org/wiki/Lowest_common_ancestor]: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

## 564

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be `0` or negative.

For example, `[2, 4, 6, 2, 5]` should return `13`, since we pick `2`, `6`, and `5`. `[5, 1, 1, 5]` should return `10`, since we pick `5` and `5`.

Follow-up: Can you do this in O(N) time and constant space?

## 572

This problem was asked by Palantir.

Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?

## 590

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

## 599

This problem was asked by Two Sigma.

Ghost is a two-person word game where players alternate appending letters to a word. The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses. Here is a sample game:

-    Player 1: g
-    Player 2: h
-    Player 1: o
-    Player 2: s
-    Player 1: t [loses]

Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.

For example, if the dictionary is `["cat", "calf", "dog", "bear"]`, the only winning start letter would be `b`.

## 632

This problem was asked by VMware.

The skyline of a city is composed of several buildings of various widths and heights, possibly overlapping one another when viewed from a distance. We can represent the buildings using an array of (left, right, height) tuples, which tell us where on an imaginary x-axis a building begins and ends, and how tall it is. The skyline itself can be described by a list of (x, height) tuples, giving the locations at which the height visible to a distant observer changes, and each new height.

Given an array of buildings as described above, create a function that returns the skyline.

For example, suppose the input consists of the buildings [(0, 15, 3), (4, 11, 5), (19, 23, 4)]. In aggregate, these buildings would create a skyline that looks like the one below.

```
     ______
    |      |        ___
 ___|      |___    |   |
|   |   B  |   |   | C |
| A |      | A |   |   |
|   |      |   |   |   |
------------------------

```
As a result, your function should return [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)].

## 643

This problem was asked by YouTube.

Write a program that computes the length of the longest common subsequence of three given strings. For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious", it should return `5`, since the longest common subsequence is "eieio".

## 238

This problem was asked by MIT.

[Blackjack](https://en.wikipedia.org/wiki/Blackjack) is a two player card game whose rules are as follows:

*    The player and then the dealer are each given two cards.
*    The player can then "hit", or ask for arbitrarily many additional cards, so long as their total does not exceed 21.
*    The dealer must then hit if their total is 16 or lower, otherwise pass.
*    Finally, the two compare totals, and the one with the greatest sum not exceeding 21 is the winner.

For this problem, cards values are counted as follows: each card between 2 and 10 counts as their face value, face cards count as 10, and aces count as 1.

Given perfect knowledge of the sequence of cards in the deck, implement a blackjack solver that maximizes the player's score (that is, wins minus losses).

## 658

This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string `"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"` represents:

```
dir
    subdir1
    subdir2
        file.ext
```

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` represents:

```
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
```

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.

## 660

This problem was asked by Airbnb.

You come across a dictionary of sorted words in a language you've never seen before. Write a program that returns the correct order of letters in this language.

For example, given `['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']`, you should return `['x', 'z', 'w', 'y']`.


## 673

Given a list of points, a central point, and an integer `k`, find the nearest `k` points from the central point.

For example, given the list of points `[(0, 0), (5, 4), (3, 1)]`, the central point `(1, 2)`, and `k = 2`, return `[(0, 0), (3, 1)]`.

## 676

This problem was asked by LinkedIn.

Given a string, return whether it represents a number. Here are the different kinds of numbers:

*    "10", a positive integer
*    "-10", a negative integer
*    "10.1", a positive real number
*    "-10.1", a negative real number
*    "1e5", a number in scientific notation

And here are examples of non-numbers:

* "a"
* "x 1"
* "a -2"
* "-"

## 763

This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

* 10 = max(10, 5, 2)
* 7 = max(5, 2, 7)
* 8 = max(2, 7, 8)
* 8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.