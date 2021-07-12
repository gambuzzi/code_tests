# Easy questions

## Sum of numbers

Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.

For example, given `[10, 15, 3, 7]` and `k` of 17, return **true** since 10 + 7 is 17.

*Bonus: Can you do this in one pass?*

### brute solution

complexity: O(n<sup>2</sup>)

```python

def sol(arr, k):
    for i, a in enumerate(arr[:-1]):
        for b in arr[i+1:]:
            if a+b == k:
                return True
    return False

print(timeit.timeit("assert sol((1,3,42,19,10,7), 13)", setup="from __main__ import sol"))
```

timeit: 1.56883096695

### faster solution

complexity: O(n)

```python

def sol(arr, k):
    s = set()
    for a in arr:
        b = k-a
        if b in s:
            return True
        s.add(a)
    return False

print(timeit.timeit("assert sol((1,3,42,19,10,7), 13)", setup="from __main__ import sol"))
```

timeit: 1.35929107666

## Url shortner

Implement a URL shortener with the following methods:

- `shorten(url)`, which shortens the url into a six-character alphanumeric string, such as `zLg6wl`.
- `restore(short)`, which expands the shortened string into the original url. If no such shortened string exists, return `null`.

Hint: What if we enter the same URL twice?

### Discussion

First let's compute how many url can we short this way.
With figures like 'A..Za..z0..9', let's remove {i, I, l, L, o, O, 0, 1}, because is easy to misread them, we can have 56 figures

```python
cifer = 'abcdefghjklmnpqrstuvxywzABCDEFGHJKLMNPQRSTUVXYWZ23456789'

def tocode(n):
    ret  = ''
    for i in range(6):
        ret = cifer[n%len(cifer)] + ret
        n //= len(cifer)
    return ret


tocode(0)
# 'aaaaaa'

tocode(56**6-1)
# '999999'

```

So we can have 56<sup>6</sup> codes. 30_840_979_456 a little bit less than 31 billions.

Multiplying this by a resonable average of url lenght (64 bytes), we need to store 1_973_822_685_184 => 2 Petabytes of urls. We can't do this in memory so let's store it on an S3 like storage, our file will be called like the sorten version.

We must compute an hash of the url, distributed 0..30_840_979_455 and store the url in a file with name computed with the `tocode` function.

When we save the url, We check if the file is there. If not, we write it. DONE
  If we find already a file, we check the content. If it is equel, we are DONE
    If the content is differente we compute the next hash, with an evolving function. next = (hash + 4_405_854_209) % 30_840_979_456  (4_405_854_208 is a 7th of 30_840_979_456 )

Is very unprobable that we go back to the starting hash, but if this happen it means we run out of free space. We'll need 7 figures not 6. We are not taking this scenario in account.

```python
def my_hash(s):
    b = s.encode('utf-8')
    ret = 0
    for x in range(len(b)//8):
        ret <<= 4
        ret += struct.unpack('<Q', b[:8])[0]
        ret %= 30_840_979_456
        b = b[8:]
    ret <<= 4
    ret += struct.unpack('<Q', b + b'\x00' * (8-len(b)))[0]
    ret %= 30_840_979_456
    return ret

my_hash('https://www.google.com')
# 380_781_788

my_hash('https://www.google.com/?q=search')
# 19_750_499_088

```

We can also use MD5 or SHA256 from the core libraries of a lot of languages, just remeber to `% 30_840_979_456` the output

## 47

Given an array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

### Solution
Find the `min` and then the `max` after that min.

```python

def gain(stocks):
    _ptmin = _min = None
    for idx, stock in enumerate(stocks):
        if _min is None or stock < _min:
            _min = stock
            _ptmin = idx
    _max = max(stocks[_ptmin:])
    return _max-_min

```

## 63 Kids Game

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
For example, given the following matrix:
```
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
```
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.


### Solution
```python
def check(matrix, word):
    # left to right
    if word in [''.join(x) for x in matrix]:
        return True
    if word in [''.join(x[::-1]) for x in zip(*matrix[::-1])]:
        return True
    return False
```

`zip(*matrix[::-1])` is used to rotate the matrix

## 65 Spiral Print

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
For example, given the following matrix:

```
[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
```

You should print out the following:

```
1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
```

```python

while matrix:
    for x in matrix[0]:
        print(x)
    matrix = matrix[1:]
    if matrix:
        matrix = [x[::-1] for x in zip(*matrix[::-1])][::-1]  # matrix rotation

```

Print first row, rotate and go on, until run out of matrix

## 69 Product of numbers

Given a list of integers, return the largest product that can be made by multiplying any three integers.
For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
You can assume the list has at least three integers.

### Discussion
The idea is to sort the list.

If we have only positive numbers, or only negatives numbers, we take the biggest 3 numbers.

If we have at least 2 negative numbers, we computer their product and we compare it with the product of the biggest 2 positive numbers; if the product is bigger, we use them, else we don't.

At this point we multiply by the largest number of the list.

### Solution

```python

def largest_product(l):
    numbers = sorted(l)
    ret = numbers[-1]*numbers[-2]*numbers[-3]  # the input always contain at least 3 elements
    if all(x<0 for x in numbers):
        return ret
    if numbers[0]*numbers[1]*numbers[-1] > ret:  # test in the case we have 2 negatives number
        ret = numbers[0]*numbers[1]*numbers[-1]
    return ret
```

## Product of numbers

Given an array of integers, return a new array such that each element at index `i` of the new array is the product of all the numbers in the original array except the one at `i`. There are never zeros in the input array.

For example, if our input was `[1, 2, 3, 4, 5]`, the expected output would be `[120, 60, 40, 30, 24]`. If our input was `[3, 2, 1]`, the expected output would be `[2, 3, 6]`.

*Follow-up: what if you can't use division?*

### first solution

For first we compute the product of all the elements of the array.

```python
product = 1
for x in input_list:
    product *= x
```

now we create a new array with element the product divided by the element in the same position in the input_list

```python
result_list = [product / float(x) for x in input_list]
```

this works because of the properties of multiplicaion and divisions

#### note on python3

We could use `reduce` for the product of all the elements of an array in this way:

```python
product = reduce(lambda prev, curr: prev*curr, input_list, 1)
```

But in python3 `reduce` is no more a primitive statement, but you need to import it from the `functools` module, because the guide line is that a `for` loop is more readable.

### without the division.

if you cheat from the mathematically point of view you can do

```python
result_list = [product * (x**-1) for x in input_list]
```

but probably this is not what the interviewer wants.

We can compute 2 lists, one with the product from the start of the list upto the current element, and another in the same way, but reversing the input_list before. So after this we do:

```python
p = 1
prod_array = []
for x in input_list:
    prod_array.append(p)
    p *= x

p = 1
prod_reverse_array = []
for x in input_list[::-1]:
    prod_reverse_array.append(p)
    p *= x
```

and we get

```python
prod_array == [1, 1, 2, 6, 24]
prod_reverse_array[::-1] == [120, 60, 20, 5, 1]
```

if we zip together the 2 lists multipling, we get

```python
result = [x*y for x,y in zip(prod_array, prod_reverse_array[::-1])]
```

#### all the code together

```python
def solution(input_list):
    p = 1
    prod_array = []
    for x in input_list:
        prod_array.append(p)
        p *= x

    p = 1
    prod_reverse_array = []
    for x in input_list[::-1]:
        prod_reverse_array.append(p)
        p *= x

    result = [x*y for x,y in zip(prod_array, prod_reverse_array[::-1])]
    return result
```

## Operation tree

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '-', '*', or '/'.
Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:

