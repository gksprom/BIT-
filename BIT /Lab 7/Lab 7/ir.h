#ifndef IR_H
#define IR_H

#include "parsetree.h"

typedef struct Quad {
    char *op;
    char *arg1;
    char *arg2;
    char *result;
    struct Quad *next;
} Quad;

typedef Quad* List;

List IRGenModule(TreeNode *node, char **result);
void printList(List list);

#endif