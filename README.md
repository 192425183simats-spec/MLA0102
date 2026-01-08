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
