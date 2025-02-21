#include <iostream>
#include <queue>
#include <vector> // Missing include for vector
using namespace std;

class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val) {
        this->val = val;
        this->left = NULL;
        this->right = NULL;
    }
};

TreeNode* createTree(TreeNode* root) {
    int value;
    cout << "Enter Value: ";
    cin >> value;

    if (value == -1) { // Base condition for stopping recursion
        return NULL;
    }

    root = new TreeNode(value); // Allocate memory for new node
    root->left = createTree(root->left);
    root->right = createTree(root->right);
    return root;
}

void levelOrderTraversal(TreeNode* root) {
    if (!root) return;

    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* frontNode = q.front();
        q.pop();

        cout << frontNode->val << " ";
        if (frontNode->left) {
            q.push(frontNode->left);
        }
        if (frontNode->right) {
            q.push(frontNode->right);
        }
    }
    cout << endl; // To ensure correct formatting
}

void rootToLeafTraversalHelper(TreeNode* root, int &temp, vector<int> &result) {
    if (!root) return;

    if (root->left == NULL && root->right == NULL) {
        temp*=10;
        temp+=root->val;
        result.push_back(temp);
        temp/=10;
        return;
    }

    temp*=10;
    temp+=root->val;
    rootToLeafTraversalHelper(root->left, temp, result);
    rootToLeafTraversalHelper(root->right, temp, result);
    temp/=10;
    return;
}

vector<int> rootToLeafTraversal(TreeNode* root) {
    vector<int> result;
    if (!root) return result;

    int temp = 0;
    rootToLeafTraversalHelper(root, temp, result);
    return result;
}

int main() {
    TreeNode* root = NULL;
    root = createTree(root);

    cout << "\nLevel Order Traversal: ";
    levelOrderTraversal(root);

    cout << "\nRoot to Leaf Paths:\n";
    vector<int> result = rootToLeafTraversal(root);
    int answer = 0;
    for (int i = 0; i < result.size(); i++) {
        answer+=result[i];
    }

    cout<<"Answer : "<< answer;
    return 0;
}
