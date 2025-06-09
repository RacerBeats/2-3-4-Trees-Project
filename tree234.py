# Francisco Ortega & Dillan Desai - responsible for this file
# Group Members: Dillan Desai (ID: 10629536), Ryan Cheung (ID: 10754470), Francisco Ortega (ID: 10758041)
# Course Section: CS 034 - 39575
# Instructor: Prof. Ashraf
# Date: 6/8/25
# Chapter 15 Lab: Building a B-Tree

# Description: This file contains the Node and Tree234 classes along with methods for inserting, 
# checking the existence of a key, and printing the keys in sorted order.


class Node:
    def __init__(self):
        self.keys = []
        self.children = []

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        return False
        
    def is_full(self):
        # A node is full when it has 3 keys (maximum for a 2-3-4 tree)
        return len(self.keys) == 3


class Tree234:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        # If root is full, we need to split it before inserting
        if self.root.is_full():
            new_root = Node()
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(self.root, key)
        else:
            self._insert_non_full(self.root, key)

    def _split_child(self, parent, index):
        # Get the child that needs to be split
        child = parent.children[index]
        
        # Create a new node to hold the right half
        new_node = Node()
        
        # Move the middle key to the parent
        middle_key = child.keys[1]
        parent.keys.insert(index, middle_key)
        
        # Move the right key to the new node
        new_node.keys.append(child.keys[2])
        
        # Update the original child to only have the left key
        child.keys = [child.keys[0]]
        
        # If the child is not a leaf, distribute its children
        if not child.is_leaf():
            new_node.children = child.children[2:]  # Right half of children
            child.children = child.children[:2]     # Left half of children
        
        # Insert the new node as a child of the parent
        parent.children.insert(index + 1, new_node)

    def _insert_non_full(self, node, key):
        # Start from the rightmost key
        i = len(node.keys) - 1
        
        # If node is a leaf, insert the key in the correct position
        if node.is_leaf():
            # Find the right position for the key
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
        else:
            # Find the child where the key should be inserted
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            
            # If the child is full, split it
            if node.children[i].is_full():
                self._split_child(node, i)
                # After splitting, determine which child to go to
                if key > node.keys[i]:
                    i += 1
            
            # Recursively insert into the appropriate child
            self._insert_non_full(node.children[i], key)

    def contains(self, key):
        return self._contains(self.root, key)

    def _contains(self, node, key):
        i = 0
        while i < len(node.keys):
            if key == node.keys[i]:
                return True
            elif key < node.keys[i]:
                break
            i += 1

        if node.is_leaf():
            return False

        return self._contains(node.children[i], key)

    def inOrderTraversal(self):
        self._inOrderTraversal(self.root)

    def _inOrderTraversal(self, node):
        if node is None:
            return
        for i in range(len(node.keys)):
            if not node.is_leaf():
                self._inOrderTraversal(node.children[i])
            print(node.keys[i], end=" ")
        if not node.is_leaf():
            self._inOrderTraversal(node.children[-1])
            