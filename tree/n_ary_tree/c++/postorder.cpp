#include <vector>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
public:
    void traverse(Node* node, vector<int> *vals){
        if (node != NULL){
            int n = node->children.size();
            for(int i=0;i<n;i++){
                traverse(node->children[i], vals);
            }
            vals->push_back(node->val);
        }
        return;
    }
    vector<int> postorder(Node* root) {
        vector<int> res;
        traverse(root, &res);
        return res;
    }
};