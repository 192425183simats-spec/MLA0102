BFS(G, s)
1. Create an empty queue Q
2. Create an empty set VISITED

3. Mark s as visited
4. Enqueue s into Q

5. While Q is not empty do
6.     u ← Dequeue(Q)
7.     Print u

8.     For each vertex v adjacent to u do
9.         If v is not visited then
10.            Mark v as visited
11.            Enqueue v into Q
12.        End If
13.    End For
14. End While

