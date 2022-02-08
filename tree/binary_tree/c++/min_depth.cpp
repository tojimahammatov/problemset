
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int depth = 100001;
    void traverseLeaves(TreeNode* node, int nodes_depth){
        if (!node){
            return;
        }
        if ((!(node->left)) && (!(node->right))){
            if (depth > nodes_depth){
                depth = nodes_depth;
            }
        }else{
            traverseLeaves(node->left, nodes_depth+1);
            traverseLeaves(node->right, nodes_depth+1);
        }
    }
    int minDepth(TreeNode* root) {
        if (!root){
            return 0;
        }
        traverseLeaves(root, 1);
        return depth;
    }
};
