# Critical Node Identification

- A critical node (also known as a cut vertex) in a graph is a node whose removal would increase the number of connected components in the graph.
- In other words, if you delete a critical node, the graph becomes disconnected or splits into multiple isolated parts.
- Critical nodes play a crucial role in maintaining the connectivity of the graph.
- They are often identified during network analysis, fault tolerance assessment, and communication network design.

1. **Betweenness Centrality**:
   - Betweenness centrality identifies nodes that act as bridges between other nodes.
   - Nodes with high betweenness centrality lie on many shortest paths between other nodes.
   - They are critical for maintaining communication and flow within the network.
   - Formula: $$\text{Betweenness Centrality} = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$
     where:
     - $\sigma_{st}$ is the total number of shortest paths from node $$s$$ to node $$t$$.
     - $\sigma_{st}(v)$ is the number of those paths that pass through node $$v$$.

2. **Closeness Centrality**:
   - Closeness centrality measures how quickly a node can reach other nodes in the network.
   - Nodes with high closeness centrality are critical for efficient communication.
   - Formula: $$\text{Closeness Centrality} = \frac{1}{\sum_{i} \text{Shortest Path Length from Node to Other Nodes}}$$

3. **Eigenvector Centrality**:
   - Eigenvector centrality considers both the node's connections and the centrality of its neighbors.
   - Nodes with high eigenvector centrality are connected to other influential nodes.
   - Formula: $$\mathbf{Ax} = \lambda \mathbf{x}$$
     where:
     - $\mathbf{A}$ is the adjacency matrix.
     - $\mathbf{x}$ is the eigenvector.
     - $\lambda$ is the eigenvalue.

4. **PageRank**:
   - PageRank, popularized by Google, ranks nodes based on their importance in a web graph.
   - Nodes with high PageRank are critical because they are linked to by other important nodes.
   - Formula: $$PR(v) = (1 - d) + d \sum_{u \in B_v} \frac{PR(u)}{L(u)}$$
     where:
     - $d$ is the damping factor (usually 0.85).
     - $B_v$ is the set of nodes linking to node $v$.
     - $L(u)$ is the out-degree of node $u$.

5. **Local Clustering Coefficient**:
   - The local clustering coefficient measures how well-connected a node's neighbors are.
   - Nodes with high local clustering coefficients form tightly interconnected clusters.
   - Critical nodes often have low local clustering coefficients because they act as bridges between different clusters.
   - Formula: $$C_i = \frac{2E_i}{k_i(k_i - 1)}$$
     where:
     - $C_i$ is the local clustering coefficient of node $$i$$.
     - $E_i$ is the number of edges between the neighbors of node $i$.
     - $k_i$ is the degree of node $i$.