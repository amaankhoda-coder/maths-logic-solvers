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
