# Lab 15 - Creating & Applying a 2-3-4 Tree ADT

## Description

This lab implements a custom 2-3-4 Tree ADT and tests it using a test program.
The test program creates a random list of 15 - 20 integers and inserts them into the tree.
The program then performs a traversal of the tree, examining the numbers present in the tree.

This demonstrates an applied understanding of the 2-3-4 Tree data structure.
---

# Members

- **Dillan Desai ID: 10629536** – 2-3-4 Tree implementation ('tree234.py')
- **Ryan Cheung ID: 10754470** – Test Program (`main_test.py`) & README
- **Francisco Ortega ID: 10758041** – 2-3-4 Tree implementation ('tree234.py')
- **Course Section**: CS 034 - 39575  
- **Instructor**: Prof. Ashraf  
- **Date**: 06/08/25

---

## Project Structure

```
tree234.py      # Main script that contains core logic of a 2-3-4 Tree
main_test.py    # Testing script, initializes instance of 2-3-4 Tree & random number list
```

---

## Requirements

- Python 3.x
- No external libraries needed
---

## Instructions to Run

1. Make sure the following files are in the same directory:
   - `tree234.py`
   - `main_test.py`

2. Run the program:

### On Windows:
```bash
python main_test.py
```

### On macOS/Linux:
```bash
python3 main_test.py
```
---

## Input
**main_test.py**

The program initializes a 2-3-4 Tree and inserts a list of random integers into the tree.

## Output

Console output pasted from 1 instance of running the program:

```
Inserting 15 random values into the 2-3-4 Tree:
Values: [16, 33, 79, 48, 68, 29, 41, 68, 17, 1, 37, 11, 54, 64, 88]
--------------------------------------------------
Inserting: 16
Inserting: 33
Inserting: 79
Inserting: 48
Inserting: 68
Inserting: 29
Inserting: 41
Inserting: 68
Inserting: 17
Inserting: 1
Inserting: 37
Inserting: 11
Inserting: 54
Inserting: 64
Inserting: 88

--------------------------------------------------
Testing 'contains' method:
Tree contains 68: True
Tree contains 1: True
Tree contains 68: True
Tree contains 169: False
Tree contains 121: False

--------------------------------------------------
In-order traversal of the tree (should be sorted):
1 11 16 17 29 33 37 41 48 54 64 68 68 79 88 

--------------------------------------------------
Verification - sorted input values:
[1, 11, 16, 17, 29, 33, 37, 41, 48, 54, 64, 68, 68, 79, 88]

--------------------------------------------------
Validating all values were inserted correctly:
SUCCESS: All inserted values were found in the tree!
```

