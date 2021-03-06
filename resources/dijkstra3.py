graph = {'A':{'B':5,'C':7},
         'B':{'A':5,'D':10},
         'C':{'A':7,'D':8},
         'D':{'B':10,'C':8}}

d1graph = {'S':{'A':5, 'B':6, 'C':2},
           'A':{'S':5, 'D':4},
           'B':{'S':6, 'C':2, 'D':4, 'T':8},
           'C':{'S':2, 'B':2, 'T':12},
           'D':{'A':4, 'B':4, 'T':3},
           'T':{'B':8, 'C':12, 'D':3}}

owngraph1 = {'A':{'B':5,'C':8,'D':7},
             'B':{'A':5,'C':2,'E':1},
             'C':{'A':8,'B':2,'E':5,'F':9},
             'D':{'A':7,'F':11},
             'E':{'B':1,'C':5,'G':3},
             'F':{'C':9,'D':11,'G':10},
             'G':{'E':3,'F':10}}

import math
class Node(object):
    '''
    A node is a single point on a nodegraph.
    Attributes:
        identifier: a string as a letter or combination of letters to identify the node
        visited: a boolean determining if the node has been visisted
        shortest: an integer that represents the shortest length from start node to the given node
        previous: a string representing the identifier of the previous node
        connectors: a dictionary (associative array) defining all connectors and their length for a node
    '''

    def __init__(self, identifier, visited, shortest, previous, connectors = {}):
        self.identifier = str(identifier)
        self.visited = bool(visited)
        self.shortest = int(shortest)
        self.previous = str(previous)
        self.connectors = connectors
    
class Graph(object):
    '''
    A graph instantiates and groups Nodes.
    Attributes:
        name: a string representing the name of the graph
        nodes: a dictionary of node instances
        startNode: a string representing the start point
        endPoint: a string representing the end point
        currentNode: a node instance reprenting the current node being used
        unvisited: a list of node identifiers as strings representing unvisited nodes
        finalLength: an integer representing the final length of the shortest path
        finalRoute: a list of node identifiers as strings representing the final shortest path route
    '''

    name = "the graph"
    
    nodes = {}
    startNode = str()
    endNode = str()
    currentNode = object()

    unvisited = list()
    
    finalLength = int()
    finalRoute = list()

    shortestnode = str()
    shortestnodeval = float("inf")
    
    finished = False
    
    def __init__(self, graph_dict):
        for node, connections in sorted(graph_dict.items()):
            connectors = {}
            for connector, distance in sorted(connections.items()):
                connectors[connector] = str(distance)
            self.nodes[node] = Node(node, False, 0, "", connectors)
        
    def listNodes(self):
        nodelist = []
        for node in sorted(self.nodes):
            nodelist.append(node)
            nodelist.sort()
        return nodelist
    
    def findShortest(self, start_node, end_node):
        self.startNode = start_node
        self.endNode = end_node
        self.currentNode = self.nodes[self.startNode]
        self.unvisited.append(self.currentNode.identifier)
        
        while(self.unvisited): ##is unvisited list empty?
            for connector, length in sorted(self.currentNode.connectors.items()): ##loop round all connectors attached to current node
                connectorObject = self.nodes[connector]
                if(not connectorObject.visited):
                    if((connectorObject.shortest == 0) or (int(length) < int(connectorObject.shortest))):
                        if(self.currentNode.previous):
                            prevnode = str(self.currentNode.previous)
                            connectorObject.shortest = int((self.nodes[prevnode]).shortest) + int(length)
                        else:
                            connectorObject.shortest = length
                        connectorObject.previous = self.currentNode.identifier
                        if(connectorObject.visited != True):
                            self.unvisited.append(connectorObject.identifier)
            self.unvisited.remove(self.currentNode.identifier)
            self.currentNode.visited = True
            self.shortestnode = str()
            self.shortestnodeval = float("inf")
            for node in self.unvisited:
                nodeobject = self.nodes[node]
                if(float(nodeobject.shortest) < float(self.shortestnodeval)):
                    self.shortestnodeval = nodeobject.shortest
                    self.shortestnode = nodeobject.identifier
            if(self.shortestnode):
                self.currentNode = self.nodes[self.shortestnode]
        self.finalRoute.append(self.endNode)
        self.currentNode = self.nodes[self.endNode]
        print(newgraph.nodes['T'].shortest)
        while(self.finished == False):
##            print(self.currentNode.identifier)
            if(self.currentNode.identifier == self.startNode):
                self.finished = True
            else:
                self.finalRoute.append(self.currentNode.previous)
                self.currentNode = self.nodes[self.currentNode.previous]

newgraph = Graph(d1graph)
print("This graph contains nodes "+(str(newgraph.listNodes())))
print("This graph includes vertex "+newgraph.nodes['A'].identifier)
print("This node is connected to "+(str(newgraph.nodes['A'].connectors)))
if(newgraph.nodes['A'].visited):
    print("and it has been visited")
else:
    print("and it has not been visited")
newgraph.findShortest('S','T')
print("The shortest length from A to D is "+str(newgraph.nodes['T'].shortest))
print("The quickest route from A to D is ", newgraph.finalRoute)
