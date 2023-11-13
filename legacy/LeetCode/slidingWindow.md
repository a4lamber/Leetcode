# Sliding window

我目前的理解, sliding window technique,实际上就是two pointer technique的一个变种;

two types of slidign window
- fixed length window
- dynamically resizable window





Dead giveaway for using sliding window
- things we iterate over **sequentially**
  - **contiguou** sequence of elements like strings, arrays, linked list
- min,max,longest,shortest,contained
  - maybe we need to calculate something



questions variants
- fixed length 
  - max sum subarray of size K
- dynamic variant
  - smallest sum >= to some value S
- dynamic variant with auxillary data structure
  - boolean flag, hash


# Reference
- [Youtuber, Ryan Schachte](https://www.youtube.com/watch?v=MK-NZ4hN7rs&ab_channel=RyanSchachte)

he summarizes the question variants and keyword and hints for suggesting sliding window technique very well. Did his example in java.


- [youtuber, Byte by Byte](https://www.youtube.com/watch?v=GcW4mgmgSbw&ab_channel=BytebyByte)
  
Concise and clean explanation, focus on technique, taught in python, start with this video if you are new to the sliding window technique.
