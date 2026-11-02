# maths-logic-solvers
A collection of Python scripts solving mathematical and algorithmic logic puzzles.

## 1. The 100 Coins Riddle (`coin_puzzle.py`)

### The Problem
You are placed in a pitch-black room with 100 identical coins on a table. Exactly 10 coins are facing Heads up, and 90 are facing Tails up. You cannot see the coins, and you cannot feel which side is facing up. 

**Task:** Divide the 100 coins into two separate groups (not necessarily equal in size) such that both groups contain the exact same number of coins facing Heads up. All 100 coins must be used.

### The Algorithmic Solution
1. Count out exactly 10 random coins into Group A (leaving 90 coins in Group B).
2. Flip every single coin in Group A over. 
3. Mathematically, the number of Heads in both groups will now be identical every single time.

## 2. Ritangle Competition Matrix Search (`ritangle_q1.py`)




### Code Implementation Walkthrough
Lines 1-2 = Creating 2 “axis” as arrays – the prime number axis x and y. 

Line 3 = Creating variable total to be used at end of program 

Lines 4-9 = using indented for loops to identify every coordinate of point on grid 

Line 10 = Stating the coordinates of the points provided in the question 

Lines 11-16 = Creating variable and using indented for loops to store the 33 available coordinates, excluding the 3 given points. 

Lines 17-27 = The actual brute forcing of the code. Using 3 indented for loops to find 3 unique coordinates and then assigning theses coordinates to 3 new variable points. 

Lines 28-42 = Finding the distance between the new coordinates and the given points using Pythagoras idea.

Lines 43-47 = Adding all distances that are not the same or unique, to a new list of distances. 

Lines 48-50 = Checking if all distances are different to each other. If they are not, program finds a new list of coordinates and repeats finding distances till all 15 distances are unique. 

Lines 51-54 = Multiplying x and y components of original prime number axes to find the value of each point. 

Lines 55-57 = Adding all the new values together and outputting the result. Program then breaks to prevent the for loop repeating for anymore unwanted coordinates.
