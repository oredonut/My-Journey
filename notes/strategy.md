According to what I've learnt so far
## when solving a leet Code problem:
I have  to analyse the problem properly, I look at the data I'm given whether it is an array, a string or a graph and what they asked me to do with it .
e.g Track nested structures like valid parentheses,LIFO should come to your head which means you're using stacks

## Then Check the constraints
 Using this cheat sheet 
 - If n<= 20....expected time complexity : O(2**n) or O(n!)
 And we prolly using brute force or backtracking  because the data size is tiny
 - If n<= 100....expected time complexity : O(n**3) or O(n**2) 
 prolly use nested loops
- If n<= 10**5>....O(nlogn) or O(n)
 Nested loop will fail, Using divide and conquer is advisable
 ## Walk through the framework
 Always figure out the brute force way first