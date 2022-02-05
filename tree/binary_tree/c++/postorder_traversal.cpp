#include <vector>

using namespace std;

/*** Definition for a binary tree node. */
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution{
public:
    void traverse(TreeNode* node, vector<int> *vals){
        if (node != NULL){
            traverse(node->left, vals);
            traverse(node->right, vals);
            vals->push_back(node->val);
        }
        return;     // very important for the performance
    }

    vector<int> preorderTraversal(TreeNode* root){
        vector<int> res;
        traverse(root, &res);
        return res;
    }
};