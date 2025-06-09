# Ryan Cheung - responsible for this file
# Group Members: Dillan Desai (ID: 10629536), Ryan Cheung (ID: 10754470), Francisco Ortega (ID: 10758041)
# Course Section: CS 034 - 39575
# Instructor: Prof. Ashraf
# Date: 6/8/25
# Chapter 15 Lab: Building a B-Tree

# Description: Test program for 2-3-4 Tree implementation

import random
import sys
import os

# Add the parent directory to the path to allow importing the module
# This makes the import work regardless of where the script is run from
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Tree234 class using a relative path
from last_lab.tree234 import Tree234
def main():
    # Create a 2-3-4 Tree
    tree = Tree234()
    
    # Generate 15-20 random integers between 1 and 100
    num_values = random.randint(15, 20)
    random_values = [random.randint(1, 100) for _ in range(num_values)]
    
    print(f"Inserting {num_values} random values into the 2-3-4 Tree:")
    print("Values:", random_values)
    print("-" * 50)
    
    # Insert the random values into the tree
    for value in random_values:
        print(f"Inserting: {value}")
        tree.insert(value)
    
    print("\n" + "-" * 50)
    print("Testing 'contains' method:")
    
    # Test contains method with values that should be in the tree
    for i in range(3):  # Test 3 random values from our inserted set
        if len(random_values) > 0:
            test_value = random_values[random.randint(0, len(random_values) - 1)]
            print(f"Tree contains {test_value}: {tree.contains(test_value)}")
    
    # Test contains method with values that should NOT be in the tree
    for i in range(2):  # Test 2 values that shouldn't be in the tree
        non_existent = random.randint(101, 200)  # Values outside our insertion range
        print(f"Tree contains {non_existent}: {tree.contains(non_existent)}")
    
    print("\n" + "-" * 50)
    print("In-order traversal of the tree (should be sorted):")
    tree.inOrderTraversal()
    
    # Verify the tree is sorted by comparing with sorted input
    print("\n\n" + "-" * 50)
    print("Verification - sorted input values:")
    print(sorted(random_values))
    
    # Validate that all inserted values can be found
    print("\n" + "-" * 50)
    print("Validating all values were inserted correctly:")
    all_found = True
    for value in random_values:
        if not tree.contains(value):
            print(f"ERROR: Value {value} was inserted but not found in the tree!")
            all_found = False
    
    if all_found:
        print("SUCCESS: All inserted values were found in the tree!")

if __name__ == "__main__":
    main()
