/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;

        unordered_map<Node*, Node*> visited;
        return dfs(node, visited);
    }
private:
    Node* dfs(Node* node, unordered_map<Node*, Node*> & visited) {
        // int val; 1
        // vector<Node*> neighbors; 2, 4
        if (visited.count(node)) {
            return visited[node];
        }

        Node* clone_node = new Node(node->val);
        visited[node] = clone_node;

        for (Node* neighbor: node->neighbors) {
            Node* clone_neighbor = dfs(neighbor, visited);
            clone_node->neighbors.push_back(clone_neighbor);
        }
        return clone_node;
    }
    
};