#include <stdlib.h>
#include <stdio.h>

typedef struct S {
    int* ints;
} S;

#define LEN 50

int main() {
    S s;
    unsigned i, j;
    int sum;

    s.ints = (int*)malloc(LEN * sizeof(int));

    j = 0u;
    for (i = 0u; i < LEN; ++i) {
        s.ints[i] = ++j;
    }

    sum = 0;
    for (i = 0u; i < LEN; ++i) {
        sum += s.ints[i];
    }

    printf("Sum! %i\n", sum);

    free(s.ints);
}
