
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
    // int depth = 1;
    // void postorderTraverse(TreeNode* node, int nodes_depth){
    //     if (node!=nullptr){
    //         postorderTraverse(node->left, nodes_depth+1);
    //         postorderTraverse(node->right, nodes_depth+1);
    //         if (depth < nodes_depth){
    //             depth = nodes_depth;
    //         }
    //     }
    // }
    // int maxDepth(TreeNode* root) {
    //     if (!root){
    //         return 0;
    //     }
    //     postorderTraverse(root, 1);
    //     return depth;
    // }
    int maxDepth(TreeNode* root) {
        if (root == nullptr){
            return 0;
        }
        int l = 1 + maxDepth(root->left);
        int r = 1 + maxDepth(root->right);
        return l > r ? l : r;
    }
};