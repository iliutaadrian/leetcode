### Arrays Hashing

#### Contains Duplicate - [217](217.py)
Use a hash set and compare the length
#### Valid Anagram - [242](242.py)
Use 2 frequency list
Sort the 2 arrays compare
Use 2 hash with frequency
#### Two Sum - [1](1.py)
One pass with hash and calculate target - each number value.
#### Group Anagrams - [49](49.py)
Frequency of [0]\*26
Tuple of frequency
#### Top K Frequent Elements - [347](347.py)
Make a count hash {1:3, 2:3}
Frequency based on length array
Iterate reverse
#### Product of Array Except Self - [238](238.py)
no division
Prefix and Postfix array for every number in array
```python
[1,2,3,4]
[1,1,2,6] - prefix
[24,12,4,1] - suffix
[24,12,8,6]
```
#### Valid Sudoku - [36](36.py)
cols = {}
rows = {}
boxes = {} # boxes[(i // 3, j // 3)] = set()
#### Longest Consecutive Sequence - [128](128.py)
Make a set
Find if the number is the first in the sequence by checking if the number - 1 is in the array
Search the number + 1 to the end

---

### Two Pointers

#### Valid Palindrome - [125](125.py)	
Method 1: reverse the string and check it with the original one.
Method 2: use 2 pointers and compare the characters. 
#### Two Sum II Input Array Is Sorted - [167](167.py)
Start, end. Calculate the sum of nums pointer. 
If the sum is < target start++; sum > target end--
#### 3Sum - [15](15.py)
Take first number at start. Check if > target, and remove duplicates.
Take 2 pointers and do a 3 sum.
#### Container With Most Water - [11](11.py)
Area Rectangle = min(height) * (end - start). If height[start] < height[end] start++ else end--
#### Trapping Rain Water

---

### Sliding window

#### Best Time to Buy And Sell Stock - [121](121.py)	
```python
start = stock[0], max profit = 0, find max profit in the array.
```
#### Longest Substring Without Repeating Characters	- [3](3.py)
while char in set, remove from the start
bcd, c
#### Longest Repeating Character Replacement	
#### Permutation In String	
#### Minimum Window Substring	
#### Sliding Window Maximum

---

### Stack
#### Valid Parentheses - [20](20.py)
Map = {")": "(", "]": "[", "}": "{"}
make a stack, check last element in map, check last element from stack
#### Min Stack - [155](155.py)
one stack, one min_stack; piush in each stack
#### Evaluate Reverse Polish Notation - [150](150.py)
operators list, stack with numbers. If operator, pop 2 and do the operation
#### Generate Parentheses - [22](22.py)
backtrack(self, open, closed, n, stack, res):
return if open == closed == n; open < n, add (, backtrack, pop; if closed < open, add ), backtrack, pop
#### Daily Temperatures	- [739](739.py)
```python
monotonic decreasing order stack
stack = [] # pair of (temperature, index)
Input: temperatures = [73,74,75,71,69,72,76,73]

Output: [1,1,4,2,1,1,0,0]

Process:
- For the first temperature 73, there's no warmer temperature ahead, so it waits 1 day to get warmer (74).
- For the second temperature 74, it waits 1 day to get warmer (75).
- For the third temperature 75, it waits 4 days to get warmer (76).
- For the fourth temperature 71, it waits 2 days to get warmer (72).
- For the fifth temperature 69, it waits 1 day to get warmer (72).
- For the sixth temperature 72, it waits 1 day to get warmer (76).
- For the seventh and eighth temperatures 76 and 73, there's no warmer temperature ahead, so they wait 0 days.
```
#### Car Fleet	
#### Largest Rectangle In Histogram


