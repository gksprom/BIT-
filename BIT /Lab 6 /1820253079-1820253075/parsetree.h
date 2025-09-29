#ifndef PARSETREE_H
#define PARSETREE_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct TreeNode {
    char *label;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

TreeNode* mkTree(const char *label, TreeNode *left, TreeNode *right);
void printTree(TreeNode *node, int indent);

#endif