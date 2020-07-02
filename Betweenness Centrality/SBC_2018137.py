#!/usr/bin/env python3
from collections import defaultdict 
from copy import *
import re
import itertools

ROLLNUM_REGEX = "2018137"




class Graph(object):
    name = "Daksh Thapar"
    email = "daksh18137@iiitd.ac.in"
    roll_num = "2018137"

    def __init__ (self, vertices, edges):
        """
        Initializes object for the class Graph

        Args:
            vertices: List of integers specifying vertices in graph
            edges: List of 2-tuples specifying edges in graph
        """

        self.vertices = vertices
        
        ordered_edges = list(map(lambda x: (min(x), max(x)), edges))
        
        self.edges    = ordered_edges
        self.graph = defaultdict(list) 
        
        self.validate()

    def validate(self):
        """
        Validates if Graph if valid or not

        Raises:
            Exception if:
                - Name is empty or not a string
                - Email is empty or not a string
                - Roll Number is not in correct format
                - vertices contains duplicates
                - edges contain duplicates
                - any endpoint of an edge is not in vertices
        """

        if (not isinstance(self.name, str)) or self.name == "":
            raise Exception("Name can't be empty")

        if (not isinstance(self.email, str)) or self.email == "":
            raise Exception("Email can't be empty")

        if (not isinstance(self.roll_num, str)) or (not re.match(ROLLNUM_REGEX, self.roll_num)):
            raise Exception("Invalid roll number, roll number must be a string of form 201XXXX. Provided roll number: {}".format(self.roll_num))

        if not all([isinstance(node, int) for node in self.vertices]):
            raise Exception("All vertices should be integers")

        elif len(self.vertices) != len(set(self.vertices)):
            duplicate_vertices = set([node for node in self.vertices if self.vertices.count(node) > 1])

            raise Exception("Vertices contain duplicates.\nVertices: {}\nDuplicate vertices: {}".format(vertices, duplicate_vertices))

        edge_vertices = list(set(itertools.chain(*self.edges)))

        if not all([node in self.vertices for node in edge_vertices]):
            raise Exception("All endpoints of edges must belong in vertices")

        if len(self.edges) != len(set(self.edges)):
            duplicate_edges = set([edge for edge in self.edges if self.edges.count(edge) > 1])

            raise Exception("Edges contain duplicates.\nEdges: {}\nDuplicate vertices: {}".format(edges, duplicate_edges))

    





    def min_dist(self, start_node, end_node):
        '''
        Finds minimum distance between start_node and end_node

        Args:
            start_node: Vertex to find distance from
            end_node: Vertex to find distance to

        Returns:
            An integer denoting minimum distance between start_node
            and end_node
        '''
       
        d={}
        for i in range(len(self.vertices)):
            d[self.vertices[i]]=[]

       
        for i in range(len(self.edges)):
           
            d[self.edges[i][0]].append(self.edges[i][1])
            d[self.edges[i][1]].append(self.edges[i][0])
 
        Q=[start_node]
        X=[[start_node]]


        while len(Q)!=len(self.vertices):
            
            for i in range(len(X)):
          
                l=[]

                for j in range(len(X[i])):
                    
                    if d[X[i][j]] not in X:     
                        
                        for u in range(len(d[X[i][j]])):

                            if d[X[i][j]][u] not in Q:

                                l.append(d[X[i][j]][u])
                X.extend([l])
                
                
            for i in range(len(X)):
                for j in range(len(X[i])):

                    if X[i][j] not in Q:
                        Q.append(X[i][j])


        c=X.count([])
        for i in range(c):
            X.remove([])

        for i in range(len(X)):
            X[i]=deepcopy(list(set(X[i])))



        for i in range(len(X)):
            if start_node in X[i]:
                L_s=i+1

            if end_node in X[i]:
                L_e=i+1

        dist=L_e- L_s

        return dist

        raise NotImplementedError




    def all_shortest_paths(self,start_node, end_node):
        """
        Finds all shortest paths between start_node and end_node

        Args:
            start_node: Starting node for paths
            end_node: Destination node for paths

        Returns:
            A list of path, where each path is a list of integers.
        """

        X=self.all_paths(start_node,end_node)
        distance=self.min_dist(start_node,end_node)
        O=[]

        for i in range(len(X)):
            if len(X[i])==distance+1:
                O.append(X[i])
        

        return O

        raise NotImplementedError



    def printAllPathsUtil(self, start_node, end_node, visited, path,O) : 

        d={}
        
        for i in range(len(self.vertices)):
            d[self.vertices[i]]=[]

        for i in range(len(self.edges)):
               
            d[self.edges[i][0]].append(self.edges[i][1])
            d[self.edges[i][1]].append(self.edges[i][0])

        visited[start_node]= True
        path.append(start_node) 

        if start_node==end_node: 
            O.append(path[:])
        else: 
            
            for i in d[start_node]: 
                if visited[i]==False: 
                    self.printAllPathsUtil(i,end_node , visited, path,O) 
                      
        path.pop() 
        
        visited[start_node]= False

        return O

        raise NotImplementedError

        

   
    def all_paths(self,start_node, end_node): 
  
        visited=[False]*(len(self.vertices)+1) 
        O=[]
        path=[] 
  
        return self.printAllPathsUtil(start_node,end_node,visited,path,O)

        raise NotImplementedError



    def betweenness_centrality(self, node):
        """
        Find betweenness centrality of the given node

        Args:
            node: Node to find betweenness centrality of.

        Returns:
            Single floating point number, denoting betweenness centrality
            of the given node
        """
        pairs=[]


        for i in range(len(self.vertices)):
            for j in range(i+1,len(self.vertices)):
                if self.vertices[i]!=node and self.vertices[j]!=node:
                    pairs.append([self.vertices[i],self.vertices[j]])
        X=[]
        Y=[]
        Z=[]
        Z_final=[]


        for i in range(len(pairs)):
            X.append(len(self.all_shortest_paths(pairs[i][0],pairs[i][1])))

        
        for i in range(len(pairs)):
            Z=deepcopy((self.all_shortest_paths(pairs[i][0],pairs[i][1])))

            for i in range(len(Z)):
                Z_final.append(Z)
    
     
        for i in range(len(Z_final)):
            if Z_final.count(Z_final[i])>1:
                Z_final[i]=[]


        c=Z_final.count([])
        for i in range(c):
            Z_final.remove([])

        J=[]
        K=[]
        for i in range(len(Z_final)):
            
            if len(Z_final[i])==1:

                    if node not in Z_final[i][0]:
                        J.append([])

                    else:
                        J.append([Z_final[i][0]])


            else:
                
                K=[]
                COUNT=0
                for k in range(len(Z_final[i])):
                    
                    
                    if node in Z_final[i][k]:
                        K.append(Z_final[i][k])
                        COUNT+=1

                if COUNT==0:
                    J.append([])
                else:
                        J.append(K)
        

        for i in range(len(J)):
                if J[i]==[]:
                    Y.append(0)
                else:
                    Y.append(len(J[i]))


        BC=[]

        for i in range(len(X)):
            BC.append(Y[i]/X[i])

        s=sum(BC)
        return s

        raise NotImplementedError


    def top_k_betweenness_centrality(self):
        """
        Find top k nodes based on highest equal betweenness centrality.

        
        Returns:
            List a integer, denoting top k nodes based on betweenness
            centrality.
        """

        BC_list=[]

        for i in self.vertices:
            BC_list.append((self.betweenness_centrality(i)))

        m=max(BC_list)
        OUTPUT=[]
        cu=BC_list.count(m)

        for i in range(cu):
            ind=BC_list.index(m)
            OUTPUT.append(ind+1)

            BC_list[ind]=0.0
       

        return OUTPUT

        raise NotImplementedError



if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5, 6]
    edges    = [(1, 2), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5), (4, 6)]

    graph = Graph(vertices, edges)

    print(graph.top_k_betweenness_centrality())

    