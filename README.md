BFS(Graph, Start)

Create an empty queue Q
Create an empty set VISITED

Mark Start as visited
Insert Start into Q

While Q is not empty
    Remove a vertex u from Q
    Print u

    For each vertex v adjacent to u
        If v is not in VISITED
            Mark v as visited
            Insert v into Q
        End If
    End For
End While


DFS(Graph, Start)

Create an empty set VISITED
Call DFS_Visit(Start)

DFS_Visit(u)
    If u is not in VISITED
        Mark u as visited
        Print u

        For each vertex v adjacent to u
            DFS_Visit(v)
        End For
    End If

Decision tree

Start with the complete dataset as the root node.
If all training examples belong to the same class, create a leaf node.
If no attributes remain, create a leaf node with the majority class.
Calculate entropy for each attribute.
Compute information gain for all attributes.
Select the attribute with the highest information gain.
Create a decision node using the selected attribute.
Split the dataset based on attribute values.
Repeat the process recursively for each subset.
Stop when all nodes are classified.

End Algorithm


A* 

Initialize the Open list with the start node.
Initialize the Closed list as empty.
For each node, calculate f(n) = g(n) + h(n).
Select the node with the lowest f(n) from the Open list.
If the selected node is the goal, return the solution path.
Move the node from Open list to Closed list.
Generate all neighboring nodes.
Ignore neighbors already in the Closed list.
Update cost and parent if a better path is found.
Add valid neighbors to the Open list.
Continue until the goal is reached or Open list becomes empty.

End Algorithm


Water jug

Start with both jugs empty.
Define the initial state and goal state.
Fill any jug completely.
Empty any jug.
Pour water from one jug to another until one is full or the other is empty.
Check whether the current state matches the goal state.
Avoid repeating previously visited states.
Continue the process until the goal state is reached or no solution exists.

End Algorithm
