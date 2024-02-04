# All about Data Structure Algorithms with Real-time example

<br>
<p align="center"><img src="https://i.ibb.co/hB0gQWq/dsa.png" height="200"></p>

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

## Linked List

Linked list consists of a sequence of elements called nodes. Each node contains two parts: the data and a reference (or pointer) to the next node in the sequence. Linked lists offer dynamic memory allocation, efficient insertion and deletion operations, and are especially useful when the size of the data structure is unknown or frequently changing.

![alt text](./png/linkedlist.png)

### Why Linked List

For eg: Let's assume we have a list of elements in array

```python
list=[1,2,3,4,5,6,7,8,9,.......,1000000]
```

If we want to insert element in between, all numbers next to the insertion elements will be shifted further.  
Suppose, If we have 1 million of elements in the array (this may take a long time to shift).
Also this increases the time complexity.

LinkedList algorithm stores elements with the address of next node.  
So it doesn't need to shift any nodes while inserting or deleting an element from the middle of
elements.

### Realtime Example Linked List

Let's consider a real-life example of a linked list: a playlist in a music streaming application.

In a music streaming application like Spotify or Apple Music, a playlist is essentially a collection of songs that users can organize and listen to in a particular order. We can represent a playlist using a linked list data structure.

Node Representation:
Each node in the linked list represents a song in the playlist. It contains two parts:

Data: Information about the song, such as the song title, artist, album, duration, etc.
Reference: A reference to the next song in the playlist.
Playlist Structure:

The playlist starts with the first song (the head of the linked list).
Each song is linked to the next song in the playlist through the "next" reference.
The last song in the playlist points to None, indicating the end of the playlist.
Operations:

Adding a Song: To add a new song to the playlist, we create a new node and update the reference of the last song to point to the new song.  
Deleting a Song: To remove a song from the playlist, we adjust the references of the neighboring nodes to bypass the deleted node.  
Playing Songs: We can traverse the linked list from the beginning (head) to the end, playing each song in the playlist sequentially.  
Reordering Songs: We can easily rearrange the playlist by modifying the references between nodes without moving the actual song data.
