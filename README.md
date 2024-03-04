# Coding Challenges

This repository contains solutions to three coding challenges written in Python. The challenges are as follows:

1. **Challenge 1: Equal Bricks**
   
   Given an array representing the number of bricks in each box, the task is to calculate the minimum number of moves needed to distribute the bricks in such a way that each box contains exactly 10 bricks.

2. **Challenge 2: Maximum Sum of Two Numbers**
   
   Given an array of integers, the goal is to find the maximum sum of two numbers whose digits add up to the same sum.

3. **Challenge 3: String Generation**
   
   Given an integer N, the task is to generate a string of length N containing as many different lowercase letters ('a' - 'z') as possible, with each letter occurring an equal number of times.

## Table of Contents

1. [Equal Bricks](#equal-bricks)
2. [Maximum Sum of Two Numbers](#maximum-sum-of-two-numbers)
3. [String Generation](#string-generation)
4. [How to Use](#how-to-use)
5. [Contributing](#contributing)
6. [License](#license)

## Equal Bricks

The solution to this problem involves calculating the minimum number of moves required to distribute bricks equally across boxes. It iterates through the array of bricks, determining the necessary moves to adjust the brick count in each box until they all have exactly 10 bricks. If it's not possible, the function returns -1.

## Maximum Sum of Two Numbers

This challenge focuses on finding the maximum sum of two numbers from an array whose digits add up to the same sum. It employs a dictionary to store the maximum sum of two numbers for each sum of digits, iterating through the array to calculate the sum of digits for each number and updating the maximum sum accordingly.

## String Generation

The goal of this task is to generate a string of length N containing as many different lowercase letters ('a' - 'z') as possible, with each letter occurring an equal number of times. It first determines the number of times each letter should occur, then generates the string pattern accordingly.

## How to Use

To use these solutions:

1. Clone this repository to your local machine.
2. Navigate to the directory containing the Python files.
3. Run the Python files using a Python interpreter.

```bash
python challenge1.py
python challenge2.py
python challenge3.py
