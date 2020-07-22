# Knuth's Conjecture in Pyhton3 using BFS

According to Knuth's conjecture we can generate any number with the help of number 4, square root and factorial.
For example, 
For n = 5 the series of operations are
1. Take factorial of 4
	4! = 24
2. Take factorail of 24
	24! = 620448401733239439360000
3. Take square root of 24!
	sqrt(24!) = 787685471322
4. Take square root of 787685471322
	sqrt(787685471322) = 887516
5. Take square root of 887516
	sqrt(887561) = 942
6. Take square root of 942
	sqrt(942) = 30
7. Take square root of 30
	sqrt(30) = 5

In this code, we select starting node as 4 and then we generate factorial of 4 and square root of 4 and then we 
take each node and apply these two operations until we find the given number. Once we find the given number we 
retrace the complete path upto the starting node.
