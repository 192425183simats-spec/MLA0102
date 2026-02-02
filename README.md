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
End BFS



A* 
AStar(Graph, Start, Goal)
Create an empty Open list
Create an empty Closed list
Insert Start into Open list
Set g(Start) = 0
While Open list is not empty
Select node n with minimum f(n)
If n is Goal
Return solution path
End If
Move n from Open list to Closed list
For each neighbor m of n
If m is in Closed list
Continue
End If
Calculate g(m)
Calculate h(m)
Calculate f(m) = g(m) + h(m)
Insert or update m in Open list
End For
End While
End AStar



Water jug

WaterJug(JugA, JugB, Goal)
Initialize JugA = 0
Initialize JugB = 0
Create an empty set VISITED
While current state is not Goal
Fill JugA
Fill JugB
Empty JugA
Empty JugB
Pour water from JugA to JugB
Pour water from JugB to JugA
Check Goal state
Avoid repeated states
End While
End WaterJug
