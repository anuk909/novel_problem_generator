# Task ID: hard/9

## Prompt

```python
def minimum_quantum_spanning_tree(graph, edge_weights, qubits, quantum_state):
    """
    Imagine constructing a minimum spanning tree (MST) of a graph using Kruskal's algorithm, but with a twist involving quantum computing. Each edge of the graph is associated with a set of quantum bits (qubits), and the eligibility of an edge for the MST depends on the quantum state of these qubits represented by a bitmask. Here are the key elements:

    - 'graph' is a list of tuples representing edges, e.g., (0, 1).
    - 'edge_weights' provides the corresponding weights for these edges.
    - 'qubits' is a list of lists where each sublist contains qubits associated with the corresponding edge by index.
    - 'quantum_state' is an integer representing a bitmask where each bit corresponds to the state of a qubit. A qubit indexed 'i' is in the 'on' state if the 'i-th' bit in 'quantum_state' is '1; otherwise it's 'off'.

    To qualify an edge for the MST, the sum of 'on' states for the qubits associated with the edge must exhibit odd parity.

    The function returns the weight of the MST formed under these constraints or -1 if no valid MST can be formed.

    Examples:
    minimum_quantum_spanning_tree([(0, 1), (0, 2), (1, 2)], [2, 3, 1], [[0, 1], [1], [0]], 0b11) should return 1, as only the edge (1, 2) with weight 1 satisfies the condition.
    minimum_quantum_spanning_tree([], [], [], 0) should return 0, demonstrating how cases with no edges are treated (i.e., weight of an empty MST).
    """

```

## Canonical Solution

```python
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x != root_y:
                if self.rank[root_x] > self.rank[root_y]:
                    self.parent[root_y] = root_x
                elif self.rank[root_x] < self.rank[root_y]:
                    self.parent[root_x] = root_y
                else:
                    self.parent[root_y] = root_x
                    self.rank[root_x] += 1

    def is_valid_edge(qubits, qs_bitmask):
        total = sum((qs_bitmask >> q) & 1 for q in qubits)
        return total % 2 != 0

    def minimum_quantum_spanning_tree(graph, edge_weights, qubits, quantum_state):
        edges = sorted(zip(edge_weights, graph, qubits), key=lambda x: x[0])
        uf = UnionFind(max(max(u, v) for u, v in graph) + 1)
        mst_weight = 0
        edges_used = 0
        for weight, (u, v), edge_qubits in edges:
            if is_valid_edge(edge_qubits, quantum_state) and uf.find(u) != uf.find(v):
                uf.union(u, v)
                mst_weight += weight
                edges_used += 1
        return mst_weight if edges_used == len(graph) - 1 else -1
```

## Test Cases

```python
def check(candidate):
    assert candidate([(0, 1), (0, 2), (1, 2)], [2, 3, 1], [[0, 1], [1], [0]], 0b11) == 1
    assert candidate([(0, 1), (1, 2), (2, 3), (3, 0)], [1, 2, 3, 4], [[0], [1], [2], [3]], 0b1010) == 6
    assert candidate([(0, 1), (1, 2), (2, 0)], [10, 20, 30], [[0], [1], [0, 1]], 0) == -1
    assert candidate([(0, 1)], [5], [[0]], 1) == 5
    assert candidate([], [], [], 0) == 0
```

## Entry Point

`minimum_quantum_spanning_tree`

## Extra Info

## Topics

["Kruskal's Algorithm", 'Bitmask']

## Field

['Quantum Computing']

## Cleaned Prompt

```python
Write a function to compute the minimum spanning tree's weight under quantum constraints based on a bitmask representing quantum states. Each edge in the graph may only be included in the MST if its corresponding qubits have states that satisfy the 'odd parity of sum of 1's in bitmask' condition. Return -1 if a valid MST can't be formed.
```

## Warnings

- Solution failed correctness check. reason: failed: 
- 4, Ambiguous Problem Description: The problem specifies that the eligibility of an edge depends on the "odd parity of sum of 'on' states of its qubits". However, it does not mention how the qubits that are not 'on' (possibly in the 'off' state) affect the eligibility. The lack of comprehensive rules regarding 'off' state qubits could lead to multiple interpretations of edge eligibility.