```
    *
   / \
  +    +
 / \  / \
3  2  4  5
```

You should return 45, as it is `(3 + 2) * (4 + 5)`.

### Solution 

Given the tree as a list
['*', '+', '+', 3, 2, 4, 5]

```python
tree = ['*', '+', '+', 3, 2, 4, 5]

def walk(tree, p):
    if p<len(tree) and tree[p] is not None:
        yield from walk(tree,p*2+1)  # left
        yield from walk(tree,p*2+2)  # right
        yield tree[p]

>>> list(walk(tree,0))

 [3, 2, '+', 4, 5, '+', '*']

```

now we have the RPN of our tree, that we evaluate with a stack

```python
from collections import deque

def compute(l):
    ops = {
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '/': lambda a,b: a/b,
    }
    stack = deque()
    for c in l:
        ret = c
        if c in ops:
            b = stack.pop()
            a = stack.pop()
            ret = ops[c](a,b)
        stack.append(ret)

    return stack.pop()

>>> compute(walk(tree,0))

45

```

## 73

This problem was asked by Google.
Given the head of a singly linked list, reverse it in-place.

```python
def reverse(node, prev_node = None):
    if node:
        next_node = node.next
        node.next = prev_node
        reverse(next_node, node)
```

## 71

This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability.

### Simple solution
```python
def rand5():
    ret = 7
    while ret>5:
        ret = rand7()
    return ret
```

### Math solution

Imagine a matrix 7 by 7, we can think of it as an array of 49 elements, that is linear.
We chose a cell with uniform probability using rand7.
then we have to take this number 0..48 and do modulo 5.
But we have to discard the tail of the array, because this would make the probability not uniform anymore.
So we keep 0..44 and we 'roll again' is we get a number bigger than 44.

```python
def rand5():
    idx = 48
    while idx>44:
        idx = rand7()*7+rand7()
    return 1+(idx%5)
```

## 71 reverse

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability.

```python
def rand7():
    idx = 24
    while idx>20:
        idx = rand5()*5+rand5()
    return 1+(idx%7)
```
 
## 70

This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

### Note
The biggest perfect number is 11_111_111_110

### Solution
```python
def perferct_number(end):
    n = 1
    while n<=1_111_111_111:
        m=n
        _sum=0
        while m:
            _sum+=m%10
            m//=10
        last = 10-_sum
        if 0<=last<10:
            end-=1
            if end == 0:
                return n*10+last
        n+=1
```

## 72 hard

This problem was asked by Google.
In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.
Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.
The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.
For example, the following input graph:
ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).
The following input graph:
A
[(0, 0)]
Should return null, since we have an infinite loop.

## 45

This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

```python
def fx(s):
    start=0
    l=2
    ret=""
    while start+l<=len(s):
        rev = s[start+l-1:start-1:-1]
        if start==0:
            rev = s[l-1::-1]
        if s[start:start+l] == rev and l>len(ret):
            ret = s[start:start+l]
        l += 1
        if start+l>len(s):
            start+=1
            l=2
    return ret
```

##  44

This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.


## 43

This problem was asked by Amazon.

Implement a stack that has the following methods:

* `push(val)`, which pushes an element onto the stack
* `pop()`, which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return `null`.
* `max()`, which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.

## 42 hard?

This problem was asked by Google.
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

## 41

This problem was asked by Facebook.
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.
Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

## 40

This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
Do this in O(N) time and O(1) space.

## 39

This problem was asked by Dropbox.
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:
Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.
You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

## 38

This problem was asked by Microsoft.
You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

## 37

This problem was asked by Google.
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set.

## 36 - duplciate 484 medium

This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.

## 35

This problem was asked by Google.
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.
Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

## 34

This problem was asked by Quora.
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
As another example, given the string "google", you should return "elgoogle".

## 33

This problem was asked by Microsoft.
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2

## 32

This problem was asked by Jane Street.
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.
There are no transaction costs and you can trade fractional quantities.

## 31

This problem was asked by Google.
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Given two strings, compute the edit distance between them.

## 30
This problem was asked by Facebook.
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

## 29

This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

## 28

This problem was asked by Palantir.
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k.
For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

## 27

This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.

## 25

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

