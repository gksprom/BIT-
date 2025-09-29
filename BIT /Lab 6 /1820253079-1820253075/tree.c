#include "parsetree.h"

TreeNode* mkTree(const char *label, TreeNode *left, TreeNode *right) {
    TreeNode *node = malloc(sizeof(TreeNode));
    node->label = strdup(label);
    node->left = left;
    node->right = right;
    return node;
}

void printTree(TreeNode *node, int indent) {
    if (!node) return;
    for (int i = 0; i < indent; i++) printf("  ");
    printf("%s\n", node->label);
    printTree(node->left, indent + 1);
    printTree(node->right, indent + 1);
}