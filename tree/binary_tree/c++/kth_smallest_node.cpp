
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
    // void inorder(TreeNode* node, vector<int>* vals){
    //     if (node){
    //         inorder(node->left, vals);
    //         vals->push_back(node->val);
    //         inorder(node->right, vals);
    //     }
    //     return;
    // }
    // int kthSmallest(TreeNode* root, int k) {
    //     if (!root){
    //         return 0;;
    //     }
    //     vector<int> nums;
    //     inorder(root, &nums);
    //     return nums[k-1];
    // }
    int count = 0;
    int kthSmallest(TreeNode* root, int k){
        if (root->left){
            int l = kthSmallest(root->left, k);
            if (l != -1){
                return l;
            }
        }
        count++;
        if(count == k){
            return root->val;
        }
        if (root->right){
            int r = kthSmallest(root->right, k);
            if (r != -1){
                return r;
            }
        }
        return -1;
    }
};