- `.` (period) which matches any single character
- `*` (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

## 24

This problem was asked by Google.
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
Design a binary tree node class with the following methods:
is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

## 23

Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
For example, given the following board:

```python
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
```

and start = `(3, 0)` (bottom left) and end = `(0, 0)` (top left), the minimum number of steps required to reach the end is 7, since we would need to go through `(1, 2)` because there is a wall everywhere else on the second row.

## 22 - 480 medium

This problem was asked by Microsoft.
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

## 21

This problem was asked by Snapchat.
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

## How to Pick a Random Element from an Infinite Stream

Hope your interview practicing is going well! Let's work through the problem of uniformly picking a random element from a gigantic stream. This is a common interview question at companies like Google and Facebook.
Naively, we could process the stream and store all the elements we encounter in a list, find its size, and pick a random element from [0, size - 1]. The problem with this approach is that it would take O(N) space for a large N.
Instead, let's attempt to solve using loop invariants. On the ith iteration of our loop to pick a random element, let's assume we already picked an element uniformly from [0, i - 1]. In order to maintain the loop invariant, we would need to pick the ith element as the new random element at 1 / (i + 1) chance. For the base case where i = 0, let's say the random element is the first one. Then we know it works because
For i = 0, we would've picked uniformly from [0, 0].
For i > 0, before the loop began, any element K in [0, i - 1] had 1 / i chance of being chosen as the random element. We want K to have 1 / (i + 1) chance of being chosen after the iteration. This is the case since the chance of having being chosen already but not getting swapped with the ith element is 1 / i * (1 - (1 / (i + 1))) which is 1 / i * i / (i + 1) or 1 / (i + 1)
Let's see how the code would look:
import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element
Since we are only storing a single variable, this only takes up constant space!
Turns out this algorithm is called Reservoir Sampling. If you liked this problem and solution, sign up for our mailing list below for problems like these! You can also read our other post on how to solve tricky interview questions like this one here.
Best of luck!
Marc
If you liked this guide, feel free to forward it along! As always, shoot us an email if there's anything we can help with!

== 77

This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

== 80

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
    a
   / \
  b   c
 /
d

== 81

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

## 82

This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content `“Hello world”`, three `read7()` returns
`“Hello w”, “orld”` and then `“”`.

## 91

This problem was asked by Dropbox.

What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

```python
functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
```

## 94

This problem was asked by Google.
Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least one node, and does not need to go through the root.

## 98

This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:
```python
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```

exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.

### Solution

```python
def recursive_solution(grid, x, y, used, word):
    if word == '':
        return True
    first_letter = word[0]

    for dx, dy in ((0,1),(1,0),(-1,0),(0,-1)):
        nx = x + dx
        ny = y + dy
        if nx<0 or ny<0 or nx>len(grid[0])-1 or ny>len(grid)-1 or (nx,ny) in used:
            continue

        if grid[ny][nx] == first_letter:
            ret = recursive_solution(grid, nx, ny, used | {(nx,ny)}, word[1:])
            if ret:
                return True
    return False


def exists(grid, word):
    if word == '':
        return False
    first_letter = word[0]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell==first_letter:
                ret = recursive_solution(grid, x, y, {(x,y)}, word[1:])
                if ret:
                    return True
    return False

def stack_exists(grid, word):
    if word == '':
        return False
    first_letter = word[0]
    stack = []  # here a deque would be better
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell==first_letter:
                stack.append((x, y, {(x,y)}, word[1:]))
    while stack:
        x, y, used, w = stack.pop()
        if w == '':
            return True
        first_letter = w[0]

        for dx, dy in ((0,1),(1,0),(-1,0),(0,-1)):
            nx = x + dx
            ny = y + dy
            if nx<0 or ny<0 or nx>len(grid[0])-1 or ny>len(grid)-1 or (nx,ny) in used:
                continue

            if grid[ny][nx] == first_letter:
                stack.append((nx, ny, used | {(nx,ny)}, w[1:]))

    return False


assert (
    solution(
        [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E'],
        ],
        'ABCB'
    )
)==False

assert (
    solution(
        [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E'],
        ],
        'ABCCED'
    )
)==True

assert (
    solution(
        [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E'],
        ],
        'ABCESEEDASFC'
    )
)==True

assert (
    stack_solution(
        [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E'],
        ],
        'ABCB'
    )
)==False

assert (
    stack_solution(
        [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E'],
        ],
        'ABCCED'
    )
)==True

assert (
    stack_solution(
        [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E'],
        ],
        'ABCESEEDASFC'
    )
)==True
```

## 100

This problem was asked by Google.
You are in an infinite 2D grid where you can move in any of the 8 directions:
 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.
Example:
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

## 101

This problem was asked by Alibaba.
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
A solution will always exist. See Goldbach’s conjecture.
Example:
Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
[a, b] < [c, d]
If a < c OR a==c AND b < d.

## 108

This problem was asked by Google.
Given two strings A and B, return whether or not A can be shifted some number of times to get B.
For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.

## 107

This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print `1, 2, 3, 4, 5`.

```
  1
 / \
2   3
   / \
  4   5
```

## 104

This problem was asked by Google.
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?
For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.

## 117

This problem was asked by Facebook.
Given a binary tree, return the level of the tree with minimum sum.

## 118

This problem was asked by Google.
Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

## 124

This problem was asked by Microsoft.
You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?
Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.

## 125

This problem was asked by Google.
Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.
For example, given the following tree and K of 20
    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.

```python

tree = [10, 5, 15, None, None, 11, 15]

dict_tree = {}
for i, x in enumerate(tree):
    if x is not None:
        dict_tree[i] = x

dict_tree = { i:x for i, x in enumerate(tree) if x is not None }

def search(dict_tree, n, skip):
    ptr = 0
    while ptr in dict_tree:
        if dict_tree[ptr]==n and ptr!=skip:
            return ptr
        if dict_tree[ptr]>n:
            ptr = ptr*2 + 1  # left
        else:
            ptr = ptr*2 + 2  # right
    return None

def solve(tree, k):
    dict_tree = { i:x for i, x in enumerate(tree) if x is not None }

    for p1, value in dict_tree.items():
        p2 = search(dict_tree, k-value, p1)
        if p2 is not None:
            return value, k-value, p1, p2

    return None, None, None, None

```

COMPLEXITY: O( n lg(n) )
SPACE: the new map O (n)

ANTOTHER WAY

```python
tree = [10, 5, 15, None, None, 11, 15]

def search(tree, n, skip):
    ptr = 0
    while ptr < len(tree) and tree[ptr] is not None:
        if tree[ptr]==n and ptr!=skip:
            return ptr
        if tree[ptr]>n:
            ptr = ptr*2 + 1  # left
        else:
            ptr = ptr*2 + 2  # right
    return None

def solve(tree, k):
    for p1, value in enumerate(tree):
        if value is None:
            continue
        p2 = search(tree, k-value, p1)
        if p2 is not None:
            return value, k-value, p1, p2

    return None, None, None, None

```

COMPLEXITY: O( n lg(n) )
SPACE: no additional memory needed

ANTOTHER WAY

```python

def solve(tree, k):
    from collections import defaultdict
    dict_tree = defaultdict(list)
    for i, x in enumerate(tree):
        if x is not None:
            dict_tree[x].append(i)

    for key1 in dict_tree:
        key2 = k-key1
        if key2==key1 and len(dict_tree[key1])>1:
            return key1, key2, dict_tree[key1][0], dict_tree[key1][1]
        if key2 in dict_tree:
            return key1, key2, dict_tree[key1][0], dict_tree[key2][0]
```

COMPLEXITY: O( n ) if no collisions
WORSE O ( n^2 )

## 127

This problem was asked by Microsoft.
Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.
For example, the following linked list:
1 -> 2 -> 3 -> 4 -> 5
is the number 54321.
Given two linked lists in this format, return their sum in the same linked list format.
For example, given
9 -> 9
5 -> 2
return 124 (99 + 25) as:
4 -> 2 -> 1

## 132

This question was asked by Riot Games.
Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:
record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
Follow-up: What if our system has limited memory?

## 134

This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, `SparseArray`, that implements the same interface:

- `init(arr, size)`: initialize with the original large array and size.
- `set(i, val)`: updates index at i with val.
- `get(i)`: gets the value at index i.

## 135

This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is `[10, 5, 1, -1]`, which has sum `15`.

```
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
```

## 145

This problem was asked by Google.
Given the head of a singly linked list, swap every two nodes and return its head.
For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

## 154

This problem was asked by Amazon.
Implement a stack API using only a heap. A stack implements the following methods:
push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:
push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap

## 157

This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, `carrace` should return true, since it can be rearranged to form `racecar`, which is a palindrome. `daily` should return `false`, since there's no rearrangement that can form a palindrome.


## 159

Given a string, return the first recurring character in it, or null if there is no recurring character.
For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

### Solution

```python

def solution(string):
    seen = set()
    for c in string:
        if c in seen:
             return c
        seen.add(c)
    return None

```

## 161

This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number
```
1111 0000 1111 0000 1111 0000 1111 0000
```

return

```
0000 1111 0000 1111 0000 1111 0000 1111
```

## 171

You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:
{"timestamp": 1526579928, count: 3, "type": "enter"}
This means 3 people entered the building. An exit looks like this:
{"timestamp": 1526580382, count: 2, "type": "exit"}
This means that 2 people exited the building. timestamp is in Unix time.
Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.

## 170 medium

This problem was asked by Facebook.

Given a `start` word, an `end` word, and a dictionary of valid words, find the shortest transformation sequence from `start` to `end` such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same length as `start` and `end` and is lowercase.

For example, given `start = "dog"`, `end = "cat"`, and `dictionary = {"dot", "dop", "dat", "cat"}`, return `["dog", "dot", "dat", "cat"]`.

Given `start = "dog"`, `end = "cat"`, and `dictionary = {"dot", "tod", "dat", "dar"}`, return `null` as there is no possible transformation from `dog` to `cat`

## 173

This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:
```python
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
```

it should become:

```python
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
```

### Solution (Python)

```python
def flat(d):
    ret = {}
    for k,v in d.items():
        if type(v)==dict:
            for k2,v2 in flat(v).items():
                ret[k+'.'+k2] = v2
        else:
            ret[k]=v
    return ret
```

#### Better solution ?

```
def flat(d):
    ret = {}
    for k,v in d.items():
        try:
            elem = flat(v)
            for k2 in elem:
                ret[k+'.'+k2] = elem[k2]
        except AttributeError:
            ret[k]=v
    return ret
```

You can assume keys do not contain dots in them, i.e. no clobbering will occur.

## 175

This problem was asked by Google.

You are given a starting state `start`, a list of transition probabilities for a Markov chain, and a number of steps `num_steps`. Run the Markov chain starting from `start` for `num_steps` and compute the number of times we visited each state.

For example, given the starting state `a`, number of steps 5000, and the following transition probabilities:
```
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
```
One instance of running this Markov chain might produce `{ 'a': 3012, 'b': 1656, 'c': 332 }`.

## 176

This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.


## 177

This problem was asked by Airbnb.
Given a linked list and a positive integer k, rotate the list to the right by k places.
For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.
Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.

## 191

This problem was asked by Stripe.

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.

## 189 (dup 489)

This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where all its elements are distinct.

For example, given the array `[5, 1, 3, 5, 2, 3, 4, 1]`, return 5 as the longest subarray of distinct elements is `[5, 2, 3, 4, 1]`.

## 187

This problem was asked by Google.
You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.
For example, given the following rectangles:
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.

## 194

This problem was asked by Facebook.
Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.

## 196

This problem was asked by Apple.
Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.
For example, given the following tree:
  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.

## 197

This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.

## 201

This problem was asked by Google.
You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.
Write a program that returns the weight of the maximum weight path.

## 202 (dup 491)

This problem was asked by Palantir.
Write a program that checks whether an integer is a palindrome. For example, `121` is a palindrome, as well as `888`. `678` is not a palindrome. Do not convert the integer into a string.

## 204

This problem was asked by Amazon.

Given a complete binary tree, count the number of nodes in faster than O(n) time. Recall that a complete binary tree has every level filled except the last, and the nodes in the last level are filled starting from the left.

## 205

This problem was asked by IBM.

Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.

## 206

This problem was asked by Twitter.
A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.
Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].

