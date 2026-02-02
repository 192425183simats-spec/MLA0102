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

DecisionTree(Data, Features)

If all examples have same class:
    Return Leaf Node with that class
End If

If Features list is empty:
    Return Leaf Node with Majority Class
End If

Select the Best Feature F (using Info Gain or Gini Index)
Create a Root Node with Feature F

For each value v of Feature F:
    Subset = all examples where F = v
    If Subset is empty:
        Add Leaf Node with Majority Class
    Else:
        Child = DecisionTree(Subset, Features - F)
        Attach Child to Root Node for value v
    End If
End For

Return Root Node




A* 

AStar(Graph, Start, Goal)

Create an empty priority queue OPEN
Create an empty set CLOSED

Insert Start into OPEN with f(Start) = g(Start)+h(Start)
Set g(Start) = 0

While OPEN is not empty:
    Node = node in OPEN with smallest f value
    If Node == Goal:
        Return Path from Start to Goal
    End If

    Remove Node from OPEN
    Add Node to CLOSED

    For each neighbor N of Node:
        If N in CLOSED:
            Continue
        Tentative_g = g(Node) + cost(Node, N)
        If N not in OPEN:
            Add N to OPEN
        Else if Tentative_g >= g(N):
            Continue
        End If
        Set g(N) = Tentative_g
        Set f(N) = g(N) + h(N)
        Set Parent(N) = Node
End While

Return "No Path Found"



Water jug

WaterJug(JugX, JugY, Target)

Create empty queue Q
Create empty set VISITED
Insert initial state (0,0) into Q
Mark (0,0) as visited

While Q is not empty:
    State = Remove from Q
    If State has Target in any jug:
        Print Solution
        Stop
    End If

    For each possible action:
        1. Fill JugX
        2. Fill JugY
        3. Empty JugX
        4. Empty JugY
        5. Pour JugX -> JugY
        6. Pour JugY -> JugX
        Generate new State

        If new State not in VISITED:
            Insert new State into Q
            Mark new State as VISITED
End While


Min max
Minimax(Node, Depth, MaximizingPlayer)

If Node is a Terminal Node or Depth == 0:
    Return Evaluation(Node)

If MaximizingPlayer:
    MaxEval = -∞
    For each child of Node:
        Eval = Minimax(child, Depth-1, False)
        MaxEval = max(MaxEval, Eval)
    End For
    Return MaxEval
Else:
    MinEval = +∞
    For each child of Node:
        Eval = Minimax(child, Depth-1, True)
        MinEval = min(MinEval, Eval)
    End For
    Return MinEval
End If


Alpha-Beta puning

AlphaBeta(Node, Depth, α, β, MaximizingPlayer)

If Node is Terminal or Depth == 0:
    Return Evaluation(Node)

If MaximizingPlayer:
    Value = -∞
    For each child of Node:
        Value = max(Value, AlphaBeta(child, Depth-1, α, β, False))
        α = max(α, Value)
        If α ≥ β:
            Break   # β cut-off
    End For
    Return Value
Else:
    Value = +∞
    For each child of Node:
        Value = min(Value, AlphaBeta(child, Depth-1, α, β, True))
        β = min(β, Value)
        If β ≤ α:
            Break   # α cut-off
    End For
    Return Value
End If

