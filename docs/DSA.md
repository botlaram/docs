# All about Data Structure Algorithms with Real-time example

## Linear Search

Linear search, also known as sequential search, is a simple search algorithm that checks each element in a list or array until the target element is found or the entire list is traversed. It starts searching from the beginning of the list and compares each element with the target element until a match is found or the end of the list is reached.

![alt text](./png/linear-search.png)

### Realtime Example Linear Search

A real-time example of linear search could be searching for a specific contact in your phone's contact list.

Imagine you have a list of contacts stored in your phone, and you want to find the contact information for a particular person, let's say "John Doe". You could use linear search to look through each contact in your list one by one until you find the contact named "John Doe".

## Binary Search

Binary search is a searching algorithm that efficiently finds the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half. Here's how it works:

Initial Step: Binary search requires the array to be sorted initially. Let's say you have a sorted array arr.

Divide: Start with the whole array. Calculate the midpoint of the array.

Compare: Compare the target value with the element at the midpoint. If the target value matches the midpoint value, the search is successful.

Adjust Search Range: If the target value is less than the midpoint value, then the target, if present, must be in the lower half of the array. If the target value is greater, then it must be in the upper half.

Repeat: Repeat steps 2-4 until the target value is found or until the search interval is empty.

![alt text](./png/binary_search.png)

### Realtime Example Binary Search

A real-life example of binary search can be found in a library catalogue system.

Imagine you are searching for a particular book in a library with thousands of books arranged in alphabetical order by title. Instead of starting from the first book and checking each book sequentially, which could take a long time especially in a large library, you can use binary search.