## 210

This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

- if n is even, the next number in the sequence is `n / 2`
- if n is odd, the next number in the sequence is `3n + 1`

It is conjectured that every such sequence eventually reaches the number `1`. Test this conjecture.

Bonus: What input `n <= 1000000` gives the longest sequence?

## 212

This problem was asked by Dropbox.
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".

## 214

This problem was asked by Stripe.
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.
For example, given 156, you should return 3.

## 221

This problem was asked by Zillow.
Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.

## 224

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input `[1, 2, 3, 10]`, you should return `7`.

Do this in `O(N)` time.

## 225 - duplicate 483

This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.


## 227

This problem was asked by Facebook.

Boggle is a game played on a 4 x 4 grid of letters. The goal is to find as many words as possible that can be formed by a sequence of adjacent letters in the grid, using each cell at most once. Given a game board and a dictionary of valid words, implement a Boggle solver.

## 231

This problem was asked by IBM.

Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. If this is not possible, return `None`.

For example, given `"aaabbc"`, you could return `"ababac"`. Given `"aaab"`, return `None`.

## 232

This problem was asked by Google.

Implement a `PrefixMapSum` class with the following * methods:

* `insert(key: str, value: int)`: Set a given key's value in the map. If the key already exists, overwrite the value.
* `sum(prefix: str)`: Return the sum of all values of keys that begin with a given prefix.

For example, you should be able to run the following code:

```python
mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
```

## 233

This problem was asked by Apple.
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.

## 247

This problem was asked by PayPal.

Given a binary tree, determine whether or not it is height-balanced. A height-balanced binary tree can be defined as one in which the heights of the two subtrees of any node never differ by more than one.

## 244

This problem was asked by Square.
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.
For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.
Implement this algorithm.
Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).

## 237

This problem was asked by Amazon.
A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. The following tree is an example:
        4
      / | \
    3   5   3
  /           \
9              9
Given a k-ary tree, determine whether it is symmetric.

## 241

This problem was asked by Palantir.
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:
A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.
For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.
Given a list of paper citations of a researcher, calculate their h-index.

## 252

This problem was asked by Palantir.
The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.
Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.

## 255

This problem was asked by Microsoft.
The transitive closure of a graph is a measure of which vertices are reachable from other vertices. It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.
For example, suppose we are given the following graph in adjacency list form:
graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
The transitive closure of this graph would be:
[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Given a graph, find its transitive closure.

## 273

This problem was asked by Apple.
A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.
For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.

## 269

This problem was asked by Microsoft.
You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

* L, meaning the domino has just been pushed to the left,
* R, meaning the domino has just been pushed to the right, or
* ., meaning the domino is standing still.

Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.
For example, given the string `.L.R....L`, you should return `LL.RRRLLL`.
Given the string `..R...L.L`, you should return `..RR.LLLL`.

## 266

This problem was asked by Pivotal.

A step word is formed by taking a given word, adding a letter, and anagramming the result. For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns all valid step words.

## 265

This problem was asked by Atlassian.
MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.
Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.
For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].

## 261

This problem was asked by Amazon.
Huffman coding is a method of encoding characters based on their frequency. Each letter is assigned a variable-length binary string, such as 0101 or 111110, where shorter lengths correspond to more common letters. To accomplish this, a binary tree is built such that the path from the root to any leaf uniquely maps to a character. When traversing the path, descending to a left child corresponds to a 0 in the prefix, while descending right corresponds to 1.
Here is an example tree (note that only the leaf nodes have letters):
        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.
Given a dictionary of character frequencies, build a Huffman tree, and use it to determine a mapping between characters and their encoded binary strings.

## 258

 Daily Coding Problem
Good morning! Here's your coding interview problem for today.
This problem was asked by Morgan Stanley.
In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".
Given a binary tree, write an algorithm to print the nodes in boustrophedon order.
For example, given the following tree:
       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].

## 277

This problem was asked by Google.
UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.
For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:
For a single-byte character, the first bit must be zero.
For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.
Visually, this can be represented as follows.
 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Write a program that takes in an array of integers representing byte values, and returns whether it is a valid UTF-8 encoding.

## 278

This problem was asked by Amazon.
Given an integer N, construct all possible binary search trees with N nodes.

## 282

This problem was asked by Netflix.
Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a^2+ b^2= c^2.

## 279

This problem was asked by Twitter.

A classroom consists of `N` students, whose friendships can be represented in an adjacency list. For example, the following descibes a situation where `0` is friends with `1` and `2`, `3` is friends with `6`, and so on.

```python
{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]}
```

Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group. For the example above, the friend groups would be `{0, 1, 2, 5}`, `{3, 6}`, `{4}`.

Given a friendship list such as the one above, determine the number of friend groups in the class.

### Solution

```python

_input = {0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]}
 
sets = {}
ret = []
 
for k,v in _input.items():
    if k not in sets:
        s = set([k]+v)
        sets[k] = s
        for vv in v:
            sets[vv] = s
        ret.append(s)
    else:
        for vv in v:
            sets[k].add(vv)
            sets[vv] = sets[k]

print(sets)
print(ret)

```

and the output will be

```python
{0: {0, 1, 2, 5}, 1: {0, 1, 2, 5}, 2: {0, 1, 2, 5}, 5: {0, 1, 2, 5}, 3: {3, 6}, 6: {3, 6}, 4: {4}}
[{0, 1, 2, 5}, {3, 6}, {4}]
```

## 283

This problem was asked by Google.
A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.
These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.
Given an integer N, write a program that returns, in order, the first N regular numbers.


## 290

On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

|        Arrangement       |   Change |
|--------------------------|-------------|
| ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B |
| ['B', 'B', 'G', 'B']      | (B, G) -> R |
| ['B', 'R', 'B']           | (R, B) -> G |
| ['B', 'G']                | (B, G) -> R |
| ['R']                     | |

### Solution

```python
from collections import deque

_input = ['R', 'G', 'B', 'G', 'B']

def son(a,b):
    return {
        frozenset(('R','G')) : 'B',
        frozenset(('R','B')) : 'G',
        frozenset(('B','G')) : 'R',
    }[frozenset((a,b))]

def solution(_input):
    stack = deque([_input])
    while stack:
        sol = stack.pop()
        final = True
        for i,(a,b) in enumerate(zip(sol,sol[1:])):
            if a!=b:
                stack.append(sol[:i]+[son(a,b)]+sol[i+2:])
                final = False
        if final:
            yield sol
            
print (min(solution(_input), key=len))

```

