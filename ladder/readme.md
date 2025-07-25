# The Ladder Problem

## Problem Statement
You have a ladder with **n** rungs. You can climb the ladder by taking either:
- **1 step** at a time, or
- **2 steps** at a time, or
- a mix of **1 step** and **2 steps**

**Question**: How many different ways are there to reach the top of the ladder?

---

## Examples

### Small Cases
**1 rung ladder**:
- Only one way: take 1 step
- **Answer: 1 way**

**2 rung ladder**:
- Way 1: take 1 step, then 1 step
- Way 2: take 2 steps at once
- **Answer: 2 ways**

**3 rung ladder**:
- Way 1: 1 + 1 + 1
- Way 2: 1 + 2
- Way 3: 2 + 1
- **Answer: 3 ways**

---

## Discovery Steps

### Step 1: Calculate More Examples
Work out the answers for larger ladders:
- **4 rungs**: ? ways
- **5 rungs**: ? ways  
- **6 rungs**: ? ways

*Try to list out all the combinations for the 4-rung case to verify your answer.*

### Step 2: Look for Patterns
Once you have calculated the first 6 answers, examine the sequence:
- Do you notice any relationship between consecutive numbers?
- Can you predict the next number in the sequence without calculating all combinations?
- What mathematical sequence does this remind you of?

### Step 3: Write a function to calculate the answer (ladder1.py)
Implement a basic recursive solution.

### Step 4: Write a class to calculate the answer (ladder2.py)
Convert your function into a class-based approach.

### Step 5: Write a class with memory to calculate the answer (ladder3.py)
Add a cache of previous results for better performance.

### Step 6: Compare performance (ladder4.py)
Combine all implementations and time each one to see which performs best.

---

## Files in this Project
- **ladder/ladder1.py** - Basic recursive function
- **ladder/ladder2.py** - Class-based recursive solution
- **ladder/ladder3.py** - Optimised class with caching
- **ladder/ladder4.py** - Performance comparison tool