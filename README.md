# IP-Projects
Intorduction to Programming- course projects


1. Web Service Application-
Process JSON data from a webiste and read certain attributes like weather, humidity and report it using a Python script

________________________________________________________________________________________________________________________________________________

2. KMap Initialization
Write a program in Python and a test file, which takes a function of maximum 4 variables as input and gives the corresponding minimized function(s) as the output 
(minimized using the K-Map methodology), considering the case of Don’t Care conditions.

Example 1: 
No. of variables: 4
Function: (0,1,2,4,5,6,8,9,12,13,14) d -
Simplified expression: y’+w’z’+xz’


________________________________________________________________________________________________________________________________________________

3. Betweenness Centrality-

If there is a list of nodes sorted in decreasing order according to their Standardized Betweenness Centralities, the first ‘k’ nodes with equal Standardized Betweenness Centrality from this list will be the output. 

For accomplishing this last we can divide the task into sub-tasks:
-	Creation of the graph
-	Calculating the Standardized Betweenness Centrality of each of the nodes
a.	Calculating no. of shortest paths between a pair of nodes (say A and B)
b.	Calculating no. of shortest paths between a pair of nodes passing through the node chosen (say C) for calculating the Standardized Betweenness Centrality
c.	Repeat steps a and b for each pair of nodes. The summation of all the X/Y will be the Betweenness Centrality of node C. From this we can also calculate the Standardized Betweenness Centrality.
d.	Similarly, repeat steps a,b and c to get the Standardized Betweenness Centrality of all the nodes in the graph.
-	Producing the output of top-‘k’ nodes


________________________________________________________________________________________________________________________________________________


4. Matplotlib Transformations 2D

Take input as shape type, either dic or polygon and translate it or rotate it through any angle theta using matrix linear transformations and plot using matplotlib

________________________________________________________________________________________________________________________________________________