## 298

This problem was asked by Google.

A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input `[2, 1, 2, 3, 3, 1, 3, 5]`, the longest portion will involve types 1 and 3, with a length of four.

### Solution

```python
_input = [2, 1, 2, 3, 3, 1, 3, 5]

def solution(_input):
    sets = [set() for _ in range(len(_input)+1)]
    for i, x in enumerate(_input+[None]):
        for j in range(i+1):
            try:
                sets[j].add(x)
            except AttributeError:
                continue
            if len(sets[j])>2:
                yield i-j
                sets[j] = None
                
print(max(solution(_input)))
```

## 300

This problem was asked by Uber.

On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file.

Write a program that reads this file as a stream and returns the top 3 candidates at any given time. If you find a voter voting more than once, report this as fraud.

### Solution 1 

```python
from collections import Counter

_input = [
 #   (voter_id, candidate_id)
 (1, 3),
 (2, 3),
 (3, 1),
 (4, 1),
 (1, 2),
 (5, 2),
 (6, 4),
 (7, 3),
 (11, 3),
 (12, 3),
 (13, 1),
 (14, 1),
 (111, 4),
 (15, 4),
 (16, 4),
 (17, 4),
 (18, 4), 
 (19, 5),
]

def solution(_input):
    voters = set()
    top3 = Counter()
    for voter_id, candidate_id in _input:
        if voter_id in voters:
            print(f"Fruad! {voter_id=},{candidate_id=}")
            continue
        voters.add(voter_id)
        top3[candidate_id] += 1
        yield [x[0] for x in top3.most_common(3)]

for x in solution(_input):
    print(x)
```

### Solution 2

Without the use of the `Counter` class.

```python
_input = [
 #   (voter_id, candidate_id)
 (1, 3), (2, 3), (3, 1), (4, 1), (1, 2), (5, 1), (6, 4), (7, 3), (11, 3), (12, 3), (13, 1),
 (14, 1), (111, 4), (15, 4), (16, 4), (17, 4), (18, 4), (19, 5),
]

class Top3:
    def __init__(self):
        self._cnt = dict()  # count the votes
        self._seq = list()  # the list of the candidates, sorted by votes
        self._positions = dict()  # the position of a candidate in the self._seq list
        
    def increment(self, k):   
        if k not in self._cnt:
            self._cnt[k] = 0
        self._cnt[k] += 1
        votes = self._cnt[k]
        
        if k not in self._positions:
            self._seq.append([k, votes])
            self._positions[k] = len(self._seq)-1
        ptr = self._positions[k]
        self._seq[ptr][1] = votes
        
        new_ptr = ptr
        while new_ptr>0 and votes>self._seq[new_ptr-1][1]:  # linear search of the new position based on the new vote count. Yes, it is linear, but the counter is just incrementing by 1 so it can only move in the direction of the head of the list and cant jump 'a lot'
            new_ptr -= 1
        self._seq[new_ptr], self._seq[ptr] = self._seq[ptr], self._seq[new_ptr]
        self._positions[k] = new_ptr
        self._positions[self._seq[ptr][0]] = ptr
    
    def most_common(self):
        return self._seq[:3]
        
    
def solution(_input):
    voters = set()
    top3 = Top3()
    for voter_id, candidate_id in _input:
        if voter_id in voters:
            print(f"Fruad! {voter_id=},{candidate_id=}")
            continue
        voters.add(voter_id)
        top3.increment(candidate_id)
        yield top3.most_common()

for x in solution(_input):
    print(x)

```

## 303

This problem was asked by Microsoft.

Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?

### Solution

Some math

``` 
hours_degree = 360/12 * hours + 360/12/60 * minutes
minutes_degree = 360/60 * minutes
```
The hours hand rotate by 30 degrees every hour plus half a degree for every minute of the hour
The minutes hand rotate by 6 degrees every minute

The angle is the absolute difference between the two.

```python
solution = abs(hours_degree - minutes_degree)  # remember to truncate to the nearest integer
```

#### Bonus

We have to solve the equations:

```
30 * h + 0.5 * m = 6 * m

30 * h = 5.5 * m

m = 30 / 5.5 * h
```

this is true for 

| h | m |
| -- | -- |
| 0 | 0 |
| 1 | 5.45 |
| 2 | 10.9 |
| 3 | 16.36 |
| 4 | 21.81 |
| 5 | 27.27 |
| 6 | 32.73 |
| 7 | 38.18 |
| 8 | 43.64 |
| 9 | 49.09 |
| 10 | 54.55 |
| 11 | no solution |

## 305

This problem was asked by Amazon.

Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

### Solution

```python
class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next
        
    def __str__(self):
        return "Node({},{})".format(self.value, self.next)
        
def generate_linkedlist(s):
    start = ptr = None
    for v in s.split(' -> '):
        n = Node(int(v))
        if start is None:
            start = n
        if ptr is not None:
            ptr.next = n
        ptr = n
    return start


def sol(linkedlist):
    if linkedlist is None:
        return None
    ptr = linkedlist
    _sum = 0
    while ptr:
        _sum += ptr.value
        if _sum==0:
            return sol(ptr.next)
        ptr = ptr.next
    linkedlist.next = sol(linkedlist.next)
    return linkedlist
    
linkedlist = generate_linkedlist("3 -> 4 -> -7 -> 5 -> -6 -> 6")
print (linkedlist)
print (sol(linkedlist))
```

## 307

This problem was asked by Oracle.
Given a binary search tree, find the floor and ceiling of a given integer. The floor is the highest element in the tree less than or equal to an integer, while the ceiling is the lowest element in the tree greater than or equal to an integer.
If either value does not exist, return None.

## 310

This problem was asked by Pivotal.
Write an algorithm that finds the total number of set bits in all integers between 1 and N.

## 311

This problem was asked by Sumo Logic.

Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that the first and last elements are lower than all others.

## 312

You are given a 2 x N board, and instructed to completely cover the board with the following shapes:
Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.
For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.
A B B C
A B C C
Given an integer N, determine in how many ways this task is possible.

## 315

This problem was asked by Google.

In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:

```
1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
```

Write a program to determine whether a given input is a Toeplitz matrix.

## 321

This problem was asked by PagerDuty.
Given a positive integer N, find the smallest number of steps it will take to reach 1.
There are two kinds of permitted steps:
You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

## 324

This problem was asked by Amazon.
Consider the following scenario: there are N mice and N holes placed at integer points along a line. Given this, find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.
Each move consists of moving one mouse one unit to the left or right, and only one mouse can fit inside each hole.
For example, suppose the mice are positioned at [1, 4, 9, 15], and the holes are located at [10, -5, 0, 16]. In this case, the best pairing would require us to send the mouse at 1 to the hole at -5, so our function should return 6.

## 325

This problem was asked by Jane Street.
The United States uses the imperial system of weights and measures, which means that there are many different, seemingly arbitrary units to measure distance. There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.
Create a data structure that can efficiently convert a certain quantity of one unit to the correct amount of any other unit. You should also allow for additional units to be added to the system.

## 327

This problem was asked by Salesforce.

Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.

## 332

This problem was asked by Jane Street.

Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

a + b = M
a XOR b = N

