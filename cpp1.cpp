#include <memory>

using std::unique_ptr;

struct S {
    unique_ptr<int[]> ints;
};

int main() {
    const int LEN = 50;
    auto s = S {
        unique_ptr<int[]> { new int[LEN] }
    };

    auto j = 0u;
    for (auto i = 0u; i < LEN; ++i) {
        s.ints[i] = ++j;
    }

    auto sum = 0;
    for (auto i = 0u; i < LEN; ++i) {
        sum += s.ints[i];
    }

    printf("Sum! %i\n", sum);
}
