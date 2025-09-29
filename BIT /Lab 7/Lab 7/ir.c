#include "ir.h"

static int temp_counter = 0;

char* new_temp() {
    char *buf = malloc(8);
    sprintf(buf, "t%d", temp_counter++);
    return buf;
}

List append(List head, List tail) {
    if (!head) return tail;
    List p = head;
    while (p->next) p = p->next;
    p->next = tail;
    return head;
}

List IRGenModule(TreeNode *node, char **result) {
    if (!node) return NULL;

    if (!node->left && !node->right) {
        *result = strdup(node->label);
        return NULL;
    }

    // Handle assignment separately
    if (strcmp(node->label, "=") == 0) {
        char *rhsVal;
        List rhsCode = IRGenModule(node->right, &rhsVal);

        Quad *q = malloc(sizeof(Quad));
        q->op = strdup("=");
        q->arg1 = rhsVal;
        q->arg2 = NULL;
        q->result = strdup(node->left->label);
        q->next = NULL;

        *result = q->result;
        return append(rhsCode, q);
    }

    char *leftVal, *rightVal;
    List leftCode = IRGenModule(node->left, &leftVal);
    List rightCode = IRGenModule(node->right, &rightVal);

    char *res = new_temp();
    Quad *q = malloc(sizeof(Quad));
    q->op = strdup(node->label);
    q->arg1 = leftVal;
    q->arg2 = rightVal;
    q->result = res;
    q->next = NULL;

    List code = NULL;
    code = append(code, leftCode);
    code = append(code, rightCode);
    code = append(code, q);

    *result = res;
    return code;
}

void printList(List list) {
    while (list) {
        if (list->arg2)
            printf("%s = %s %s %s\n", list->result, list->arg1, list->op, list->arg2);
        else
            printf("%s = %s\n", list->result, list->arg1);
        list = list->next;
    }
}