```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<pair<int,int>> solve(int m, int n) {
    vector<pair<int,int>> ret;
    for (int i=0; i<m/2; i++) {
        if (((m-i) ^ i) == n) {
            ret.push_back(make_pair(i,m-i));
        }
    }
    return ret;
}

int main()
{
    cout << "solve(705, 573)" << endl;

    auto res = solve(705, 573);
    cout << res.size() << " solutions" << endl;

    for (auto x = res.begin(); x != res.end();) {
        cout << x->first << "," << x->second;
        x++;
        if (res.end() != x) { cout << " - "; }
    }
    cout << endl;
    return 0;
}
```

## 334

This problem was asked by Twitter.

The 24 game is played as follows. You are given a list of four integers, each between 1 and 9, in a fixed order. By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses, determine whether it is possible to reach the value 24.

For example, given the input [5, 2, 7, 8], you should return True, since (5 * 2 - 7) * 8 = 24.

Write a function that plays the 24 game.

```cpp

#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

pair<int, string> compute(int a, int b, int c, int d, int seq) {
    stringstream ss;
    int op[] = {
        (seq>>5) & 15,
        (seq>>2) & 7,
        (seq) & 3,
    };

    for (auto o: op) {
        switch(o) {
            case 0: a=a+b; b=c; c=d;
                ss << "a+b ";
                break;
            case 1: a=a-b; b=c; c=d;
                ss << "a-b ";
                break;
            case 2: a=a*b; b=c; c=d;
                ss << "a*b ";
                break;
            case 3: if (b==0) {throw "divison by 0";}; a=a/b; b=c; c=d;
                ss << "a/b ";
                break;
            case 4: b=b+c; c=d;
                ss << "b+c ";
                break;
            case 5: b=b-c; c=d;
                ss << "b-c ";
                break;
            case 6: b=b*c; c=d;
                ss << "b*c ";
                break;
            case 7: if (c==0) {throw "divison by 0";}; b=b/c; c=d;
                ss << "b/c ";
                break;
            case 8: c=c+d;
                ss << "c+d ";
                break;
            case 9: c=c-d;
                ss << "c-d ";
                break;
            case 10: c=c*d;
                ss << "c*d ";
                break;
            case 11: if (d==0) {throw "divison by 0";}; c=c/d;
                ss << "c/d ";
                break;
            default:
                break;
        }

    }
    ss << seq << " end";
    string sss = ss.str();
    return make_pair(a, sss);
}

vector<string> solve(int a, int b, int c, int d) {
    vector<string> ret;
    int seq = 0;
    pair<int, string> res;
    while (seq <= 0x1ff) {
        try{
            res = compute(a,b,c,d,seq);
        } catch (const char* msg) {
        //    cerr << msg << endl;
            seq++;
            continue;
        }
        if (res.first == 24) {
            ret.push_back(res.second);
        }
        seq++;
    }
    return ret;
}

int main()
{
    cout << "solve(5,2,7,8)" << endl;

    for (auto x: solve(5,2,7,8)) {
        cout << x << endl;
    }
    return 0;
}
```

## 340

This problem was asked by Google.

Given a set of points (x, y) on a 2D cartesian plane, find the two closest points.

For example, given the points `[(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)`], return `[(-1, -1), (1, 1)]`.

```python
def dist(a,b):
    x1, y1 = a
    x2, y2 = b
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

points = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]
print ( min(
  (dist(a,b),a,b) for a in points for b in points if a != b
) )
```

## 341

This problem was asked by Google.

You are given an N by N matrix of random letters and a dictionary of words.

Find the maximum number of words that can be packed on the board from the given dictionary.

A word is considered to be able to be packed on the board if:

* It can be found in the dictionary
* It can be constructed from untaken letters by other words found so far on the board
* The letters are adjacent to each other (vertically and horizontally, not diagonally).
* Each tile can be visited only once by any word.

For example, given the following dictionary:

```python
{ 'eat', 'rain', 'in', 'rat' }
```

and matrix:

```python
[['e', 'a', 'n'],
 ['t', 't', 'i'],
 ['a', 'r', 'a']]
```

Your function should return 3, since we can make the words 'eat', 'in', and 'rat' without them touching each other.

We could have alternatively made 'eat' and 'rain', but that would be incorrect since that's only 2 words.

## 347

You are given a string of length N and a parameter k. The string can be manipulated by taking one of the first k letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string daily and k = 1. The best we can create in this case is ailyd.

## 348

This problem was asked by Zillow.

A ternary search tree is a trie-like data structure where each node may have up to three children. Here is an example which represents the words `code`, `cob`, `be`, `ax`, `war`, and `we`.

```
       c
    /  |  \
   b   o   w
 / |   |   |
a  e   d   a
|    / |   | \
x   b  e   r  e
```

The tree is structured according to the following rules:

* left child nodes link to words lexicographically earlier than the parent prefix
* right child nodes link to words lexicographically later than the parent prefix
* middle child nodes continue the current word

For instance, since `code` is the first word inserted in the tree, and `cob` lexicographically precedes `cod`, `cob` is represented as a left child extending from `cod`.

Implement insertion and search functions for a ternary search tree.

## 352

This problem was asked by Palantir.

A typical American-style crossword puzzle grid is an N x N matrix with black and white squares, which obeys the following rules:

Every white square must be part of an "across" word and a "down" word.

No word can be fewer than three letters long.

Every white square must be reachable from every other white square.

The grid is rotationally symmetric (for example, the colors of the top left and bottom right squares must match).

Write a program to determine whether a given matrix qualifies as a crossword grid.

## 359

This problem was asked by Slack.

You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357


## 362

This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.


## 370

This problem was asked by Postmates.

The “active time” of a courier is the time between the pickup and dropoff of a delivery. Given a set of data formatted like the following:

(delivery id, timestamp, pickup/dropoff)
Calculate the total active time in seconds. A courier can pick up multiple orders before dropping them off. The timestamp is in unix epoch seconds.

For example, if the input is the following:

```
(1, 1573280047, 'pickup')
(1, 1570320725, 'dropoff')
(2, 1570321092, 'pickup')
(3, 1570321212, 'pickup')
(3, 1570322352, 'dropoff')
(2, 1570323012, 'dropoff')
```
The total active time would be 1260 seconds.

## 372

This problem was asked by Amazon.

Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.

## 376

This problem was asked by Google.

You are writing an AI for a 2D map game. You are somewhere in a 2D grid, and there are coins strewn about over the map.

Given the position of all the coins and your current position, find the closest coin to you in terms of Manhattan distance. That is, you can move around up, down, left, and right, but not diagonally. If there are multiple possible closest coins, return any of them.

For example, given the following map, where you are x, coins are o, and empty spaces are . (top left is 0, 0):

```
---------------------
| . | . | x | . | o |
---------------------
| o | . | . | . | . |
---------------------
| o | . | . | . | o |
---------------------
| . | . | o | . | . |
---------------------
```

return (0, 4), since that coin is closest. This map would be represented in our question as:

```
Our position: (0, 2)
Coins: [(0, 4), (1, 0), (2, 0), (3, 2)]
```

## 379

This problem was asked by Microsoft.

Given a string, generate all possible subsequences of the string.

For example, given the string xyz, return an array or set with the following strings:


```
x
y
z
xy
xz
yz
xyz
```
Note that zx is not a valid subsequence since it is not in the order of the given string.

## 381

This problem was asked by Paypal.

