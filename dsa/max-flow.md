# Maximum flow

In graph theory, a flow network is defined as a directed graph involving a source(*S*) and a sink(*T*) and several other nodes connected with edges. Each edge has an individual capacity which is the maximum limit of flow that edge could allow.

Flow in the network should follow the following conditions:

 - For any non-source and non-sink node, the input flow is equal to output flow.
 - For any edge(*E<sub>i</sub>*) in the network, 0 <= flow(*E<sub>i</sub>*) <= Capacity(*E<sub>i</sub>*).
 - Total flow out of the source node is equal total to flow in to the sink node.


### Maximum Flow

It is defined as the maximum amount of flow that the network would allow to flow from source to sink. Multiple algorithms exist in solving the maximum flow problem. Two major algorithms to solve these kind of problems are Ford-Fulkerson algorithm and Dinic's Algorithm.

### Ford-Fulkerson Algorithm

~~~
function: FordFulkerson(Graph G,Node S,Node T):
    Initialise flow in all edges to 0
    while (there exists an augmenting path(P) between S and T in residual network graph):
        Augment flow between S to T along the path P
        Update residual network graph
    return
~~~

An augmenting path is a simple path from source to sink which do not include any cycles and that pass only through positive weighted edges. A residual network graph indicates how much more flow is allowed in each edge in the network graph. If there are no augmenting paths possible from *S* to *T*, then the flow is maximum.

![](https://he-s3.s3.amazonaws.com/media/uploads/61e8b57.png)


# References

1. [Maximum flow](https://www.hackerearth.com/zh/practice/algorithms/graphs/maximum-flow/tutorial/)