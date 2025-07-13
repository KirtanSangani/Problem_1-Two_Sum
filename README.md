# Problem 1: Two Sum

7/13/2025

## Thought Process
My initial reaction to the problem was to use a double for loop to be able to traverse through the List multiple times. I did try this method, knowing that it would be exponentially slower than I wanted it to be; however, I wanted to try a brute force method first before optimizing the solution. The optimized solution was challenging only because I knew I needed a Hash Map for this problem; however, I did not know the proper implementation of a Hash Map while doing this. 

##  Initial Solution
I created my ans List variable, which is where I would store the correct indexes. I created my double for loop, with the outer loop only looping once, and the inner loop looping the length of the List n times. In the loops, I checked to see if the num[i] + num[j] was equal to the target. If it was, I added it to the ans List and returned it. After the for loops, I returned the ans List.

Initial solution - 2015 ms 

Complexity - O(n^2)

## Final Solution
After doing some research, I implemented the Hash Map, which logically is somewhat similar to that of a set. Instead of [], I used {} for my ans variable. I created a for loop with i and num as my indexes. I also created a temp variable which is equal to the target minus the num. I checked to see if temp was in the Hash Map, and if it was, the program would return a List of the index of temp in the Hash Map and i. If that did not run, I would add temp and its corresponding index to the Hash Map. In the end, I returned an empty list if there was no solution

Final Solution - 0 ms

Complexity - O(n)

## Takeaways
I learned how to create a Hash Map in Python and some basic methods I can use to modify and manipulate the Hash Map. I also learned about how the speed of a Hash Map can be used to go around the use of a double for loop. I also learned the enumerate() function, which allows you to iterate through a list and also have the indexes of each variable. I also found out that you can use enumerate() within the for loop to iterate through.