Read this Wikipedia article on Base64 encoding. [https://en.wikipedia.org/wiki/Base64]

Implement a function that converts a hex string to base64.

For example, the string:
```
deadbeef
```
should produce:
```
3q2+7w==
```

## 382

This problem was asked by Google.

Yesterday you implemented a function that encodes a hexadecimal string into Base64.

Write a function to decode a Base64 string back to a hexadecimal string.

For example, the following string:
```
3q2+7w==
```
should produce:
```
deadbeef
```

## 373

This problem was asked by Facebook.

Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed using elements from L.

For example, given L = [5, 2, 99, 3, 4, 1, 100], return 5 as we can build a sequence [1, 2, 3, 4, 5] which has length 5.

## 374

This problem was asked by Amazon.

Given a sorted array arr of distinct integers, return the lowest index i for which arr[i] == i. Return null if there is no such index.

For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2. Even though arr[3] == 3, we return 2 since it's the lowest index.


## 386

This problem was asked by Twitter.

Given a string, sort it in decreasing order based on the frequency of characters. If there are multiple possible solutions, return any of them.

For example, given the string `tweet`, return `tteew`. `eettw` would also be acceptable.

## 394

This problem was asked by Uber.

Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.

For example, given k = 18 and the following binary tree:

```
    8
   / \
  4   13
 / \   \
2   6   19
```
Return `True` since the path `8 -> 4 -> 6` sums to `18`.

### Solution

Let's represent the tree as the usual list with node at index `i` that has the left node at `2*i+1` and the right node at `2*i+2`.

```python
tree = [8,4,13,2,6,None,19]

def walk(t, current=0, s=0): # s is the accumulator of the sums until this node.
    left = current*2+1
    right = current*2+2
    something_on_the_left = (left<len(t) and t[left] is not None)
    something_on_the_right = (right<len(t) and t[right] is not None)
    is_a_leaf = not something_on_the_left and not something_on_the_right
    if is_a_leaf:
        yield s+t[current]
    else:
        if something_on_the_left:
            yield from walk(t, left, s+t[current])
        if something_on_the_right:
            yield from walk(t, right, s+t[current])
    
assert(18 in walk(tree)) == True
assert(17 in walk(tree)) == False

```

## 399

This problem was asked by Facebook.

Given a list of strictly positive integers, partition the list into 3 contiguous partitions which each sum up to the same value. If not possible, return null.

For example, given the following list:

`[3, 5, 8, 0, 8]`

Return the following 3 partitions:

```
[[3, 5],
 [8, 0],
 [8]]
```

Which each add up to 8.

### Solution

```python
l = [3, 5, 8, 0, 8]

def sol(l):
    ret = []
    s = sum(l)
    if s%3 != 0:
        return None
    target = s // 3 
    start = 0
    _sum = 0
    for i,v in enumerate(l):
        if _sum+v==target:
            ret.append(l[start:i+1])
            _sum = 0
            start = i+1
        elif _sum+v>target or len(ret)>3:
            return None
        else:
            _sum += v
    if len(ret) != 3:
        return None
    return ret 
    
print(sol(l))
```

## 401

This problem was asked by Twitter.

A permutation can be specified by an array `P`, where `P[i]` represents the location of the element at `i` in the permutation. For example, `[2, 1, 0]` represents the permutation where elements at the index `0` and `2` are swapped.

Given an array and a permutation, apply the permutation to the array. For example, given the array `["a", "b", "c"]` and the permutation `[2, 1, 0]`, return `["c", "b", "a"]`.

### Solution

```python
l = ["a", "b", "c"]
p = [2, 1, 0]

sol = [l[x] for x in p]

print(sol)
```

## 402 same as 362

This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.


## 403

This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).

[_See 71 reverse_](#71-reverse)

## 404

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given `[(30, 75), (0, 50), (60, 150)]`, you should return 2.

## 416

This problem was asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:

```
 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
```
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:
```
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
```

It takes 1 step to move from `(0, 0)` to `(1, 1)`. It takes one more step to move from `(1, 1)` to `(1, 2)`.

## 418

This problem was asked by Atlassian.

MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given `[10, 40, 200, 1000, 60, 30]`, you should return `[1, 2, 3, 4, 2, 1]`.

Given `[100, 40, 20, 1000, 60, 30]`, you should return `[3, 2, 1, 3, 2, 1]`.

### Solution

Let's assume there are never two employees with the same amount of lines of code, one aside the other.

```python
l = [10, 40, 200, 1000, 60, 30]

def sol(l):
    if not l:
        return l
    
    if len(l) == 1:
        return [1]
    
    mins = []  # list of the local minimums
    maxs = []  # list of the local maximums
    
    for i,x in enumerate(l):
        if (i==0 or x<l[i-1]) and (i==len(l)-1 or x<l[i+1]):
            mins.append(i)
        if (i==0 or x>l[i-1]) and (i==len(l)-1 or x>l[i+1]):
            maxs.append(i)

    ret = [None] * len(l)
    
    for m in mins:
        # ret[m]=1
        if maxs[0]<m:  # descending ramp
            M = maxs.pop(0)
            for i in range(m-M+1):
                if m-i>=0 and (ret[m-i] is None or ret[m-i]<i+1):
                    ret[m-i] = i+1
        # ascending ramp
        if maxs:
            M = maxs[0]
            for i in range(M-m+1):
                if m+1<len(ret) and (ret[m+i] is None or ret[m+i]<i+1):
                    ret[m+i] = i+1
    return ret  
```

If we have the same value side by side, we can get rid of it and put it back later.

```python
l = [10, 40, 200, 200, 200, 1000, 60, 30]

def remove_doubles(l):
    remove = set()
    for i,(a,b) in enumerate(zip(l,l[1:])):
        if a==b:
            remove.add(i)
            
    return remove, [x for i,x in enumerate(l) if i not in remove]        

def sol(l):
    if not l:
        return l
    
    if len(l) == 1:
        return [1]
    
    doubles, lines = remove_doubles(l)

    mins = []
    maxs = []
    
    for i,x in enumerate(lines):
        if (i==0 or x<lines[i-1]) and (i==len(lines)-1 or x<lines[i+1]):
            mins.append(i)
        if (i==0 or x>lines[i-1]) and (i==len(lines)-1 or x>lines[i+1]):
            maxs.append(i)

    ret = [None] * len(lines)
    
    for m in mins:
        # ret[m]=1
        if maxs[0]<m:  # descending ramp
            M = maxs.pop(0)
            for i in range(m-M+1):
                if m-i>=0 and (ret[m-i] is None or ret[m-i]<i+1):
                    ret[m-i] = i+1
        # ascending ramp
        if maxs:
            M = maxs[0]
            for i in range(M-m+1):
                if m+1<len(ret) and (ret[m+i] is None or ret[m+i]<i+1):
                    ret[m+i] = i+1

    for i in sorted(doubles):
        ret[i+1:i+1] = ret[i:i+1]

    return ret
```

## 419

This problem was asked by PagerDuty.

Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

## 422

This problem was asked by Salesforce.

Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.

### Solution

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return "Node(value:{},\n\tleft:{},\n\tright:{}\n)".format(self.value, self.left, self.right)
        
a = Node(13, Node(8), Node(7, Node(1), Node(3)))
b = Node(1, Node(18, right=Node(1)), Node(7, Node(1), Node(3)))

def walk(tree, idx = 0):
    if tree:
        yield (idx, tree.value)
        if tree.left:
            yield from walk(tree.left, idx*2+1)
        if tree.right:
            yield from walk(tree.right, idx*2+2)

def sol(a, b):
    sum_tree = dict(walk(a))
    size = 0
    for k, v in walk(b):
        if k not in sum_tree:
            sum_tree[k] = 0
        sum_tree[k] += v    
        if k>size:
            size=k
    
    # this is an additional step, you could just keep the `sum_tree` dict as result
    ret = [None] * (size+1)
    for k, v in sum_tree.items():
        ret[k] = v
    return ret
    
print(sol(a,b))
# >>> [14, 26, 14, None, 1, 2, 6]
```

The result is the usual binary tree with the root at 0, left node at `n*2+1`, and right node at `n*2+2`

If you want to go back to a `Node` tree

```python
def list_to_nodes(l, idx=0):
    if idx<len(l) and l[idx] is not None:
        return Node(l[idx], 
            list_to_nodes(l, idx*2+1),
            list_to_nodes(l, idx*2+2),
        )

print(list_to_nodes(sol(a,b)))
# Node(value:14,
# 	left:Node(value:26,
#   	left:None,
#    	right:Node(value:1,
#        	left:None,
#       	right:None
#       )
#   ),
# 	right:Node(value:14,
# 	    left:Node(value:2,
# 	        left:None,
# 	        right:None
#       ),
# 	    right:Node(value:6,
# 	        left:None,
# 	        right:None
#       )
#   )
# )
```

Alternatively we can use a `dict` as intermediate data structure, instead of our list-tree

```python
def sol(a, b):
    sum_tree = dict(walk(a))
    for k, v in walk(b):
        if k not in sum_tree:
            sum_tree[k] = 0
        sum_tree[k] += v    

    return sum_tree
    
print(sol(a,b))
# >>> {0: 14, 1: 26, 2: 14, 5: 2, 6: 6, 4: 1}
def list_to_nodes(tree, idx=0):
    if idx in tree:
        return Node(tree[idx], 
            list_to_nodes(tree, idx*2+1),
            list_to_nodes(tree, idx*2+2),
        )
```

## 423

This problem was asked by Microsoft.

The transitive closure of a graph is a measure of which vertices are reachable from other vertices. It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.

For example, suppose we are given the following graph in adjacency list form:

```
graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
```

The transitive closure of this graph would be:
```
[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
```

Given a graph, find its transitive closure.

## 434

This problem was asked by Oracle.

Given a binary search tree, find the floor and ceiling of a given integer. The floor is the highest element in the tree less than or equal to an integer, while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.

## 438

This problem was asked by Amazon.

Implement a stack API using only a heap. A stack implements the following methods:

* push(item), which adds an element to the stack
* pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)

Recall that a heap has the following operations:

* push(item), which adds a new key to the heap
* pop(), which removes and returns the max value of the heap

## 449

This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture. [https://en.wikipedia.org/wiki/Goldbach%27s_conjecture]

Example:

```
Input: 4
Output: 2 + 2 = 4
```

If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

```
[a, b] < [c, d]
```

If a < c OR a==c AND b < d.

## 456

This problem was asked by Amazon.

You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:

```
{"timestamp": 1526579928, count: 3, "type": "enter"}
```

This means 3 people entered the building. An exit looks like this:

```
{"timestamp": 1526580382, count: 2, "type": "exit"}
```

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.

## 452

This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

```
1 -> 2 -> 3 -> 4 -> 5
```

is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

```
9 -> 9
```
```
5 -> 2
```
return 124 (99 + 25) as:
```
4 -> 2 -> 1
```

## 451

This problem was asked by Apple.

Implement the function `fib(n)`, which returns the `n` <sup>`th`</sup> number in the Fibonacci sequence, using only `O(1)` space.


## 463 duplicated of 290

This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input `['R', 'G', 'B', 'G', 'B']`, it is possible to end up with a single Qux through the following steps:

```
        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
```


### Solution 463

```python
# evoltion rules
son={
    frozenset({'R','G'}): 'B',
    frozenset({'R','B'}): 'G',
    frozenset({'B','G'}): 'R'
}

def fx(l):
    """
    compute all possible next steps of a sequence `l`
    """
	for n,(a,b) in enumerate(zip(l,l[1:])):
		if a!=b:
			yield l[:n] + [son[frozenset((a,b))]] + l[n+2:]


def solution(l):
	stack = [l]
	already_seen = set()  # this is to avoid following multiple identical paths
	while stack:
		x = stack.pop()
		if tuple(x) in already_seen:
			continue
		else:
			already_seen.add(tuple(x))
		y = None
		for y in fx(x):
		    stack.append(y)
		if y is None:  # if there is no possible evolution, yield the current value as a final one.
		    yield x

# example
>>> _in = list("RGBGGRGRBR")
>>> min(solution(_in))
['B', 'B']
>>> list(solution(_in))
[['R', 'R'], ['B', 'B'], ['G', 'G'], ['R', 'R', 'R', 'R'], ['B', 'B', 'B', 'B'], ['G', 'G', 'G', 'G']]
>>>

# example from the problem
>>> list(solution(list('RGBGB')))
[['R'], ['R', 'R', 'R']]
>>> min(solution(list('RGBGB')))
['R']

```

## 504

This problem was asked by Twitter.

You run an e-commerce website and want to record the last `N` `order ids` in a log.

Implement a data structure to accomplish this, with the following API:

* `record(order_id)`: adds the order_id to the log
* `get_last(i)`: gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.

### Solution 504

Circular buffer

```python

class LastOrders:
    def __init__(self, n):
        self._ptr = 0
        self._n = n
        self._buffer = [None] * n

    def record(self, order_id):
        self._buffer[self._ptr] = order_id
        self._ptr += 1
        self._ptr %= self._n

    def get_last(self, i):
        if i>self._n:
            raise ValueError()
        start = self._ptr - i
        if start < 0:
            return self._buffer[start % self._n :] + self._buffer[: self._ptr]
        return self._buffer[start: self._ptr]
```

What if we ask for more elements than what we put in ?

We will get some `None` in the list. We can always filter them out.

```
>>> l = LastOrders(10)
>>> l.record(1231231)
>>> l.get_last(1)
[1231231]
>>> l.get_last(2)
[None, 1231231]
>>> l.record(12311)
>>> l.get_last(2)
[1231231, 12311]
>>> l.get_last(3)
[None, 1231231, 12311]
```

## 518

This problem was asked by Microsoft.

Given an array of numbers and a number k, determine if there are three entries in the array which add up to the specified number k. For example, given `[20, 303, 3, 4, 25]` and `k = 49`, return `true` as 20 + 4 + 25 = 49.

## 539

This problem was asked by Pandora.

Given an undirected graph, determine if it contains a cycle.

## 581

This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

```
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
```

and

```
{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
```

return 6.

## 600

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

## 644

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 ```

 ## 662

 This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers `[42, 56, 14]`, return `14`.

### Solution

```python
from collections import defaultdict

l = [42, 56, 14]

def prime_fact(n):
    ret = defaultdict(int)
    m = 2
    while n>1:
        while n % m == 0:
            n //= m
            ret[m] += 1
        m += 1 if m==2 else 2
    return ret
    
assert prime_fact(84)=={2: 2, 3: 1, 7: 1}

def sol(l):
    ret = None
    for x in l:
        if ret is None:
            ret = prime_fact(x)
        else:
            factors = prime_fact(x)
            # merge ret and factors into new based on the GCD rules
            new = {}
            for k,v in ret.items():
                if k in factors:
                    new[k] = min(v, factors[k])
            ret = new
    ret_n = 1
    if ret:
        for k,v in ret.items():
            ret_n *= k**v
    
    return ret_n

print(sol(l))
```

## 671

This problem was asked by Facebook.

Given a function `f`, and `N` return a debounced `f` of `N` milliseconds.

That is, as long as the debounced `f` continues to be invoked, `f` itself will not be called for `N` milliseconds.

